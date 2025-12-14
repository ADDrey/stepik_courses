pip install django

python -m django --version

django-admin startproject Course_SecondProject .

python manage.py runserver

python manage.py migrate

python manage.py startapp blog

python manage.py test   # run all tests

python manage.py makemigrations

python manage.py createsuperuser  # for admin panel

python manage.py changepassword admin

SECRET_KEY: Случайно сгенерированный секретный ключ, используемый для защиты от подделок CSRF (Cross-Site Request Forgery) и других атак. Генерируйте его с помощью python manage.py shell и import secrets; secrets.token_hex(32) и никогда не коммитите в публичный репозиторий!

print(posts.query)  # For watching SQL requests