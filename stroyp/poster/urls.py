from django.urls import path#формирует маршруты
from django.views.decorators.cache import cache_page

from .views import *
# cache_page(60*10)
urlpatterns = [
    path('', (GoodsHome.as_view()), name='home'),
    path('test/',testfall),
    path('post/<slug:post_slug>/',ShowPost.as_view(),name='post')
    # path('', order_create, name='order_create'),
]