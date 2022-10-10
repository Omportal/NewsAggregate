from django.urls import path
from .views import NewsView, HabrView, ItprogerView, TprogerView

urlpatterns = [
    path('', NewsView.as_view(), name='news'),
    path('habr', HabrView.as_view(), name='habr'),
    path('itproger', ItprogerView.as_view(), name='it_proger'),
    path('tporger', TprogerView.as_view(), name='tproger')
]
