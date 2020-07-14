from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from django.conf.urls import include, url
from reports.views import VialListView, VialAuditListView, VialDetailView, AmpouleListView, AmpouleAuditListView, AmpouleDetailView, Dashboard
urlpatterns = [
    path('',Dashboard,name='dashboard',),
    path('accounts/', include("django.contrib.auth.urls")),
    path('admin/', admin.site.urls),
    path('vials/', VialListView.as_view(), name='vials'),
    path('vials/<int:pk>/', VialDetailView.as_view(), name='vial_detail'),    
    path('ampoules/', AmpouleListView.as_view(), name='ampoules'),
    path('ampoules/<int:pk>/', AmpouleDetailView.as_view(), name='ampoule_detail'),
    path('audit/vials/', VialAuditListView.as_view()),
    path('audit/ampoules/', AmpouleAuditListView.as_view()),
    path(
        'admin/password_reset/',
        auth_views.PasswordResetView.as_view(),
        name='admin_password_reset',
    ),
    path(
        'admin/password_reset/done/',
        auth_views.PasswordResetDoneView.as_view(),
        name='password_reset_done',
    ),
    path(
        'reset/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(),
        name='password_reset_confirm',
    ),
    path(
        'reset/done/',
        auth_views.PasswordResetCompleteView.as_view(),
        name='password_reset_complete',
    ),
]
