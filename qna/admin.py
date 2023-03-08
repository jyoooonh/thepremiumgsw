from django.contrib import admin
from .models import Teacher, Time_Table, Reserve

class ReserveAdmin(admin.ModelAdmin):
    list_display = ('date', 'teacher_id', 'time')

admin.site.register(Reserve, ReserveAdmin)
admin.site.register(Teacher)
admin.site.register(Time_Table)

