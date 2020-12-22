from django.urls import path
from .views import FileView, ColumnView, MeanView
from django.views.static import serve

urlpatterns = [
    path('upload/',FileView.as_view(), name='upload'),
    path('roundoff/',ColumnView.as_view(), name='roundoff'),
    path('mean/',MeanView.as_view(), name='mean'),
]