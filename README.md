# Проект "Homework_1"

## Описание:
Проект "Homework_1" - это виджеты на Python для управления банковских операций клиента. 

## Установка:
1. Клонируйте репозиторий:
```
git clone https://github.com/AvetisGrigoryan/Homework_1.git
```
2. Установите виртуальное окружение:
```
python3 -m venv myenv
```
3. Установите линтер flake8:
```
poetry add --group lint flake8
```
4. Установите  это статический анализатор mypy:
```
poetry add --group lint mypy
```
5. Установите форматер кода black:
```
poetry add --group lint black
```
6. Установите форматер кода isort:
```
poetry add --group lint isort
```
## Использование:
1. Запускаем для проверки модуль "masks.py". В нём реализованы две функции которые маскируют номер карты и счет клиента.
2. Запускаем для проверки модуль "widget.py". В нём реализованы две функции которые маскируют номер карты и счета и возвращает дату в нужном формате.
3. Запускаем для проверки модуль "processing.py". В нем реализованы две функции: первая возвращают новый список словарей по ключу, вторая возвращает отсортированный список по дате.
4. Оставьте комментарий для исправлений работы функций.

## Контакты:
Аветис - avetisgrib@gmail.com

Ссылка на проект - [GitHub](https://github.com/AvetisGrigoryan/Homework_1.git)
