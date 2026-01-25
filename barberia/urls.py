from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('usuarios.urls')),
    path('citas/', include('citas.urls')),

    path('logout/', LogoutView.as_view(), name='logout'),
]
