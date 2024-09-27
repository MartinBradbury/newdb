from rest_framework import serializers
from .models import Profile
from followers.models import Follow

class ProfieSerializer(serializers.ModelSerializer):
    owner= serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    """
    Allow users to follow profiles and identify with an ID
    """
    following_id = serializers.SerializerMethodField()

    def get_following_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            following = Follow.objects.filter(
                owner=user, followed=obj.owner
            ).first()
            print(following)
            return following.id if following else None
        return None

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner
    
    class Meta:
        model = Profile
        fields = [
                    'owner', 'created_at', 'updated_at',
                    'name', 'content', 'image', 'is_owner',
                    'following_id',
            ]