from rest_framework import serializers

from server.presentations.models import Creator, Presentation


class CreatorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Creator
        exclude = ("created_at", "updated_at")


class PresentationSerializer(serializers.ModelSerializer):
    creator = CreatorSerializer(read_only=True)

    class Meta:
        model = Presentation
        fields = "__all__"

