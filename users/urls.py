from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.urls import path
from . import views
urlpatterns = [
path('register/', views.register_user, name='register'),
path('profile/', views.profile, name='profile'),
path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
 ]