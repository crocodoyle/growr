from django.contrib import admin

from track.models import Kid, Measurement


class KidAdmin(admin.ModelAdmin):
    fields = ['first_name', 'last_name', 'born', 'male']

class MeasurementAdmin(admin.ModelAdmin):
    fields = ['weight', 'height', 'taken', 'child']

admin.site.register(Kid, KidAdmin)
admin.site.register(Measurement, MeasurementAdmin)
