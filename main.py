import pytest
from programs import quad_equation, brave_sysadmin, acquaintance, api_yandex


@pytest.mark.parametrize(
    'a, b, c, expected',
    [
        (1, 8, 15, '-3.0 -5.0'),
        (1, -13, 12, '12.0 1.0'),
        (-4, 28, -49, '3.5'),
        (1, 1, 1, 'корней нет')
    ]
)
def test_quad_equation(a, b, c, expected):
    result = quad_equation(a, b, c)
    assert result == expected


@pytest.mark.parametrize(
    'models, available, manufacturers, expected',
    [
        (
            ['480 ГБ 2.5" SATA накопитель Kingston A400', '500 ГБ 2.5" SATA накопитель Samsung 870 EVO',
             '480 ГБ 2.5" SATA накопитель ADATA SU650', '240 ГБ 2.5" SATA накопитель ADATA SU650',
             '250 ГБ 2.5" SATA накопитель Samsung 870 EVO', '256 ГБ 2.5" SATA накопитель Apacer AS350 PANTHER',
             '480 ГБ 2.5" SATA накопитель WD Green', '500 ГБ 2.5" SATA накопитель WD Red SA500'],
            [1, 1, 1, 1, 0, 1, 1, 0],
            ['Intel', 'Samsung', 'WD'],
            (['500 ГБ 2.5" SATA накопитель Samsung 870 EVO', '480 ГБ 2.5" SATA накопитель WD Green'], 2)
        )
    ]
)
def test_brave_sysadmin(models, available, manufacturers, expected):
    result = brave_sysadmin(models, available, manufacturers)
    assert result == expected


@pytest.mark.parametrize(
    'boys, girls, expected',
    [
        (
            ['Peter', 'Alex', 'John', 'Arthur', 'Richard'],
            ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha'],
            'Alex и Emma, Arthur и Kate, John и Kira, Peter и Liza, Richard и Trisha'
        ),
        (
            ['Peter', 'Alex', 'John', 'Arthur'],
            ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha'],
            'Кто-то может остаться без пары!'
        ),
        (
            ['Peter', 'Alex', 'John', 'Arthur', 'Richard'],
            ['Kate', 'Liza', 'Kira', 'Emma'],
            'Кто-то может остаться без пары!'
        )
    ]
)
def test_acquaintance(boys, girls, expected):
    result = acquaintance(boys, girls)
    assert result == expected


@pytest.mark.parametrize(
    'path, status_code',
    [
        ('test_folder', 201),
        ('test_folder', 409)
    ]
)
def test_api_yandex(path, status_code):
    # Вставьте ниже ваш токен от Яндекс.Диск REST API
    token = ''
    result = api_yandex(token, path).status_code
    assert result == status_code
