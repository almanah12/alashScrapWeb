from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView

from .views import *

urlpatterns = [
    # path('', scrap_run, name='scrap_run_url'),
    path('table/', scrap_table, name='scrap_table_url'),
    path('settings/', scrap_settings, name='scrap_settings_url'),

]