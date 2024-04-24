from django.db import models

class dl(models.Model):
	rto_state=models.CharField(max_length=40)
	rto_office=models.CharField(max_length=200)
	rto_pincode=models.IntegerField() 

	name=models.CharField(max_length=70)
	father_name=models.CharField(max_length=70)
	mother_name=models.CharField(max_length=70)
	adhar_card_no=models.IntegerField() 
	date=models.DateField()
	birth_p=models.CharField(max_length=70)

	email=models.CharField(max_length=70)
	mobile=models.BigIntegerField()
	otp=models.BigIntegerField(null=True)
	
	gender=models.CharField(max_length=70)
	relation=models.CharField(max_length=70)
	age=models.IntegerField() 
	qulification=models.CharField(max_length=70)
	b_group=models.CharField(max_length=70)
	a_mobile=models.BigIntegerField()
	occupation=models.CharField(max_length=70)
	country=models.CharField(max_length=70)
	state=models.CharField(max_length=70)
	city=models.CharField(max_length=70)
	address=models.CharField(max_length=80)
	pincode=models.IntegerField() 
	issues_state=models.CharField(max_length=70)
	issue_date=models.DateField()
	expire_date=models.DateField()
	disablity_yn=models.CharField(max_length=70)
	disablit=models.CharField(max_length=70)
	doner=models.CharField(max_length=70)
	all_yes=models.CharField(max_length=70)
	photo=models.FileField()
	sign=models.FileField()
	document=models.CharField(max_length=70)
	proof=models.CharField(max_length=70)
	doc_no=models.BigIntegerField()
	issue_date_doc=models.DateField()
	issues_by=models.CharField(max_length=70)
	doc_1=models.FileField()
	document_2=models.CharField(max_length=70)
	proof_2=models.CharField(max_length=70)
	doc_no_2=models.BigIntegerField()
	issue_date_2=models.DateField()
	issues_by_2=models.CharField(max_length=70)
	doc_2=models.FileField()

	document_3=models.CharField(max_length=70,null=True)
	proof_3=models.CharField(max_length=70,null=True)
	doc_no_3=models.BigIntegerField(null=True)
	issue_date_3=models.DateField(null=True)
	issues_by_3=models.CharField(max_length=70,null=True)
	doc_3=models.FileField(null=True)

	rto_number = models.CharField(max_length=20, blank=True, null=True)  
# Create your models here.

# Create your models here.
class registration(models.Model):
	name=models.CharField(max_length=40)
	email=models.CharField(max_length=40)
	password=models.CharField(max_length=40)
	cpassword=models.CharField(max_length=40)
	address=models.CharField(max_length=40)
	mobile=models.BigIntegerField()
	gender=models.CharField(max_length=40)
	state=models.CharField(max_length=40)

class otp(models.Model):
	otp=models.BigIntegerField()


class appoinment_data(models.Model):
	date=models.DateField()
	time=models.CharField(max_length=40)

class office(models.Model):
	city=models.CharField(max_length=40)
	r_office=models.CharField(max_length=400)
	password=models.CharField(max_length=40)
	cpassword=models.CharField(max_length=40)

class conta(models.Model):
	name=models.CharField(max_length=40)
	email=models.CharField(max_length=40)
	subject=models.CharField(max_length=40)
	message=models.CharField(max_length=400)

from django.db import models

class RenewalHistory(models.Model):
    rto_state = models.CharField(max_length=100)
    rto_office = models.CharField(max_length=100)
    rto_pincode = models.CharField(max_length=10)
    mobile = models.CharField(max_length=20)
    # Add other fields from your dl model here
    issues_state=models.CharField(max_length=70,null=True)
    issue_date=models.DateField(null=True)
	
    expire_date = models.DateTimeField(null=True)
    photo=models.FileField(null=True)
    sign=models.FileField(null=True)
    document=models.CharField(max_length=70,null=True)
    proof=models.CharField(max_length=70,null=True)
    doc_no=models.BigIntegerField(null=True)
    issue_date_doc=models.DateField(null=True)
    issues_by=models.CharField(max_length=70,null=True)
    doc_1=models.FileField(null=True)
    document_2=models.CharField(max_length=70,null=True)
    proof_2=models.CharField(max_length=70,null=True)
    doc_no_2=models.BigIntegerField(null=True)
    issue_date_2=models.DateField(null=True)
    issues_by_2=models.CharField(max_length=70,null=True)
    doc_2=models.FileField(null=True)
    document_3=models.CharField(max_length=70,null=True)
    proof_3=models.CharField(max_length=70,null=True)
    doc_no_3=models.BigIntegerField(null=True)
    issue_date_3=models.DateField(null=True)
    issues_by_3=models.CharField(max_length=70,null=True)
    doc_3=models.FileField(null=True)


    def __str__(self):
        return self.mobile  # You can return any field you want to identify the object

    class Meta:
        verbose_name = 'Renewal History'
        verbose_name_plural = 'Renewal Histories'


# models.py

from django.db import models

class VehicleRegistration(models.Model):

    owner_name = models.CharField(max_length=100,null=True)
    owner_address = models.CharField(max_length=100,null=True)
    owner_address_temp = models.CharField(max_length=100,null=True)
    insurance = models.CharField(max_length=100,null=True)

    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    manufacture_year = models.IntegerField()
    vin = models.CharField(max_length=100)
    mileage = models.CharField(max_length=100)  # Assuming mileage can be a string
    engine = models.CharField(max_length=100)
    transmission = models.CharField(max_length=100)
    fuel = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    body_style = models.CharField(max_length=100)
    features = models.TextField()
    condition = models.TextField()
    ownership_history = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.CharField(max_length=100)
    
    state_code = models.CharField(max_length=100,null=True)
    city_code = models.CharField(max_length=100,null=True)

    registration_info = models.TextField()
    title_status = models.CharField(max_length=100)


from django.db import models

class DuplicateHistory(models.Model):
    applicant_name = models.CharField(max_length=100)
    applicant_address = models.TextField()
    contact_number = models.CharField(max_length=20)
    license_number = models.CharField(max_length=20)
    reason_for_duplicate = models.TextField()
    documents_submitted = models.FileField(upload_to='documents/')
    application_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, default='Pending')
    photo=models.FileField()
    sign=models.FileField()
    document=models.CharField(max_length=70)
    proof=models.CharField(max_length=70)
    doc_no=models.BigIntegerField()
    issue_date_doc=models.DateField()
    issues_by=models.CharField(max_length=70)
    doc_1=models.FileField()
    document_2=models.CharField(max_length=70)
    proof_2=models.CharField(max_length=70)
    doc_no_2=models.BigIntegerField()
    issue_date_2=models.DateField()
    issues_by_2=models.CharField(max_length=70)
    doc_2=models.FileField()
    document_3=models.CharField(max_length=70,null=True)
    proof_3=models.CharField(max_length=70,null=True)
    doc_no_3=models.BigIntegerField(null=True)
    issue_date_3=models.DateField(null=True)
    issues_by_3=models.CharField(max_length=70,null=True)
    doc_3=models.FileField(null=True)

    def __str__(self):
        return self.mobile  # You can return any field you want to identify the object

    class Meta:
        verbose_name = 'Duplicate History'
        verbose_name_plural = 'Duplicate Histories'


from django.db import models

class Payment(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=3)
    customer_name = models.CharField(max_length=100)
    customer_address = models.TextField()
    payment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Payment #{self.pk}"
