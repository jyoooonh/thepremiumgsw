from django.contrib import admin
from .models import Teacher, Reserve, Time_Table

admin.site.register(Reserve)
admin.site.register(Teacher)
admin.site.register(Time_Table)
# Register your models here.
