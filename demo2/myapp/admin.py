from django.contrib import admin

# Register your models here.
from .models import DemoModel,Articles

admin.site.register(DemoModel)
admin.site.register(Articles)

