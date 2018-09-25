from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response
from rest_framework import status

from drf_yasg.utils import swagger_auto_schema

from backend.core.mixins import LoggingMixin
from backend.core.serializers import (
    KnightMovesSerializer, ListMovesSerializer
)

from backend.core.models import Knight


class KnightMovesViewSet(LoggingMixin, GenericViewSet):
    """
    ViewSet to get Knight possible moves
    """
    serializer_class = KnightMovesSerializer

    @swagger_auto_schema(responses={200: ListMovesSerializer(many=True)})
    def get_moves_tree(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(
            serializer.get_tree_of_possible_moves,
            status.HTTP_200_OK
        )
