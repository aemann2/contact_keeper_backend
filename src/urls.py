from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from contact_keeper import views

router = routers.DefaultRouter()
router.register(r'contacts', views.ContactView, 'contact')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]