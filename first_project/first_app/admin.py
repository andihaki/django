from django.contrib import admin
from first_app.models import AccessRecord, Topic, Webpage
from first_app.models import UserProfileInfo
from first_app.models import School, Student

# Register your models here.
admin.site.register(AccessRecord)
admin.site.register(Topic)
admin.site.register(Webpage)

# Register your models here.
# admin.site.register(User)
admin.site.register(UserProfileInfo)

# class base view
admin.site.register(School)
admin.site.register(Student)