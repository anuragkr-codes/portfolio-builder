from django.shortcuts import render, redirect, get_object_or_404
from django.forms import modelformset_factory, inlineformset_factory
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Template, Portfolio, Project, Skill, Experience, Education

def home(request):
    templates = Template.objects.all()
    portfolios = Portfolio.objects.all().order_by('-created_at')[:5]  # Get the 5 most recent portfolios
    return render(request, 'generator/home.html', {
        'templates': templates,
        'portfolios': portfolios
    })

def select_template(request, template_id):
    template = get_object_or_404(Template, id=template_id)
    return render(request, 'generator/select_template.html', {'template': template})

def create_portfolio(request, template_id):
    template = get_object_or_404(Template, id=template_id)
    
    if request.method == 'POST':
        # Create portfolio
        portfolio = Portfolio(
            template=template,
            name=request.POST.get('name'),
            title=request.POST.get('title'),
            summary=request.POST.get('summary'),
            email=request.POST.get('email'),
            phone=request.POST.get('phone'),
            location=request.POST.get('location'),
            social_github=request.POST.get('social_github'),
            social_linkedin=request.POST.get('social_linkedin'),
            social_twitter=request.POST.get('social_twitter'),
        )
        portfolio.save()
        
        # Create projects
        project_titles = request.POST.getlist('project_title')
        project_descriptions = request.POST.getlist('project_description')
        project_urls = request.POST.getlist('project_url')
        project_github_urls = request.POST.getlist('project_github_url')
        
        for i in range(len(project_titles)):
            if project_titles[i]:  # Only create if title is provided
                Project.objects.create(
                    portfolio=portfolio,
                    title=project_titles[i],
                    description=project_descriptions[i] if i < len(project_descriptions) else '',
                    url=project_urls[i] if i < len(project_urls) else None,
                    github_url=project_github_urls[i] if i < len(project_github_urls) else None,
                    order=i,
                )
        
        # Create skills
        skill_names = request.POST.getlist('skill_name')
        skill_categories = request.POST.getlist('skill_category')
        skill_proficiencies = request.POST.getlist('skill_proficiency')
        
        for i in range(len(skill_names)):
            if skill_names[i]:  # Only create if name is provided
                Skill.objects.create(
                    portfolio=portfolio,
                    name=skill_names[i],
                    category=skill_categories[i] if i < len(skill_categories) else 'other',
                    proficiency=int(skill_proficiencies[i]) if i < len(skill_proficiencies) and skill_proficiencies[i].isdigit() else 50,
                )
        
        # Create experiences
        exp_titles = request.POST.getlist('exp_title')
        exp_companies = request.POST.getlist('exp_company')
        exp_locations = request.POST.getlist('exp_location')
        exp_start_dates = request.POST.getlist('exp_start_date')
        exp_end_dates = request.POST.getlist('exp_end_date')
        exp_currents = request.POST.getlist('exp_current')
        exp_descriptions = request.POST.getlist('exp_description')
        
        for i in range(len(exp_titles)):
            if exp_titles[i] and exp_companies[i] and exp_start_dates[i]:
                is_current = 'exp_current_' + str(i) in request.POST
                
                Experience.objects.create(
                    portfolio=portfolio,
                    title=exp_titles[i],
                    company=exp_companies[i],
                    location=exp_locations[i] if i < len(exp_locations) else None,
                    start_date=exp_start_dates[i],
                    end_date=None if is_current else (exp_end_dates[i] if i < len(exp_end_dates) and exp_end_dates[i] else None),
                    current=is_current,
                    description=exp_descriptions[i] if i < len(exp_descriptions) else '',
                )
        
        # Create education
        edu_institutions = request.POST.getlist('edu_institution')
        edu_degrees = request.POST.getlist('edu_degree')
        edu_fields = request.POST.getlist('edu_field')
        edu_start_dates = request.POST.getlist('edu_start_date')
        edu_end_dates = request.POST.getlist('edu_end_date')
        edu_currents = request.POST.getlist('edu_current')
        edu_descriptions = request.POST.getlist('edu_description')
        
        for i in range(len(edu_institutions)):
            if edu_institutions[i] and edu_degrees[i] and edu_start_dates[i]:
                is_current = 'edu_current_' + str(i) in request.POST
                
                Education.objects.create(
                    portfolio=portfolio,
                    institution=edu_institutions[i],
                    degree=edu_degrees[i],
                    field_of_study=edu_fields[i] if i < len(edu_fields) else None,
                    start_date=edu_start_dates[i],
                    end_date=None if is_current else (edu_end_dates[i] if i < len(edu_end_dates) and edu_end_dates[i] else None),
                    current=is_current,
                    description=edu_descriptions[i] if i < len(edu_descriptions) else None,
                )
        
        messages.success(request, 'Your portfolio has been created successfully!')
        return redirect('generator:view_portfolio', unique_id=portfolio.unique_id)
    
    return render(request, 'generator/create_portfolio.html', {'template': template})

def view_portfolio(request, unique_id):
    portfolio = get_object_or_404(Portfolio, unique_id=unique_id)
    projects = portfolio.projects.all()
    skills = portfolio.skills.all()
    experiences = portfolio.experiences.all()
    education = portfolio.education.all()
    
    # Determine which template to use based on the portfolio's template
    template_name = f"templates/template_{portfolio.template.id}.html"
    
    return render(request, template_name, {
        'portfolio': portfolio,
        'projects': projects,
        'skills': skills,
        'experiences': experiences,
        'education': education,
    })
