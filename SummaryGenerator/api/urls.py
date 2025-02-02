from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('generate-summary/', views.generate_summary, name='generate-summary'),
    path('generate-bullet-points/', views.generate_bullet_points, name='generate-bullet-points'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

