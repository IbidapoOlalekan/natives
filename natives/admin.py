from django.contrib import admin

# Register your models here.
from natives.models import Natives, Cohort

admin.site.register(Natives)
admin.site.register(Cohort)
