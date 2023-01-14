from django.urls import path
from .views import InventView, MeetingView, DrawView

urlpatterns = [
    path('invent', InventView.as_view(), name='YesMyWine Ivent'),
    path('meeting', MeetingView.as_view(), name='Annual Meeting'),
    path('lucky-draw.html', DrawView.as_view(), name='Lucky Draw'),
]