from django.contrib import admin
from . import models

admin.site.register(models.Patient)
admin.site.register(models.History)
admin.site.register(models.Hospital)


# Register your models here.
