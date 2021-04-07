from django.contrib import admin
from . import models
from django.contrib.auth.models import User

# Register your models here.
class AdminPage(admin.AdminSite) :
    site_header = 'Jerrry'
    site_title = 'SWAGBOI'
    index_title = 'SWAGBOI3'
    login_template = 'Patient_Management/admin_login.html'

admin_area = AdminPage(name ='COVID Patient Management Admin')

admin_area.register(models.Patient_Data)
admin_area.register(User)


