from django.contrib import admin
from .models import Subject, pastPaper, Slide, Video, Announcement

# Register your models here.
class subjectAdmin(admin.ModelAdmin):
    list_display = ['subject_name']

class pastPapersAdmin(admin.ModelAdmin):
    list_display = ['subject','_file']

class SlideAdmin(admin.ModelAdmin):
    list_display = ['subject','_file']




admin.site.register(Subject, subjectAdmin)
admin.site.register(pastPaper, pastPapersAdmin)
admin.site.register(Slide, SlideAdmin)
admin.site.register(Video)
admin.site.register(Announcement)