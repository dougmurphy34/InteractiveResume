from django.contrib import admin
from resume.models import Job, Skill, SkillType, JobSkillJunction, Accomplishment


#This could all be done with decorators on the models page, see:
#https://docs.djangoproject.com/en/1.7/ref/contrib/admin/

class AccomplishmentsInline(admin.StackedInline):
    model = Accomplishment
    extra = 3

class JobAdmin(admin.ModelAdmin):
    # end_date isn't bold in the admin view because it's not required - it can be null
    fieldsets = [
        ('Names', {'fields': ['company_name', 'company_short_name', 'job_title']}),
        ('Images', {'fields': ['company_logo', 'splash_image', 'splash_image_caption']}),
        ('Dates', {'fields': ['start_date', 'end_date']}),  #, 'classes': ['collapse']
        ('Description', {'fields': ['job_description'], 'classes': ['wide']})

    ]

    inlines = [AccomplishmentsInline]
    list_display = ('company_name', 'start_date', 'end_date')


class SkillTypeAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['skill_name']})
    ]


class SkillAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['skill_name']})
    ]

admin.site.register(Job, JobAdmin)
admin.site.register(Skill)
admin.site.register(SkillType)
admin.site.register(JobSkillJunction)