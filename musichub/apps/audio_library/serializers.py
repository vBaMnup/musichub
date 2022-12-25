from apps.api.services import delete_old_file
from apps.audio_library.models import (Album, Comment, Genre, License,
                                       Playlist, Track)
from apps.users.serializers import AuthorSerializer
from rest_framework import serializers


class BaseSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)


class GenreSerializer(BaseSerializer):
    class Meta:
        model = Genre
        fields = ('id', 'name', )


class LicenseSerializer(BaseSerializer):
    class Meta:
        model = License
        fields = ('id', 'text', )


class AlbumSerializer(BaseSerializer):
    class Meta:
        model = Album
        fields = ('id', 'name', 'description', 'cover', 'private')

    def update(self, instance, validated_data):
        delete_old_file(instance.cover.path)
        return super().update(instance, validated_data)


class CreateAuthorTrackSerializer(BaseSerializer):
    play_count = serializers.IntegerField(read_only=True)
    download = serializers.IntegerField(read_only=True)
    user = serializers.IntegerField(read_only=True)

    class Meta:
        model = Track
        fields = (
            'id',
            'title',
            'license',
            'genre',
            'album',
            'link_of_author',
            'file',
            'create_at',
            'play_count',
            'download',
            'private',
            'cover',
            'user',
        )

    def update(self, instance, validated_data):
        delete_old_file(instance.file.path)
        delete_old_file(instance.cover.path)
        return super().update(instance, validated_data)


class AuthorTrackSerializer(CreateAuthorTrackSerializer):
    license = LicenseSerializer()
    genre = GenreSerializer(many=True)
    album = AlbumSerializer()
    user = AuthorSerializer()


class CreatePlayListSerializer(BaseSerializer):
    class Meta:
        model = Playlist
        fields = ('id', 'title', 'cover', 'tracks')

    def update(self, instance, validated_data):
        delete_old_file(instance.cover.path)
        return super().update(instance, validated_data)


class PlayListSerializer(CreatePlayListSerializer):
    tracks = AuthorTrackSerializer(many=True, read_only=True)

    class Meta:
        model = Playlist
        fields = ('id', 'title', 'cover', 'tracks')


class CommentAuthorSerializer(serializers.ModelSerializer):
    """
    Сериалайзер комментариев
    """
    class Meta:
        model = Comment
        fields = ('id', 'text', 'track')


class CommentSerializer(serializers.ModelSerializer):
    user = AuthorSerializer()

    class Meta:
        model = Comment
        fields = ('id', 'text', 'user', 'track', 'create_at')
