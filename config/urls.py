
from django.contrib import admin
from django.urls import path, include
from managers.views import ManagerRegisterView
from appartments.views import *
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
from drf_spectacular.views import SpectacularSwaggerView,SpectacularAPIView,SpectacularRedocView

urlpatterns = [
    path('admin/', admin.site.urls),

    path('manager/register/',ManagerRegisterView.as_view()),
    path('manager-login/',TokenObtainPairView.as_view()),
    path('refresh-token/',TokenRefreshView.as_view()),

    path('appartments/',AllAppartmentsView.as_view()),
    path('appartments/<int:id>',DeleteAppartmentView.as_view()),
    path('appartment/create/', CreateApprtmentView.as_view()),
    path('appartment/delete/', DeleteAppartmentView.as_view()),

    path('city', CityView.as_view()),
    path('client',ClientView.as_view()),

    path('api/', SpectacularAPIView.as_view(), name="schema"),
    path('swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger'),
    path('redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),  
]
