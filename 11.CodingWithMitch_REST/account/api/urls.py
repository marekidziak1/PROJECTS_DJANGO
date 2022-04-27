from django.urls import path
from account.api.views import (registration_view, 
                               account_update_view, 
                               account_properties_view, 
                               account_delete_view, 
                               ObtainAuthTokenView, 
                               does_account_exist_view, 
                               ChangePasswordView)

from rest_framework.authtoken.views import obtain_auth_token

app_name = "account"

urlpatterns = [
    path('my_obtain', obtain_auth_token, name = 'my_obtain'),#login
    path('login', ObtainAuthTokenView.as_view(), name = 'login'),#login
    path('register', registration_view, name = 'register'),
    path('properties', account_properties_view, name = 'properties'),
    path('properties/update', account_update_view, name = 'update'),
    path('properties/delete', account_delete_view, name = 'delete'),

]

# przy tworzeniu usera (konta Account) wskazanego w zmeinnej settings.AUTH_USER_MODEL (w settings)
# jest wysyłany sygnał do utworzenia obiektu klasy Token z rest_framework authtoken.models

# importujesz funkcje obtain_auth_token z rest_framework.authtoken.views  
# dla ścieżki 'my_obtain' i żądania 'POST' zostaje wywołana ta funkcja: obtain_auth_token która pobiera z requesta 2 parametry:
# 'username' i 'password' (mimo tego że w models.py dla klasy dziedziczącej po AbstractBaseUser w zmiennej USERNAME_FIELD podałeś 'email'
# to przy metodzie obtain_auth_token musisz podać w parametrach nazwę 'username' (zamiast 'email'). Dla poprawnych parametrów jest
# zwracany z tabeli Token: auth_token danego użytkownika