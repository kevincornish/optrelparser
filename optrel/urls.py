from django.contrib import admin
from django.urls import path
from reports.views import VialListView, AmpouleListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('vials/', VialListView.as_view()),
    path('ampoules/', AmpouleListView.as_view())
]
