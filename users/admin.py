from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Court)
admin.site.register(CourtFile)
admin.site.register(File)
admin.site.register(Expert)
admin.site.register(ExpertsStatement)
admin.site.register(AccessRequest)