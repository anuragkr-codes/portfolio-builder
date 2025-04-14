from django.urls import path
from . import views

app_name = 'generator'

urlpatterns = [
    path('', views.home, name='home'),
    path('select-template/<int:template_id>/', views.select_template, name='select_template'),
    path('create-portfolio/<int:template_id>/', views.create_portfolio, name='create_portfolio'),
    path('portfolio/<uuid:unique_id>/', views.view_portfolio, name='view_portfolio'),
]