from django.contrib import admin
from .models import Consulting

class ConsultingAdmin(admin.ModelAdmin):
    list_display = ('date', 'teacher_name', 'student_name')
    search_fields = ["teacher_name", "student_name__username"]

admin.site.register(Consulting, ConsultingAdmin)

# Register your models here.
