from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.home, name='home'),
    path('person/', views.person_list, name='person_list'),
    path('person/<int:id>/', views.person_detail, name='person_detail'),
    path('person/new/', views.person_form, name='person_create'),
    path('person/<int:id>/edit/', views.person_form, name='person_update'),
    path('person/<int:id>/delete/', views.person_delete, name='person_delete'),
    path('referral/', views.referral_list, name='referral_list'),
    path('referral/<int:id>/', views.referral_detail, name='referral_detail'),
    path('referral/new/<int:person_id>', views.referral_form, name='referral_create'),
    path('referral/<int:person_id>/<int:id>/edit/', views.referral_form, name='referral_update'),
    path('referral/<int:id>/delete/', views.referral_delete, name='referral_delete'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
