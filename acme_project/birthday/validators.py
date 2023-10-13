from datetime import date

from django.core.exceptions import ValidationError


def real_age(value: date) -> None:
    # Считаем разницу между сегодняшним днём и днём рождения в днях 
    # и делим на 365.
    age = (date.today() - value).days / 365
    # Если возраст меньше 0 года или больше 150 лет — выбрасываем ошибку валидации.
    if age < 0 or age > 150:
        raise ValidationError(
            'Ожидается возраст от 0 года до 150 лет'
        )