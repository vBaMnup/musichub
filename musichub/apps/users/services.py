from django.core.exceptions import ValidationError


def get_path_upload_avatar(instance, file):
    """
    Создание пути для загрузки аватара
    Формат: (media)/avatar/user_id/name.jpg
    """
    return f'avatar/{instance.id}/{file}'


def validate_size_image(file_obj):
    """
    Проверка размера файла
    """
    mb_limit = 2
    if file_obj.size > mb_limit * 1024 * 1024:
        raise ValidationError(f'Максимальный размер файла {mb_limit} МБ.')

