from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model

from .models import Student, Book, Hobby

User = get_user_model()

admin.site.register(User)
admin.site.unregister(Group)
admin.site.register(Student)
admin.site.register(Book)
admin.site.register(Hobby)
