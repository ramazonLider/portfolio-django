from django.contrib import admin
from .models import Project, Category, Blog, Part
# Register your models here.
admin.site.register(Category)
admin.site.register(Project)
admin.site.register(Blog)
admin.site.register(Part)