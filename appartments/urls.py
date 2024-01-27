from django.urls import path
from .views import *

urlpatterns = [
    
    path('appartments/',AllAppartmentsView.as_view()),
    path('appartments/<int:id>',DetailAppartmentView.as_view()),
    path('appartment/create/', CreateApprtmentView.as_view()),
    path('appartment/delete/<int:id>', DeleteAppartmentView.as_view()),
    path('appartment/update/<int:id>',UpdateAppartmentView.as_view()),
    
]