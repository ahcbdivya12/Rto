from django.urls import path
from service import views as rto_office

urlpatterns = [
    
    path('home',rto_office.rto_index ),
     path('Vehical_Info',rto_office.rto_vehical_reg ),
    path('display_vehical_info/<int:column_id>/',rto_office.display_vehical_info ),
    path('generate_rc_book/<int:column_id>/',rto_office.generate_rc_book ),

    path('rto_rc_book/<int:column_id>/',rto_office.rto_rc_book ),

    path('rto_show_vehicalinfo',rto_office.rto_show_vehicalinfo ),
    path('Rto_Appoinment',rto_office.rto_appoinment ),
    path('Rto_DL_Verification',rto_office.rto_dl_verification ),

    path('Rto_DL_Application',rto_office.rto_dl_application ),
    path('Rto_Chart',rto_office.rto_chart ),
    
    path('Rto_Users',rto_office.rto_users ),
    path('',rto_office.rto_signin ),
    path('Rto_Sigup',rto_office.rto_sigup ),
    path('Rto_Inquiry',rto_office.rto_inquiry ), 

 path('accept/<int:column_id>/',rto_office.accept),
    path('Rto_dl/<int:column_id>/', rto_office.dl_print),
    
    path('logout',rto_office.LogoutPage),

]