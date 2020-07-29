from django.contrib import admin
from .models import Project, Category


class ProjectAdmin(admin.ModelAdmin):
    readonly_fields = ('created_date', 'user_profile')
    list_display = (
        'title',
        'image',
        'category',
        'created_date',
        'views',
        'goal',
        'end_date',
        'num_days',
        'raised',
    )

    ordering = ('-created_date',)



admin.site.register(Project, ProjectAdmin)
admin.site.register(Category)

