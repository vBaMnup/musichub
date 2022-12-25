from django.contrib import admin

from .models import Album, Comment, Genre, License, Playlist, Track


@admin.register(License)
class LicenseAdmin(admin.ModelAdmin):
    list_display = ('id', 'user')
    list_display_links = ('user', )
    list_filter = ('user', )


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('name', )


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'name')
    list_display_links = ('user', )
    list_filter = ('user', )


@admin.register(Track)
class TrackAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'title', 'create_at')
    list_display_links = ('title', 'user')
    list_filter = ('genre', 'create_at')
    search_fields = ('user__email', 'user__display_name', 'genre__name')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'track')
    list_display_links = ('user', )


@admin.register(Playlist)
class PlaylistAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'title')
    list_display_links = ('title', 'user')
    search_fields = ('user__email', 'user__display_name', 'tracks__title')
