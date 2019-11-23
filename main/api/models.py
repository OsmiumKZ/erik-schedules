from django.db import models

class Subjects(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')

    class Meta:
        verbose_name = 'Предмет'
        verbose_name_plural = 'Предметы'

    def __str__(self):
        return f'{self.name}'

class Teachers(models.Model):
    name = models.CharField(max_length=255, verbose_name='ФИО')

    class Meta:
        verbose_name = 'Преподаватель'
        verbose_name_plural = 'Преподаватели'

    def __str__(self):
        return f'{self.name}'

class Times(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')

    class Meta:
        verbose_name = 'Время'
        verbose_name_plural = 'Время'

    def __str__(self):
        return f'{self.name}'

class Rooms(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')

    class Meta:
        verbose_name = 'Аудитория'
        verbose_name_plural = 'Аудитории'

    def __str__(self):
        return f'{self.name}'

class Groups(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')

    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'

    def __str__(self):
        return f'{self.name}'

class Items(models.Model):
    subject = models.ForeignKey(Subjects,
                                on_delete=models.CASCADE,
                                related_name='subject',
                                verbose_name='Предмет')
    teacher = models.ForeignKey(Teachers,
                                on_delete=models.CASCADE,
                                related_name='teacher',
                                verbose_name='Преподаватель')
    room = models.ForeignKey(Rooms,
                             on_delete=models.CASCADE,
                             related_name='room',
                             verbose_name='Аудитория')
    time = models.ForeignKey(Times,
                             on_delete=models.CASCADE,
                             related_name='time',
                             verbose_name='Время')

    class Meta:
        verbose_name = 'Ячейка пары'
        verbose_name_plural = 'Ячейки пар'
        
    def __str__(self):
        return f'Предмет: {self.subject.name}, Преподаватель: {self.teacher.name}, Аудитория: {self.room.name}, Время: {self.time.name} '

class Days(models.Model):
    item_one = models.ForeignKey(Items,
                                 on_delete=models.CASCADE,
                                 related_name='item_one',
                                 verbose_name='Первая пара')
    item_two = models.ForeignKey(Items,
                                 on_delete=models.CASCADE,
                                 related_name='item_two',
                                 verbose_name='Вторая пара')
    item_three = models.ForeignKey(Items,
                                   on_delete=models.CASCADE,
                                   related_name='item_three',
                                   verbose_name='Третья пара')
    item_four = models.ForeignKey(Items,
                                  on_delete=models.CASCADE,
                                  related_name='item_four',
                                  verbose_name='Четвертая пара')
    item_five = models.ForeignKey(Items,
                                 on_delete=models.CASCADE,
                                 related_name='item_five',
                                 verbose_name='Пятая пара')
    item_six = models.ForeignKey(Items,
                                 on_delete=models.CASCADE,
                                 related_name='item_six',
                                 verbose_name='Шестая пара')
    item_seven = models.ForeignKey(Items,
                                   on_delete=models.CASCADE,
                                   related_name='item_seven',
                                   verbose_name='Седьмая пара')
    item_eight = models.ForeignKey(Items,
                                   on_delete=models.CASCADE,
                                   related_name='item_eight',
                                   verbose_name='Восьмая пара')

    class Meta:
        verbose_name = 'День'
        verbose_name_plural = 'Дни'

    def __str__(self):
        return f'День ID: {self.id}'

class Schedules(models.Model):
    group = models.ForeignKey(Groups,
                              on_delete=models.CASCADE,
                              related_name='group',
                              verbose_name='Группа')
    day_one = models.ForeignKey(Days,
                                on_delete=models.CASCADE,
                                related_name='day_one',
                                verbose_name='Понедельник')
    day_two = models.ForeignKey(Days,
                                on_delete=models.CASCADE,
                                related_name='day_two',
                                verbose_name='Вторник')
    day_three = models.ForeignKey(Days,
                                  on_delete=models.CASCADE,
                                  related_name='day_three',
                                  verbose_name='Среда')
    day_four = models.ForeignKey(Days,
                                 on_delete=models.CASCADE,
                                 related_name='day_four',
                                 verbose_name='Четверг')
    day_five = models.ForeignKey(Days,
                                 on_delete=models.CASCADE,
                                 related_name='day_five',
                                 verbose_name='Пятница')

    class Meta:
        verbose_name = 'Расписание'
        verbose_name_plural = 'Расписания'

    def __str__(self):
        return f'Расписание: {self.id}, Группы: {self.group.name}'