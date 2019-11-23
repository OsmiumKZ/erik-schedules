from django.contrib import admin
from .models import *

admin.site.register(Subjects)       # Предметы
admin.site.register(Teachers)       # Преподаватели
admin.site.register(Times)          # Время
admin.site.register(Rooms)          # Аудитории
admin.site.register(Groups)         # Группы
admin.site.register(Items)          # Ячейки пар
admin.site.register(Days)           # Дни
admin.site.register(Schedules)      # Расписания
