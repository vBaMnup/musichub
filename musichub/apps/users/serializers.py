from drf_extra_fields.fields import Base64ImageField
from djoser.serializers import UserCreateSerializer
from rest_framework import serializers

from apps.users.models import AuthUser, SocialLinks


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthUser
        fields = ('avatar', 'country', 'city', 'bio', 'display_name')


class CustomUserCreateSerializer(UserCreateSerializer):

    class Meta:
        model = AuthUser
        fields = (
            'email', 'username', 'first_name', 'last_name', 'password',
        )


class SocialLinkSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = SocialLinks
        fields = ('id', 'link', )


class AuthorSerializer(serializers.ModelSerializer):
    social_links = SocialLinkSerializer(many=True)

    class Meta:
        model = AuthUser
        fields = ('id', 'avatar', 'country', 'city', 'bio', 'display_name',
                  'social_links')
