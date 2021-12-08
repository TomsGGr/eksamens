from django.contrib import admin
from .models import StudentModel


class UserAdmin(admin.ModelAdmin):
    pass

admin.site.register(StudentModel, UserAdmin)
