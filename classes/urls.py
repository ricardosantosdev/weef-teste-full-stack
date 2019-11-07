from .views import listening_classes, adding_classes, editing_classes, deleting_classes
from django.urls import path

urlpatterns = [
    path('', listening_classes, name='classes'),
    path('nova-turma/', adding_classes, name='adding'),
    path('turma/<int:id>', editing_classes, name='editing'),
    path('excluir/<int:id>', deleting_classes, name='deleting'),
]