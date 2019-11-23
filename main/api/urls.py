from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    
    #######
    # GET
    ####
    # Прочтение групп
    path('schedule/groups/', views.GroupListAPIView.as_view()),
    # Прочтение расписаний группы
    path('schedule/groups/<int:group_id>/', views.ScheduleGroupListAPIView.as_view()),
]