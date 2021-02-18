from django.urls import path
from .views import HomePageView, AboutPageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'), # when adding class-based views always add .as_view() at the end of view name
    path('about/', AboutPageView.as_view(), name='about'),
]