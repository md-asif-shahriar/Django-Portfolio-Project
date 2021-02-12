from django.urls import path
from .views import *

urlpatterns = [
    path('', home_view, name='home'),
    path('contact', contact_view, name='contact'),

]