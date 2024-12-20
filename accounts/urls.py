from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('' , homepage , name='home'),
    path('register/', register, name='register'),
    path('verify/<str:token>/', verify_email, name='verify_email'),
    path("verify", email_sent, name="email_sent"),
    path('login/', user_login, name='login'), 
    path('logout/' , logout_view , name='logout'),
    path('contact/' , contact_page , name='contact'),
    path('profile/', view_profile , name='profile'),
    path('api/' , HumanCard_API.as_view() , name='api')
] 
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT)