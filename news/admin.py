from django.contrib import admin

# Register your models here.
from news.models import New , Category

admin.site.register(New)
admin.site.register(Category)