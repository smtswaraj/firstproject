from django.contrib import admin
from .models import Desc
class BookAdmin(admin.ModelAdmin):
    # readonly_fields = ('day',)
    # prepopulated_fields = {'day':('review',)}
    pass

# Register your models here.
admin.site.register(Desc,BookAdmin)
