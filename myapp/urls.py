from django.urls import path
from . import views

urlpatterns = [
    path('add-Viewer/', views.addViewer.as_view(), name='add-Viewer'),
    path('get-Viewer/',views.getViewer.as_view(), name='get-Viewer'),
    path('get-Data/',views.getData.as_view(), name='get-Data'),
    path('update-Data/<int:id>/',views.updateData.as_view(), name='update-Data'),
    path('delete-Data/<int:id>/',views.deleteData.as_view(), name='delete-Data'),
]