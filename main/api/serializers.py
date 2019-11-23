from rest_framework import serializers
from . import models

class GroupModelSerializer(serializers.ModelSerializer):
    """ Группы """
    class Meta:
        model = models.Groups
        fields = ('id', 
                  'name')

class ScheduleSerializer(serializers.ModelSerializer):
    """ Расписание группы """

    class ScheduleRead(serializers.ModelSerializer):
        class Meta:
            model = models.Schedules
            fields = '__all__'
            depth = 10