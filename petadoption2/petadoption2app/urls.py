from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Home view
    path('volunteer/', views.volunteer, name='volunteer'),
    path('donate/', views.donate, name='donate'),
    path('foster/', views.foster, name='foster'),
    path('success_stories/', views.success_stories, name='success_stories'),
    path('contact/', views.contact, name='contact'),
    path('adoption_records/', views.adoption_records, name='adoption_records'),
    path('adoption_process/', views.adoption_process, name='adoption_process'),
    path('about_us/', views.about_us, name='about_us'),
    path('resources/', views.resources, name='resources'),
    path('blog_news/', views.blog_news, name='blog_news'),
    path('user_account/', views.user_account, name='user_account'),
    path('privacy_security/', views.privacy_security, name='privacy_security'),
    path('available_pets/', views.available_pets, name='available_pets'),
    path('adoption_application/', views.adoption_application, name='adoption_application'),
]

