from rest_framework import generics, permissions, response
from . import models
from . import serializers

class GroupListAPIView(generics.ListAPIView):
    """ Добавление и прочтение группы """
    queryset = models.Groups.objects.all()
    serializer_class = serializers.GroupModelSerializer
    permission_classes = (permissions.AllowAny,)

class ScheduleGroupListAPIView(generics.ListAPIView):
    """ Прочтение расписаня группы """
    serializer_class = serializers.ScheduleSerializer.ScheduleRead
    permission_classes = (permissions.AllowAny,)
    lookup_field = 'group_id'

    def get_queryset(self):
        group_id = self.kwargs['group_id']
        return models.Schedules.objects.filter(group__id=group_id)