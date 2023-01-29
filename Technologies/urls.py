from django.urls import path
from . import views

urlpatterns = [
    path("technology/", views.TechnologyListCreateView.as_view()),
    path("technology/<technology_id>/", views.TechnologyUpdateView.as_view()),
]
