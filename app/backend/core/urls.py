
from django.urls import path, include

from backend.core.views import KnightMovesViewSet


knight_urls = [
    path('moves/', KnightMovesViewSet.as_view(
        {'post': 'get_moves_tree'}), name='possible-moves')
]

urlpatterns = [
    path('knight/', include(knight_urls)),
]