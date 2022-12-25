import os

from django.core.exceptions import ValidationError


def get_path_upload_avatar(instance, file):
    """
    Создание пути для загрузки аватара
    Формат: (media)/avatar/user_id/name.jpg
    """
    return f'avatar/user_{instance.id}/{file}'


def get_path_upload_cover_album(instance, file):
    """
    Создание пути для загрузки обложки альбома
    Формат: (media)/album/user_id/name.jpg
    """
    return f'album/user_{instance.user.id}/{file}'


def get_path_upload_track(instance, file):
    """
    Создание пути для загрузки трека
    Формат: (media)/track/user_id/track.mp3
    """
    return f'track/user_{instance.user.id}/{file}'


def get_path_upload_cover_playlist(instance, file):
    """
    Создание пути для загрузки обложки плейлиста
    Формат: (media)/playlist/user_id/name.jpg
    """
    return f'playlist/user_{instance.user.id}/{file}'


def validate_size_image(file_obj):
    """
    Проверка размера файла
    """
    mb_limit = 2
    if file_obj.size > mb_limit * 1024 * 1024:
        raise ValidationError(f'Максимальный размер файла {mb_limit} МБ.')


def get_path_upload_cover_track(instance, file):
    """
        Создание пути для загрузки обложки трека
        Формат: (media)/track/cover/user_id/name.jpg
        """
    return f'track/cover/user_{instance.user.id}/{file}'


def delete_old_file(path_file):
    """
    Удаление старого файла
    """
    if os.path.exists(path_file):
        os.remove(path_file)
