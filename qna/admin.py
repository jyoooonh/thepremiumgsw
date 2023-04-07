from django.contrib import admin
from .models import Teacher, Time_Table, Reserve

class ReserveAdmin(admin.ModelAdmin):
    list_display = ('date', 'time', 'teacher_id', 'student_name', 'comment_subject', "comment_content")
    search_fields = ["teacher_id__name", "student_name__username", "date"]

admin.site.register(Reserve, ReserveAdmin)
admin.site.register(Teacher)
admin.site.register(Time_Table)