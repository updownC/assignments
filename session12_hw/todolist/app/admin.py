from django.contrib import admin
from .models import Todo, Comment
# Register your models here.
admin.site.register(Todo)
admin.site.register(Comment)