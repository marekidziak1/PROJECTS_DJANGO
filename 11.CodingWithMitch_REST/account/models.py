
from django.db import models
from django.contrib.auth.models import (BaseUserManager, 
                                        AbstractBaseUser, 
                                        PermissionsMixin)
                


from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


@receiver(post_save, sender = settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class MyAccountManager(BaseUserManager):
    def create_user(self, email, username, password=None): #musisz wpisać pola z klasy dziedziczącej po AbstractBaseUser -> oprócz pola przypisanego do zmiennej USERNAME_FIELD (email) ORAZ password MUSISZ PRZYPISAĆ TU pola przypisane do listy REQUIRED_FIELDS
        if not email:
            raise ValueError('Users must have an email address')
        if not username:
            raise ValueError('Users must have username')
        user = self.model(
            email = self.normalize_email(email), #normalize_email() - funkcja odpowiedzialna za zmniejszenie liter w django
            username = username,
            #password = password,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password=None):
        user = self.create_user(
            email = self.normalize_email(email),
            password = password,
            username = username,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser, PermissionsMixin):       
    email = models.EmailField(verbose_name='email', max_length=60, unique=True)
    username = models.CharField(max_length=30, unique = True)
    avatar =  models.ImageField(null=True, blank=True, default='331050936_s.jpg')
    date_joined = models.DateTimeField(verbose_name='date joined' ,auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last_login', auto_now=True)
    is_active = models.BooleanField(default=True)   #wymagane pole - nie da się zalogować do panelu
    is_staff = models.BooleanField(default=False)   #wymagane pole - da się zalogowac do panelu ale nie można do niego zajrzeć (active musi być True)
    is_admin = models.BooleanField(default=False)   #wymagane pole - da się zalogować do panelu i da się zajrzeć do niego do środka (active i staff muszą być True)
    is_superuser = models.BooleanField(default=False)   #niewymagane - daje wszystkie uprawnienia (active, staff i admin muszą być True)

    objects = MyAccountManager()        
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['username',]#

    def __str__(self):
        return self.email
    # def has_perm(self, perm, obj=None):     #has permission to make changes in databases?
    #     return self.is_admin              
    # def has_module_perms(self, app_label):  #has module permission?
    #     return True


# żeby zadziałało trzeba 
#   #W SETTINGS.PY podać zmiennąAUTH_USER_MODEL wg klucza 'my_app.my_class': AUTH_USER_MODEL = 'account.Account'
#   *W klasie dziedziczącej po AbstractBaseUser:   
#               **albo zrobić dziedziczenie wielokrotne po 'PermissionsMixin' (tj oprócz AbstractBaseUser podać również 'PermissionsMixin') albo przesłonić metody has_perm i has_module_perms
#               **podać pola: is_active, is_staff, is_admin, is_superuser:
#                       *is_active - wymagane pole ale nic nie dające - nie da się zalogować do panelu
#                       *is_staff - wymagane pole, da się zalogowac do panelu ale nie można do niego zajrzeć (przy tym 'active' musi być True)
#                       *is_admin - wymagane pole, da się zalogować do panelu i da się zajrzeć do niego do środka (przy tym 'active' i 'staff' muszą być True)
#                       *is_superuser - niewymagane - daje wszystkie uprawnienia (przy tym 'active', 'staff' i 'admin' muszą być True)
#               **podać zmienne:    
#                       *objects = MyAccountManager() - klasa dziedzicząca po BaseUserManager musi byc pierwsza by móc przypisać do pola objects jej instancje
#                       *USERNAME_FIELD='email' - wskazuję na pole kóre będzie wykorzystywane do logowania
#                       *REQUIRED_FIELDS=['username',] - wksazuję na pola z klasy dziedziczącej po AbstractBaseUser które są wymagane przy tworzeniu usera i superusera ( są wymagane w argumentach tych funkcji)
#   *powyżej klasy dziedziczącej po AbstractBaseUser zaimplementować klasę dziedziczącą po BaseUserManager a w niej przesłonić metody create_user i  create_superuser
#   *zaimplementować w admin.py klasę dziedziczącą po UserAdmin i zarejestrowac ją bo bez tego nie bedziesz mógł się zalogować. Klasa dziedzicząca po UserAdmin musi mieć pola:
#                       **fields = ('email'... - domyślnie nie wyświetli się email pry tworzeniu usera dlatego trzeb go wskazać
#                       **list_display - gdzie wskazujesz wyświetlane pola dla listy
#                       **dodatkowe pola: fieldsets = () ;; filter_horizontal = () ;; list_filter = ()






# from django.db import models
# from django.contrib.auth.models import User
# class Account(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
#     def __str__(self):
#         return self.user.username 