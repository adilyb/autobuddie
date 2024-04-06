from django.urls import path
from general.views import HomeView, ContactusView, FrontPageView, searchBar

urlpatterns = [
    # path('', FrontPageView.as_view(), name='front_page'),
    path('', HomeView.as_view(), name='home'),
    path('contactus/', ContactusView.as_view(), name='contactus'),
    path('search/',searchBar,name='search'),
    
]
