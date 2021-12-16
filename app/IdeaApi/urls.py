from django.urls import path
from . import views

urlpatterns = [
    path('op1/', views.Group1.as_view(), name="api-overview"),
    path('op2/<int:pk>', views.Group2.as_view(), name="api-overview"),
]