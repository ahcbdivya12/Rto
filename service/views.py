from django.shortcuts import render,redirect
from django.contrib.auth import logout


from rto_web.models import dl,appoinment_data,otp,registration,office,conta,VehicleRegistration

from django.contrib import messages
# Create your views here.
def rto_index(request):
	return render(request,"rto_index.html",{})


def rto_appoinment(request):
	database_data = appoinment_data.objects.all()
	return render(request,"rto_appoinment.html",{'database_data': database_data})

def rto_dl_verification(request):
	database_data = otp.objects.all()
	return render(request,"rto_dl_verification.html",{'database_data': database_data})


# views.py

def rto_show_vehicalinfo(request):
	vehicle_data = VehicleRegistration.objects.all()
	return render(request,"rto_show_vehicalinfo.html",{'vehicle_data': vehicle_data})

def rto_vehical_reg(request):
    if request.method == 'POST':
        # Extract data from the request

        owner_name = request.POST.get('name')
        owner_address = request.POST.get('address')
        owner_address_temp = request.POST.get('address_temp')
        insurance=request.POST.get('i_comp')
        
        make = request.POST.get('makeModel')
        model = request.POST.get('model')
        manufacture_year = request.POST.get('manufactureYear')
        vin = request.POST.get('vin')
        mileage = request.POST.get('mileage')
        engine = request.POST.get('engine')
        transmission = request.POST.get('transmission')
        fuel = request.POST.get('fuel')
        color = request.POST.get('color')
        body_style = request.POST.get('bodyStyle')
        features = request.POST.get('features')
        condition = request.POST.get('condition')
        ownership_history = request.POST.get('ownershipHistory')
        price = request.POST.get('price')
        location = request.POST.get('location')
        state_code= request.POST.get('state_code')
        city_code= request.POST.get('city_code')
        
        registration_info = request.POST.get('registrationInfo')
        title_status = request.POST.get('titleStatus')
        
        # Create a new instance of the model
        vehicle = VehicleRegistration(
            owner_name=owner_name,
            owner_address=owner_address,
            owner_address_temp=owner_address_temp,
            insurance=insurance,
            
            make=make,
            model=model,
            manufacture_year=manufacture_year,
            vin=vin,
            mileage=mileage,
            engine=engine,
            transmission=transmission,
            fuel=fuel,
            color=color,
            body_style=body_style,
            features=features,
            condition=condition,
            ownership_history=ownership_history,
            price=price,
            location=location,
            registration_info=registration_info,
            title_status=title_status,
            state_code=state_code,
            city_code=city_code
        )
        
        # Save the instance to the database
        vehicle.save()
        
        # Redirect to a success page or any other desired page
        return redirect(rto_show_vehicalinfo)
 
		  # Replace 'success_page' with the name of your success page URL
    
    return render(request, 'rto_vehical_reg.html')

# views.py
import random

def generate_vehicle_number(state_code, city):
    # You can adjust the state code and city as per your database model
    # Assuming state_code is a 2-letter code and city is a string
    state_code = state_code.upper()  # Convert to uppercase if not already
    city = city.upper().replace(" ", "")  # Convert to uppercase and remove spaces

    # Generate a random 4-letter sequence (corresponding to "JD" in alphabetical order)
    random_letters = ''.join(random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(2))

    # Generate a random 4-digit number
    random_number = random.randint(1000, 9999)

    # Concatenate the components to form the vehicle number
    vehicle_number = f"{state_code}-{city}-{random_letters}-{random_number}"
    return vehicle_number
def display_vehical_info(request, column_id):
    try:
        vehicle = VehicleRegistration.objects.get(id=column_id)
        if not vehicle.vin:  # Check if the vin field is empty
            vehicle_number = generate_vehicle_number(vehicle.state_code, vehicle.city_code)
            vehicle.vin = vehicle_number
            vehicle.save()
    except VehicleRegistration.DoesNotExist:
        vehicle = None
    return render(request, 'rc_book.html', {'vehicle': vehicle})


def rto_rc_book(request,column_id):
    try:
        vehicle = VehicleRegistration.objects.get(id=column_id)
    except VehicleRegistration.DoesNotExist:
        vehicle = None
    return render(request,"rc_book_template.html",{'vehicle': vehicle})



from django.shortcuts import render

def generate_rc_book(request, column_id):
    try:
        vehicle = VehicleRegistration.objects.get(id=column_id)
    except VehicleRegistration.DoesNotExist:
        vehicle = None
    return render(request, 'rc_another_page.html', {'vehicle': vehicle})



import random
import string

def generate_rto_number():
	random_number = random.randint(1000000, 9999999)
	dl_number = f"DL-14201100{random_number}"
	return dl_number

def rto_dl_application(request):
	database_data = dl.objects.all()
	return render(request,"rto_dl_application.html",{'database_data': database_data})
def accept(request, column_id):
    try:
        # Retrieve the database entry based on the provided column_id
        database_data_1 = appoinment_data.objects.get(id=column_id)
        database_data = dl.objects.get(id=column_id)
        
        # Generate a random RTO number
        rto_number = generate_rto_number()
        
        # Update the database entry with the generated RTO number
        database_data.rto_number = rto_number
        database_data.save(update_fields=['rto_number'])

        # Pass the updated database entry to the template
        return render(request, "accept.html", {'database_data': database_data,'database_data_1': database_data_1, 'rto_number': rto_number})
    except dl.DoesNotExist:
        database_data = None
        return render(request, "accept.html", {'database_data': database_data})

def dl_print(request,column_id):
	try:
		data = dl.objects.get(id=column_id)
	except dl.DoesNotExist:
		data = None
	return render(request, "dl_print.html", {'data': data})


def rto_chart(request):
	return render(request,"rto_chart.html",{})


def rto_users(request):
	database_data = registration.objects.all()
	return render(request,"rto_users.html",{'database_data': database_data})


def rto_inquiry(request):
	database_data = conta.objects.all()
	return render(request,"rto_inquiry.html",{'database_data': database_data})

def rto_sigup(request):
	if request.method=='POST':
		city=request.POST.get('city')
		r_office=request.POST.get('r_office')
		pass1=request.POST.get('password')
		pass2=request.POST.get('cpassword')
		if office.objects.filter(r_office=r_office, password=pass1).exists():
			messages.warning(request,'office is already exists!')
			return redirect(Rto_Sigup)
		elif pass1!=pass2:
			messages.warning(request,'password and confirm password does not match !')
			return redirect(Rto_Sigup)
		else:
			dbs = office(city=city, r_office=r_office, password=pass1, cpassword=pass2)
			dbs.save()
			return render(request,"rto_signin.html",{})
	return render(request,"rto_sigup.html",{})

def rto_signin(request):
    if request.method=='POST':
        r_office=request.POST.get('r_office')
        pass1=request.POST.get('password')
        if office.objects.filter(r_office=r_office,password=pass1).exists():
        	messages.warning(request,'You are Verified Person')
        	return redirect(home)
        else:
        	messages.warning(request,'You are Not Verified Person')
    return render(request,"rto_signin.html",{})



def LogoutPage(request):
    logout(request)
    return redirect('../rto_office/')
