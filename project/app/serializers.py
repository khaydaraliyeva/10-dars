from .models import Video
from rest_framework import serializers
class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = '__all__'

    def create(self, validated_data):
        # Faylni yuklashdan oldin alohida usulda handle qilish
        video = validated_data.pop('video', None)
        instance = Video.objects.create(**validated_data)
        if video:
            instance.video = video
            instance.save()
        return instance
