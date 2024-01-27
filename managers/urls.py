from django.urls import path
from .views import *

urlpatterns = [

    path('manager/register/',ManagerRegisterView.as_view()),
    path('manager/delete/<int:id>', DeleteManagerView.as_view()),
    path('managers', AllManagersView.as_view()),
    path('manager/update/<int:id>', UpdateManagerView.as_view()),
]