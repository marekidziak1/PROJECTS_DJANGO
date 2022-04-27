from django.urls import path
from .views import loginPage, logoutPage, home

urlpatterns = [   
    path('', home, name='home'),
    path('login/', loginPage,name="login"),
    path('logout/', logoutPage, name='logout' ),

]