from django.contrib import admin
from .models import ParseData

# Register your models here.


@admin.register(ParseData)
class ParseDataAdmin(admin.ModelAdmin):
    pass
