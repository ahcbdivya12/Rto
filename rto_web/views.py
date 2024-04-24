from django.conf import settings
from django.shortcuts import render,redirect

from django.contrib.auth.models import User

from django.urls import reverse

from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.template import loader

from django.contrib import messages

from django.contrib.auth.models import User

import stripe

from django.urls import reverse


from django.conf import settings


@login_required(login_url='login')


def vehical_change(request):
    return render(request, 'vehical_change.html')


# Create your views here.
def index(request):
	return render(request,"index.html",{})

def category(request):
	return render(request,"categorys.html",{})

def about(request):
	return render(request,"about.html",{})

def print_from(request):
	return render(request,"print_from.html",{})


stripe.api_key = settings.STRIPE_SECRET_KEY


import stripe
from django.conf import settings
from django.http import JsonResponse
from django.urls import reverse
from django.shortcuts import redirect

stripe.api_key = settings.STRIPE_SECRET_KEY

def create_checkout_session(request):
    # Collect customer's name and address
    customer_name = request.POST.get('customer_name')
    customer_address = request.POST.get('customer_address')

    # Determine the currency based on the customer's location
    currency = 'inr' if customer_address and customer_address.lower() == 'india' else 'usd'

    # Create a new Checkout Session
    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[
            {
                'price_data': {
                    'currency': currency,
                    'product_data': {
                        'name': 'Driving Licence',
                    },
                    'unit_amount': 12000,  # Amount in cents
                },
                'quantity': 1,
            },
        ],
        mode='payment',
        customer_email=request.user.email,  # Assuming the user is logged in
        shipping_address_collection={
            'allowed_countries': ['IN'] if currency == 'inr' else None,
        },
        metadata={
            'customer_name': customer_name,
            'customer_address': customer_address,
        },
        success_url=request.build_absolute_uri(reverse('success')),
        cancel_url=request.build_absolute_uri(reverse('cancel')),
    )

    return redirect(session.url)

def success(request):
	return render(request, 'success.html')

def cancel(request):
    return render(request, 'cancel.html')
    
from django.contrib.auth.models import User
from django.shortcuts import render
import random
import string
from django.core.mail import send_mail
from django.conf import settings
from .models import registration  # Import your Registration model

def forget(request):
    if request.method == 'POST':
        email = request.POST.get('email')

        # Check if email exists in both User table and Registration table
        user_exists = User.objects.filter(email=email).exists()
        registration_exists = registration.objects.filter(email=email).exists()

        if user_exists and registration_exists:
            # Generate a random password
            new_password = ''.join(random.choices(string.ascii_letters + string.digits, k=8))

            # Send email with new password
            send_mail(
                'Password Reset',
                f'Your new password is: {new_password}',
                settings.EMAIL_HOST_USER,
                [email],
                fail_silently=False,
            )

            # Update password in User table
            if user_exists:
                user = User.objects.get(email=email)
                user.set_password(new_password)
                user.save()

            # Update password in Registration table
            if registration_exists:
                registration_user = registration.objects.get(email=email)
                registration_user.password = new_password
                registration_user.confirm_password = new_password
                registration_user.save()

            return render(request, 'forget.html', {'success_message': 'Password reset successful. Check your email for the new password.'})
        else:
            return render(request, 'forget.html', {'error_message': 'Email not found in both User and Registration tables.'})

    return render(request, 'forget.html')

from .models import conta
def contact(request):
	if request.method=='POST':
		uname=request.POST.get('uname')
		email=request.POST.get('email')
		subject=request.POST.get('subject')
		message=request.POST.get('message')
		if conta.objects.filter(email=email).exists():
			messages.warning(request,'email is already exists!')
			return redirect(contact)
		else:
			dbs_2 = conta(name=uname, email=email, subject=subject, message=message)
			dbs_2.save()
			return redirect('/')
	return render(request, "contact.html",{})

def guid(request):
	return render(request,"guid.html",{})

from .models import appoinment_data

def appoinment(request):
	if request.method == 'POST':
		date_u = request.POST.get('date')
		time_u = request.POST.get('time')

		if appoinment_data.objects.filter(date=date_u,time=time_u).exists():
			messages.warning(request,'The Slot Is Already Booked')
		else:
			dbs_4 = appoinment_data(date=date_u,time=time_u)
			dbs_4.save()
			return render(request, 'checkout.html', {}) 
	return render(request,"appinment.html",{})

from .models import otp
from .models import dl
def confirm(request):
    if request.method == 'POST':
        user_otp = request.POST.get('otp')
        mobile_number = request.POST.get('m_no')
        phone_number_entry = dl.objects.filter(mobile=mobile_number).first()
        if phone_number_entry:
        	return redirect(appoinment)
        else:
            messages.warning(request, 'Your number was not verified')
    return render(request, "confirm.html", {})


from .models import otp
from .models import dl
from django.shortcuts import render
from django.contrib import messages
from django.http import HttpRequest
from django.template.loader import render_to_string
from service.views import dl_print

def change_confirm(request):
    if request.method == 'POST':
        dl_number = request.POST.get('dl_number')
        mobile_number = request.POST.get('m_no')
        otp_value = request.POST.get('otp')
        if dl.objects.filter(rto_number=dl_number,mobile=mobile_number, otp=otp_value,).exists():
            try:
                data = dl.objects.get(rto_number=dl_number)
                column_id = data.id
                dl_print_html_content = dl_print(HttpRequest(), column_id).content.decode('utf-8')
                return render(request, 'another_page.html', {'dl_print_content': dl_print_html_content})
            except dl.DoesNotExist:
                messages.warning(request, 'Data not found in app_2')
        else:
            messages.warning(request, 'Your number was not verified')
    return render(request, 'change_confirm.html')
from django.contrib import messages
from .models import VehicleRegistration
from service.views import rto_rc_book  # Import the view to print vehicle registration details


def rc_book(request):
    if request.method == 'POST':
        vin = request.POST.get('vin_number')
        if VehicleRegistration.objects.filter(vin=vin).exists():
            try:
                data = VehicleRegistration.objects.get(vin=vin)
                column_id = data.id
                # Assuming display_vehical_info is a view that generates HTML content for printing vehicle registration details
                rto_rc_book_html_content = rto_rc_book(request, column_id).content.decode('utf-8')
                return render(request, 'rc_book_display.html', {'rto_rc_book_content': rto_rc_book_html_content})
            except VehicleRegistration.DoesNotExist:
                messages.warning(request, 'Data not found in app_2')
        else:
            messages.warning(request, 'Your number was not verified')
    return render(request, 'rc_book_info.html')

from django.contrib import messages
from .models import VehicleRegistration
from service.views import display_vehical_info  # Import the view to print vehicle registration details

def vehical_info(request):
    if request.method == 'POST':
        vin = request.POST.get('vin_number')
        if VehicleRegistration.objects.filter(vin=vin).exists():
            try:
                data = VehicleRegistration.objects.get(vin=vin)
                column_id = data.id
                # Assuming display_vehical_info is a view that generates HTML content for printing vehicle registration details
                display_vehical_info_html_content = display_vehical_info(request, column_id).content.decode('utf-8')
                return render(request, 'rc_another_page.html', {'display_vehical_info_content': display_vehical_info_html_content})
            except VehicleRegistration.DoesNotExist:
                messages.warning(request, 'Data not found in app_2')
        else:
            messages.warning(request, 'Your number was not verified')
    return render(request, 'vehical_info.html')


def change_confirm_renewal(request):
    if request.method == 'POST':
        mobile_number = request.POST.get('m_no')
        otp_value = request.POST.get('otp')
        if dl.objects.filter(mobile=mobile_number, otp=otp_value).exists():
            try:
                data = dl.objects.get(mobile=mobile_number)
                column_id = data.id
                dl_print_html_content = dl_print(HttpRequest(), column_id).content.decode('utf-8')
                return render(request, 'another_page_renewal.html', {'dl_print_content': dl_print_html_content})
            except dl.DoesNotExist:
                messages.warning(request, 'Data not found in app_2')
        else:
            messages.warning(request, 'Your number was not verified')
    return render(request, 'change_confirm_renewal.html')


from .models import dl, RenewalHistory
from datetime import datetime, timedelta

def renewal(request):
    if request.method == 'POST':
        # Retrieve data from the form
        rto_state = request.POST.get('rto_state')
        rto_office = request.POST.get('rto_office')
        rto_pincode = request.POST.get('rto_pincode')
        mobile = request.POST.get('mobile')
        otp = request.POST.get('otp')
        issues_state = request.POST.get('issue_state')
        issue_date = request.POST.get('issue_date')
        expire_date = request.POST.get('expir_date')
        photo = request.POST.get('d_1_2')
        sign = request.POST.get('d_1_3')
        document = request.POST.get('document_1')
        proof = request.POST.get('proof')
        doc_no = request.POST.get('d_no')
        issue_date_doc = request.POST.get('d_issue_date')
        issues_by = request.POST.get('issued_by')
        doc_1 = request.POST.get('d_1')
        document_2 = request.POST.get('document_2')
        proof_2 = request.POST.get('proof_2')
        doc_no_2 = request.POST.get('d_no_2')
        issue_date_2 = request.POST.get('d_issue_date_2')
        issues_by_2 = request.POST.get('issued_by_2')
        doc_2 = request.POST.get('d_1_2')
        document_3 = request.POST.get('document_3')
        proof_3 = request.POST.get('proof_3')
        doc_no_3 = request.POST.get('d_no_3')
        issue_date_3 = request.POST.get('d_issue_date_3')
        issues_by_3 = request.POST.get('issued_by_3')
        doc_3 = request.POST.get('d_1_3')

        try:
            existing_record = dl.objects.get(mobile=mobile)
        except dl.DoesNotExist:
            existing_record = None

        if existing_record:
            if (
                existing_record.rto_state == rto_state,
                existing_record.rto_office == rto_office, 
                existing_record.rto_pincode == rto_pincode, 
                existing_record.issues_state == issues_state ,
                existing_record.issue_date == issue_date ,
                existing_record.photo == photo ,
                existing_record.sign == sign ,
                existing_record.document == document ,
                existing_record.proof == proof ,
                existing_record.doc_no == doc_no ,
                existing_record.issue_date_doc == issue_date_doc ,
                existing_record.issues_by == issues_by ,
                existing_record.doc_1 == doc_1 ,
                existing_record.document_2 == document_2 ,
                existing_record.proof_2 == proof_2 ,
                existing_record.doc_no_2 == doc_no_2 ,
                existing_record.issue_date_2 == issue_date_2 ,
                existing_record.issues_by_2 == issues_by_2 ,
                existing_record.document_3 == document_3 ,
                existing_record.proof_3 == proof_3 ,
                existing_record.doc_no_3 == doc_no_3 ,
                existing_record.issue_date_3 == issue_date_3 ,
                existing_record.issues_by_3 == issues_by_3

            ):
                print('mobile verify')
                renewal_history =RenewalHistory.objects.create(
                	rto_state=existing_record.rto_state,
                	rto_office=existing_record.rto_office,
                	rto_pincode=existing_record.rto_pincode,
                	mobile=existing_record.mobile,
                	photo=existing_record.photo,
                	sign=existing_record.sign,
                	document=existing_record.document,
                	proof=existing_record.proof,
                	doc_no=existing_record.doc_no,
                	issue_date_doc=existing_record.issue_date_doc,
                	issues_by=existing_record.issues_by,
                	doc_1=existing_record.doc_1,
                	document_2=existing_record.document_2,
                	proof_2=existing_record.proof_2,
                	doc_no_2=existing_record.doc_no_2,
                	issue_date_2=existing_record.issue_date_2,
                	issues_by_2=existing_record.issues_by_2,
                	document_3=existing_record.document_3,
                	proof_3=existing_record.proof_3,
                	doc_no_3=existing_record.doc_no_3,
                	issue_date_3=existing_record.issue_date_3,
                	issues_by_3=existing_record.issues_by_3,
            
                    expire_date=existing_record.expire_date
                )
                
                renewal_history.expire_date += timedelta(days=20*365)
                renewal_history.save()
                return render(request, 'checkout.html', {})
            else:
                # If the data doesn't match, render a page indicating that the data doesn't match
                return render(request, 'categorys.html', {})
        else:
            # If no record exists for the given mobile number, render a page indicating that the data doesn't match
            return render(request, 'appinment.html', {}) 
    return render(request, "renewal.html", {})

from .models import dl, DuplicateHistory
from datetime import datetime, timedelta

def duplicate_form(request):
    if request.method == 'POST':
        applicant_name = request.POST.get('applicant_name')
        applicant_address = request.POST.get('applicant_address')
        mobile = request.POST.get('mobile')
        rto_number = request.POST.get('rto_number')
        reason_for_duplicate = request.POST.get('reason_for_duplicate')
        photo = request.POST.get('d_1_2')
        sign = request.POST.get('d_1_3')
        document = request.POST.get('document_1')
        proof = request.POST.get('proof')
        doc_no = request.POST.get('d_no')
        issue_date_doc = request.POST.get('d_issue_date')
        issues_by = request.POST.get('issued_by')
        doc_1 = request.POST.get('d_1')
        document_2 = request.POST.get('document_2')
        proof_2 = request.POST.get('proof_2')
        doc_no_2 = request.POST.get('d_no_2')
        issue_date_2 = request.POST.get('d_issue_date_2')
        issues_by_2 = request.POST.get('issued_by_2')
        doc_2 = request.POST.get('d_1_2')
        document_3 = request.POST.get('document_3')
        proof_3 = request.POST.get('proof_3')
        doc_no_3 = request.POST.get('d_no_3')
        issue_date_3 = request.POST.get('d_issue_date_3')
        issues_by_3 = request.POST.get('issued_by_3')
        doc_3 = request.POST.get('d_1_3')
        
        try:
            existing_record = dl.objects.get(mobile=mobile)
        except dl.DoesNotExist:
            existing_record = None
        
        if existing_record:
            if (
                existing_record.rto_number == rto_number ,
                existing_record.photo == photo ,
                existing_record.sign == sign ,
                existing_record.document == document ,
                existing_record.proof == proof ,
                existing_record.doc_no == doc_no ,
                existing_record.issue_date_doc == issue_date_doc ,
                existing_record.issues_by == issues_by ,
                existing_record.doc_1 == doc_1 ,
                existing_record.document_2 == document_2 ,
                existing_record.proof_2 == proof_2 ,
                existing_record.doc_no_2 == doc_no_2 ,
                existing_record.issue_date_2 == issue_date_2 ,
                existing_record.issues_by_2 == issues_by_2 ,
                existing_record.document_3 == document_3 ,
                existing_record.proof_3 == proof_3 ,
                existing_record.doc_no_3 == doc_no_3 ,
                existing_record.issue_date_3 == issue_date_3 ,
                existing_record.issues_by_3 == issues_by_3
            ):
                duplicate_history = DuplicateHistory.objects.create(
                    applicant_name=applicant_name,
                    applicant_address=applicant_address,
                    contact_number=existing_record.mobile,
                    license_number=existing_record.rto_number,
                    reason_for_duplicate=reason_for_duplicate,
                    photo=existing_record.photo,
                    sign=existing_record.sign,
                    document=existing_record.document,
                    proof=existing_record.proof,
                    doc_no=existing_record.doc_no,
                    issue_date_doc=existing_record.issue_date_doc,
                    issues_by=existing_record.issues_by,
                    doc_1=existing_record.doc_1,
                    document_2=existing_record.document_2,
                    proof_2=existing_record.proof_2,
                    doc_no_2=existing_record.doc_no_2,
                    issue_date_2=existing_record.issue_date_2,
                    issues_by_2=existing_record.issues_by_2,
                    document_3=existing_record.document_3,
                    proof_3=existing_record.proof_3,
                    doc_no_3=existing_record.doc_no_3,
                    issue_date_3=existing_record.issue_date_3,
                    issues_by_3=existing_record.issues_by_3,
                )
                duplicate_history.save()
                return render(request, 'checkout.html', {})
            else:
                # If the data doesn't match, render a page indicating that the data doesn't match
                return render(request, 'categorys.html', {})
        else:
            # If no record exists for the given mobile number, render a page indicating that the data doesn't match
            return render(request, 'appinment.html', {}) 
    return render(request, "duplicate_form.html", {})


from django.shortcuts import render
from .models import dl

def change_info(request):
	if request.method == 'POST':
		selected_option = request.POST.get('change_option')
		print("Selected Option:", selected_option)  # Debugging
		if selected_option == "address":
			return render(request, 'change_address.html', {})
		if selected_option == "number":
			return render(request, 'mobile_number_change.html', {})
		if selected_option == "fullname":
			return render(request, 'change_name.html', {})
		if selected_option == "perent":
			return render(request, 'prent_change.html', {})
	return render(request, 'change_info.html', {})

def change_address(request):
	if request.method == 'POST':
		name = request.POST.get('name')
		country = request.POST.get('country')
		state = request.POST.get('state')
		city = request.POST.get('city')
		address = request.POST.get('address')
		pincode = request.POST.get('pincode')
		try:
			dl_instance = dl.objects.get(name=name)
			dl_instance.country = country
			dl_instance.state = state
			dl_instance.city = city
			dl_instance.address = address
			dl_instance.pincode = pincode
			dl_instance.save()
			return render(request, 'checkout.html', {})  # Render a confirmation page
		except dl.DoesNotExist:
			return render(request, 'change_info.html', {})  # Render a change_infoation page

def mobile_number_change(request):
	if request.method == 'POST':
		name = request.POST.get('name')
		mobile = request.POST.get('mobile')
		a_mobile = request.POST.get('a_mobile')
		otp = request.POST.get('otp')
		try:
			dl_instance = dl.objects.get(name=name)
			dl_instance.mobile = mobile
			dl_instance.otp = otp
			dl_instance.a_mobile = a_mobile
			dl_instance.save()
			return render(request, 'checkout.html', {})  # Render a change_infoation page
		except dl.DoesNotExist:
			return render(request, 'change_info.html', {})  # Render a change_infoation page

def name_change(request):
	if request.method == 'POST':
		ex_name = request.POST.get('ex_name')
		name = request.POST.get('name')
		try:
			dl_instance = dl.objects.get(name=ex_name)
			dl_instance.name = name
			dl_instance.save()
			return render(request, 'checkout.html', {})  # Render a change_infoation page
		except dl.DoesNotExist:
			return render(request, 'change_info.html', {})  # Render a change_infoation page
def prent_change(request):
	if request.method == 'POST':
		father_name = request.POST.get('father_name')
		mother_name = request.POST.get('mother_name')
		
		name = request.POST.get('name')
		try:
			dl_instance = dl.objects.get(name=name)
			dl_instance.father_name = father_name
			dl_instance.mother_name = mother_name
			dl_instance.save()
			return render(request, 'checkout.html', {})  # Render a change_infoation page
		except dl.DoesNotExist:
			return render(request, 'change_info.html', {})  # Render a change_infoation page

from .models import dl 
def l_form(request):
	if request.method=='POST':
		rto_state=request.POST.get('rto_state')
		rto_office=request.POST.get('rto_office')
		rto_pincode=request.POST.get('rto_pincode')
		name=request.POST.get('f_name')
		father_name=request.POST.get('fathername')
		mother_name=request.POST.get('mothername')
		adhar_card_no=request.POST.get('adh_no')
		date=request.POST.get('dob')
		birth_p=request.POST.get('b_p');
		email=request.POST.get('email');
		mobile=request.POST.get('m_no');
		otp=request.POST.get('otp');
		gender=request.POST.get('gender');
		relation=request.POST.get('relation');
		age=request.POST.get('age');
		qulification=request.POST.get('qualification');
		b_group=request.POST.get('blood_group');
		a_mobile=request.POST.get('a_m_no');
		occupation=request.POST.get('occupation');
		country=request.POST.get('country');
		state=request.POST.get('state');
		city=request.POST.get('city');
		address=request.POST.get('address');
		pincode=request.POST.get('pincode');
		issues_state=request.POST.get('issue_state');
		issue_date=request.POST.get('issue_date');
		expire_date=request.POST.get('expir_date');
		disablity_yn=request.POST.get('d');
		disablit=request.POST.get('disbility');
		doner=request.POST.get('organs');
		all_yes=request.POST.get('data');
		photo=request.POST.get('d_1_2');
		sign=request.POST.get('d_1_3');
		document=request.POST.get('document_1');
		proof=request.POST.get('proof');
		doc_no=request.POST.get('d_no');
		issue_date_doc=request.POST.get('d_issue_date');
		issues_by=request.POST.get('issued_by');
		doc_1=request.POST.get('d_1');
		document_2=request.POST.get('document_2');
		proof_2=request.POST.get('proof_2');
		doc_no_2=request.POST.get('d_no_2');
		issue_date_2=request.POST.get('d_issue_date_2');
		issues_by_2=request.POST.get('issued_by_2');
		doc_2=request.POST.get('d_1_2');
		document_3 = request.POST.get('document_3')
		proof_3 = request.POST.get('proof_3')
		doc_no_3 = request.POST.get('d_no_3')
		issue_date_3 = request.POST.get('d_issue_date_3')
		issues_by_3 = request.POST.get('issued_by_3')
		doc_3 = request.POST.get('d_1_3')

		if dl.objects.filter(mobile=mobile).exists():
			return render(request,"l_form.html",{})  # Update the redirection path to a valid URL or view function
		else:
			dbs_1 = dl(rto_state=rto_state, rto_office=rto_office, rto_pincode=rto_pincode, name=name, father_name=father_name, mother_name=mother_name, adhar_card_no=adhar_card_no, 
                date=date, birth_p=birth_p, email=email, mobile=mobile, otp=otp, gender=gender, relation=relation, age=age, qulification=qulification, b_group=b_group, a_mobile=a_mobile,
                occupation=occupation, country=country, state=state, city=city, address=address, pincode=pincode, issues_state=issues_state, issue_date=issue_date, 
                expire_date=expire_date, disablity_yn=disablity_yn, disablit=disablit, doner=doner, all_yes=all_yes, photo=photo, sign=sign, document=document, 
                proof=proof, doc_no=doc_no, issue_date_doc=issue_date_doc, issues_by=issues_by, doc_1=doc_1, document_2=document_2, proof_2=proof_2, doc_no_2=doc_no_2,
                issue_date_2=issue_date_2, issues_by_2=issues_by_2, doc_2=doc_2, document_3=document_3, proof_3=proof_3, doc_no_3=doc_no_3,
                issue_date_3=issue_date_3, issues_by_3=issues_by_3, doc_3=doc_3)
			dbs_1.save()
			return render(request,"confirm.html",{})
	return render(request,"l_form.html",{})

from .models import registration 

def singup(request):
	if request.method=='POST':
		uname=request.POST.get('username')
		email=request.POST.get('email')
		pass1=request.POST.get('password1')
		pass2=request.POST.get('cpassword')
		address=request.POST.get('address')
		mobile=request.POST.get('mobile')
		gender=request.POST.get('gender')
		state=request.POST.get('state')

		if User.objects.filter(email=email).exists():
			messages.warning(request,'email is already exists!')
			return redirect(singup)
		elif pass1!=pass2:
			messages.warning(request,'password and confirm password does not match !')
			return redirect(singup)
		else:
			dbs = registration(name=uname, email=email, password=pass1, cpassword=pass2, address=address, mobile=mobile, gender=gender, state=state)
			dbs.save()
			my_user = User.objects.create_user(uname,email,pass1)
			my_user.save()				
			return redirect('../u_login')
	return render(request,"signup.html",{})

from django.contrib.auth import login as auth_login

def user_login(request):
	if request.method=='POST':
		username=request.POST.get('username')
		pass1=request.POST.get('password1')
		user=authenticate(request,username=username,password=pass1)
		if user is not None:
			login(request,user)
			return redirect('http://127.0.0.1:8000/')
		else:
			return redirect('../u_login')
	return render(request,'login.html')	

def LogoutPage(request):
	logout(request)
	return redirect('../u_login')
