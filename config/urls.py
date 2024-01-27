
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
from drf_spectacular.views import SpectacularSwaggerView,SpectacularAPIView,SpectacularRedocView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('appartments.urls')),
    path('api/v1/', include('managers.urls')),

    path('refresh-token/',TokenRefreshView.as_view()),
    path('manager-login/',TokenObtainPairView.as_view()),

    path('api/', SpectacularAPIView.as_view(), name="schema"),
    path('swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger'),
    path('redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),  
]
