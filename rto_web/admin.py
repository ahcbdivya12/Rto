from django.contrib import admin

# Register your models here.
from .models import dl
# what ever class we made in models.py we have to import here by class name…
admin.site.register(dl) #

from .models import registration
admin.site.register(registration)


from .models import otp
admin.site.register(otp)

from .models import appoinment_data
admin.site.register(appoinment_data)


from .models import office
admin.site.register(office)

from .models import conta
admin.site.register(conta)


from .models import RenewalHistory
admin.site.register(RenewalHistory)


from .models import VehicleRegistration
admin.site.register(VehicleRegistration)

from .models import DuplicateHistory
admin.site.register(DuplicateHistory)
