from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import DetailView,ListView

from .models import *
from .forms import OrderCreateForm
from .utils import DataMixin


# def index(request):#здесь мы добавляем ссылку на наш html код,а потом мы можем этот def подключить в urls
#     work = Work.objects.all()
#     if request.method == 'POST':
#         form = OrderCreateForm(request.POST)
#         if form.is_valid():
#             feed = Order(
#                 first_name = form.cleaned_data['first_name'],
#                 phoneNumber = form.cleaned_data['phoneNumber'],
#             )
#             order = feed.save()
#             return render(request, 'poster/created.html',
#                           {'order': order})
#     return render(request, 'poster/index.html',{'work':work})

class GoodsHome(DataMixin,ListView):
    model = Work
    template_name = 'poster/index.html'
    context_object_name = 'work'
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Главная страница')
        return dict(list(context.items())+list(c_def.items()))


class ShowPost(DataMixin,DetailView):
    model = Work
    template_name = 'poster/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self,object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=context['post'])
        return dict(list(context.items())+list(c_def.items()))



def testfall(request):
    return render(request,'poster/created.html')