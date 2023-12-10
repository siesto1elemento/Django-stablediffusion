# urls.py
from django.urls import path
from .views import run_replicate_model

urlpatterns = [
    # Your other URL patterns go here
    path('', run_replicate_model, name='run_replicate_model'),
]
