<h1>Документация проекта</h1>

<h2>Описание</h2>
<p>Это серверный проект, реализованный с использованием Django, который предоставляет API для управления движением денежных средств (ДДС).</p>
<p>Проект включает модели для учета финансовых операций, включая типы, категории и подкатегории, а также сериализаторы и API методы для взаимодействия с сервером.</p>

<h2>Технологии</h2>
<ul>
    <li>Django</li>
    <li>Django REST Framework</li>
    <li>Docker</li>
    <li>Swagger (для документации API)</li>
</ul>


<h2>Запуск проекта</h2>
<h3>1. Клонирование репозитория</h3>
<pre>
    git clone https://github.com/lxftx/dds.git
</pre>
    
<h3>2. Запуск с использованием Docker</h3>
<p>Для запуска проекта с помощью Docker, выполните следующие шаги:</p>
<ul>
    <li>Построить контейнеры: <code>docker-compose --env-file ./.env build</code></li>
    <li>Запустить контейнеры: <code>docker-compose --env-file ./.env up</code></li>
    <li>Создать суперпользователя (если нужно): <code>docker-compose run --rm ddsservice sh -c "python manage.py createsuperuser"</code></li>
</ul>
<p>После этого сервер будет доступен по адресу: <strong>http://localhost:8000</strong>.</p>

<h2>API Документация</h2>
<p>API для работы с моделями доступно через Swagger:</p>
<ul>
    <li>Для получения документации откройте: <a href="http://localhost:8000/swagger/">Swagger UI</a></li>
</ul>

<h2>Серверные методы</h2>
<p>В проекте реализованы следующие API методы:</p>
<ul>
    <li><strong>GET /api/cashflow/</strong> — Получение списка записей о движении денежных средств</li>
    <li><strong>POST /api/cashflow/</strong> — Создание новой записи</li>
    <li><strong>GET /api/cashflow/{id}/</strong> — Получение подробной информации о записи</li>
    <li><strong>PUT /api/cashflow/{id}/</strong> — Обновление записи</li>
    <li><strong>DELETE /api/cashflow/{id}/</strong> — Удаление записи</li>
<br>
    <li><strong>GET /api/subcategory/</strong> — Получение списка записей о подкатегориях</li>
    <li><strong>POST /api/subcategory/</strong> — Создание новой записи</li>
    <li><strong>GET /api/subcategory/{id}/</strong> — Получение подробной информации о записи</li>
    <li><strong>PUT /api/subcategory/{id}/</strong> — Обновление записи</li>
    <li><strong>DELETE /api/subcategory/{id}/</strong> — Удаление записи</li>
<br>
    <li><strong>GET /api/category/</strong> — Получение списка записей о категориях</li>
    <li><strong>POST /api/category/</strong> — Создание новой записи</li>
    <li><strong>GET /api/category/{id}/</strong> — Получение подробной информации о записи</li>
    <li><strong>PUT /api/category/{id}/</strong> — Обновление записи</li>
    <li><strong>DELETE /api/category/{id}/</strong> — Удаление записи</li>
<br>
    <li><strong>GET /api/type/</strong> — Получение списка записей о типах</li>
    <li><strong>POST /api/type/</strong> — Создание новой записи</li>
    <li><strong>GET /api/type/{id}/</strong> — Получение подробной информации о записи</li>
    <li><strong>PUT /api/type/{id}/</strong> — Обновление записи</li>
    <li><strong>DELETE /api/type/{id}/</strong> — Удаление записи</li>
<br>
    <li><strong>GET /api/status/</strong> — Получение списка записей о статусах</li>
    <li><strong>POST /api/status/</strong> — Создание новой записи</li>
    <li><strong>GET /api/status/{id}/</strong> — Получение подробной информации о записи</li>
    <li><strong>PUT /api/status/{id}/</strong> — Обновление записи</li>
    <li><strong>DELETE /api/status/{id}/</strong> — Удаление записи</li>
</ul>

<p>&copy; 2025 Олег Зеленский, Сервер для управления движением денежных
средств</p>