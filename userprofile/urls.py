from django.urls import path,include
from userprofile.views import UserLoginView, UserProfileUpdateView, UserProfileView, UserRegisterView

urlpatterns = [
    
    path('', include('django.contrib.auth.urls')),
    path('signup/', UserRegisterView.as_view(), name='signup'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('profile/', UserProfileView.as_view(), name="profile"),
    path('profile/update/<int:pk>/', UserProfileUpdateView.as_view(), name="profile_update"),
    
]