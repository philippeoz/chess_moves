from django.conf import settings

from rest_framework import serializers

from backend.core.models import Knight


class RecursiveField(serializers.Serializer):
    """
    To a class recursively self serialize
    """
    def to_representation(self, value):
        serializer = self.parent.parent.__class__(value, context=self.context)
        return serializer.data


class ListMovesSerializer(serializers.Serializer):
    """
    A serializer to drescribe response of get moves request
    """
    from_position = serializers.CharField()
    to_position = serializers.CharField()
    next_turn = RecursiveField(many=True)


class KnightMovesSerializer(serializers.Serializer):
    """
    Serializer to Knight moves endpoint
    """
    position = serializers.RegexField(
        regex=r'^[N]([a-z]|[0-9]+_)[0-9]+$',
        max_length=None,
        min_length=3,
        trim_whitespace=True,
        required=True
    )
    board_size = serializers.IntegerField(min_value=1, required=False)
    turns = serializers.IntegerField(min_value=1, required=False)

    @property
    def get_tree_of_possible_moves(self):
        return Knight.moves_tree_from_position(
            self.validated_data.get('position'),
            turns=self.validated_data.get('turns') or settings.TURNS_AMOUNT,
            board_size=self.validated_data.get(
                'board_size') or settings.BOARD_SIZE,
        )
