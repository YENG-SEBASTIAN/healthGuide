from django.urls import path

from healthGuide.views import (
    CustomUserCreateView, CustomUserDetailView, PatientListCreateView, PatientDetailView
)
urlpatterns = [
   path('users/', CustomUserCreateView.as_view(), name='user-create'),
   path('users/<int:pk>/', CustomUserDetailView.as_view(), name='user-detail'),
   path('patients/', PatientListCreateView.as_view(), name='patient-list'),
   path('patients/<int:pk>/', PatientDetailView.as_view(), name='patient-detail'),
]