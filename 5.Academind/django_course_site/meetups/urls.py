from django.urls import path
from . import views as meetups_views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('', meetups_views.index, name='all-meetups'),
    path('<slug:meetup_slug>/', meetups_views.meetup_details, name='meetup-detail'),
    path('<slug:meetup_slug>/success', meetups_views.confirm_registration, name="confirm_registration"),
] #+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)