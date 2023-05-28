from .models import *


class DataMixin:
    def get_user_context(self,**kwargs):#создает контекст для шаблона(убирает дублирование кода)
        context = kwargs#создаем первоначальный список
        work = Work.objects.all()
        context['work'] = work
        return context