# Онлайн платформа торговой сети электроники

Данное приложение представляет собой backend часть для системы управления 
торговой сетью электроники.

Возможности:

* Работа с элементами торговой сети.
* Работа с продуктами.
* Админ-панель для удобного управления сетью.
* API интерфейс для интеграции с другими приложениями.

## Установка

1. Клонируйте репозиторий с проектом себе на устройство
2. Установите зависимости командой `pip install -r requirements.txt`
3. Переименуйте файл .env.sample в .env и заполните **все** поля в нем.
4. Примените миграции командой `python manage.py migrate`
5. Запустите сервер командой `python manage.py runserver`
6. Для доступа в админ-панель вам нужно создать суперпользователя командой
`python manage.py csu`. Данные для входа в админку вы указали в файле .env

Для наполнения приложения тестовыми данными можно выполнить команду
`python -Xutf8 manage.py loaddata testdata.json`

## Использование

### Действия с пользователями

Для регистрации нового пользователя нужно отправить post-запрос на адрес
/users/register/.

Запрос должен передавать следующую информацию:

```
{
    "password": <пароль>,
    "email": <email>,
    "first_name": <имя>,
    "last_name": <фамилия>,
    "patronymic": <отчество (не обязательно)>,
    "phone": <телефон>
}
```

Для входа в систему нужно отправить post-запрос на адрес /users/login/.
В запросе нужно передать email и пароль.

```
{
    "email": <email>,
    "password": <пароль>
}
```

### Действия с элементами торговой сети

* Создать звено торговой сети - post-запрос на адрес /trade_network/create/.

```
{
    "name": <название>,
    "email": <email>,
    "type": <тип (один из 'factory', 'retail_network', 'individual entrepreneur')>,
    "country": <страна>,
    "city": <город>,
    "street": <улица>,
    "house": <дом>,
    "debt": <задолженность перед поставщиком (не обязательно, по умолчанию 0)>,
    "supplier": <поставщик (не обязательно)>
}
```

* Просмотр списка объектов - get-запрос на адрес /trade_network/
* Просмотр конкретного объекта - get-запрос на адрес /trade_network/\<id>/
* Изменить объект - patch-запрос на адрес /trade_network/\<id>/update/  
  Изменять поле задолженности "debt" нельзя.
* Удалить объект - delete-запрос на адрес /trade_network/\<id>/delete/

### Действия с продуктами

* Создать продукт - post-запрос на адрес /product/create/.

```
{
    "name": <название>,
    "description": <описание>,
    "model": <модель>,
    "release_date": <дата выхода продукта на рынок>,
    "trade_network": <сеть, которой этот продукт пренадлежит>,
}
```

* Просмотр списка продуктов - get-запрос на адрес /products/
* Просмотр конкретного продукта - get-запрос на адрес /products/\<id>/
* Изменить продукт - patch-запрос на адрес /products/\<id>/update/
* Удалить продукт - delete-запрос на адрес /products/\<id>/delete/
