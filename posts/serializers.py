from rest_framework import serializers
from .models import Post
from cloudinary.models import CloudinaryField

class PostSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.username")
    is_owner = serializers.SerializerMethodField()
    image = serializers.FileField(max_length=None)

    def validate_image(self, value):
        if value.size > 2 * 1024 * 1024:  # 2MB in bytes
            raise serializers.ValidationError("Image file must be no larger than 2MB.")
        return value

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner
    
    class Meta:
        model = Post
        fields = [
            'owner', 'created_at', 'updated_at',
            'title', 'content', 'image', 'is_owner',
        ]
