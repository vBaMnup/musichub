import os

from apps.api.classes import MixedSerializer, Pagination
from apps.api.permissions import IsAuthor
from apps.api.services import delete_old_file
from apps.audio_library.models import (Album, Comment, Genre, License,
                                       Playlist, Track)
from apps.audio_library.serializers import (AlbumSerializer,
                                            AuthorTrackSerializer,
                                            CommentAuthorSerializer,
                                            CommentSerializer,
                                            CreateAuthorTrackSerializer,
                                            CreatePlayListSerializer,
                                            GenreSerializer, LicenseSerializer,
                                            PlayListSerializer)
from django.http import FileResponse, Http404
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, views, viewsets
from rest_framework.parsers import MultiPartParser


class GenreView(generics.ListAPIView):
    """
    Список жанров
    """
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class LicenseView(viewsets.ModelViewSet):
    """
    CRUD лицензий автора
    """
    serializer_class = LicenseSerializer
    permission_classes = [IsAuthor, ]

    def get_queryset(self):
        return License.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class AlbumView(viewsets.ModelViewSet):
    """
    CRUD для альбомов автора
    """
    parser_classes = (MultiPartParser, )
    serializer_class = AlbumSerializer
    permission_classes = [IsAuthor]

    def get_queryset(self):
        return Album.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def perform_destroy(self, instance):
        delete_old_file(instance.cover.path)
        instance.delete()


class PublicAlbumView(generics.ListAPIView):
    """
    Список публичных альбомов автора
    """
    serializer_class = AlbumSerializer

    def get_queryset(self):
        return Album.objects.filter(user__id=self.kwargs.get('pk'),
                                    private=False)


class TrackView(MixedSerializer, viewsets.ModelViewSet):
    """
    CRUD для треков
    """
    parser_classes = (MultiPartParser, )
    permission_classes = [IsAuthor]
    serializer_class = CreateAuthorTrackSerializer
    serializer_classes_by_action = {
        'list': AuthorTrackSerializer
    }

    def get_queryset(self):
        return Track.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def perform_destroy(self, instance):
        delete_old_file(instance.file.path)
        delete_old_file(instance.cover.path)
        instance.delete()


class PlayListView(MixedSerializer, viewsets.ModelViewSet):
    """
    CRUD для плейлистов
    """
    parser_classes = (MultiPartParser,)
    permission_classes = [IsAuthor]
    serializer_class = CreatePlayListSerializer
    serializer_classes_by_action = {
        'list': PlayListSerializer
    }

    def get_queryset(self):
        return Playlist.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def perform_destroy(self, instance):
        delete_old_file(instance.cover.path)
        instance.delete()


class TrackListView(generics.ListAPIView):
    """
    Вывод всех треков
    """
    queryset = Track.objects.filter(album__private=False, private=False)
    serializer_class = AuthorTrackSerializer
    pagination_class = Pagination
    filter_backends = [DjangoFilterBackend]
    filterset_fields = [
        'title',
        'user__display_name',
        'album__name',
        'genre__name',
    ]


class AuthorTrackListView(generics.ListAPIView):
    """
    Вывод всех треков автора
    """
    serializer_class = AuthorTrackSerializer
    pagination_class = Pagination
    filter_backends = [DjangoFilterBackend]
    filterset_fields = [
        'title',
        'album__name',
        'genre__name',
    ]

    def get_queryset(self):
        return Track.objects.filter(
            user__id=self.kwargs.get('pk'),
            album__private=False, private=False
        )


class StreamingFileView(views.APIView):
    """
    Прослушивание трека
    """
    def set_play(self, track):
        track.play_count += 1
        track.save()

    def get(self, request, pk):
        track = get_object_or_404(Track, id=pk)
        if os.path.exists(track.file.path):
            self.set_play(track)
            return FileResponse(open(track.file.path, 'rb'),
                                filename=track.file.name)
        return Http404


class DownloadTrackView(views.APIView):
    """
    Скачивание трека
    """
    def set_download(self):
        self.track.download += 1
        self.track.save()

    def get(self, request, pk):
        self.track = get_object_or_404(Track, id=pk)
        if os.path.exists(self.track.file.path):
            self.set_download()
            return FileResponse(open(self.track.file.path, 'rb'),
                                filename=self.track.file.name,
                                as_attachment=True)
        return Http404


class CommentAuthorView(viewsets.ModelViewSet):
    """
    CRUD комментариев автора
    """
    serializer_class = CommentAuthorSerializer
    permission_classes = [IsAuthor]

    def get_queryset(self):
        return Comment.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CommentView(viewsets.ModelViewSet):
    """
    Коментарии к треку
    """
    serializer_class = CommentSerializer

    def get_queryset(self):
        return Comment.objects.filter(track__id=self.kwargs.get('pk'))
