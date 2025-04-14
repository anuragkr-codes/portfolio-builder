from django.contrib import admin
from .models import Template, Portfolio, Project, Skill, Experience, Education

@admin.register(Template)
class TemplateAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('name', 'title', 'template', 'created_at')
    readonly_fields = ('unique_id',)

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'portfolio', 'order')
    list_filter = ('portfolio',)

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'proficiency', 'portfolio')
    list_filter = ('category', 'portfolio')

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('title', 'company', 'start_date', 'end_date', 'current', 'portfolio')
    list_filter = ('portfolio', 'current')

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('institution', 'degree', 'start_date', 'end_date', 'current', 'portfolio')
    list_filter = ('portfolio', 'current')
