from django.db import models


class Compensation(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Contact(models.Model):
    phone = models.CharField(max_length=50, unique=True)
    address = models.CharField(max_length=50)

    def __str__(self):
        return self.phone


class Department(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)

    objects = models.manager

    def __str__(self):
        return self.name

Department.objects.all().add()

class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    contact = models.OneToOneField(Contact, on_delete=models.CASCADE, null=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, default=None)
    compensations = models.ManyToManyField(Compensation)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


# from django.db import models
#
#
# class Address(models.Model):
#     country = models.CharField(verbose_name='Страна', help_text='Введите название страны', max_length=50)
#     zip_code = models.CharField(verbose_name='Почтовый индекс', help_text='Введите почтовый индекс', max_length=10)
#     state = models.CharField(verbose_name='Область', help_text='Введите название области', max_length=100)
#     city = models.CharField(verbose_name='Город', help_text='Введите название города', max_length=50)
#     street = models.CharField(verbose_name='Улица', help_text='Введите название улицы', max_length=200)
#
#
# class Computer(models.Model):
#     model_name = models.CharField(verbose_name='Название модели', help_text='Введите название модели компьютера', max_length=50)
#     manufacturer = models.CharField(verbose_name='Производитель', help_text='Введите производителя компьютера', max_length=20)
#     cpu = models.CharField(verbose_name='Процессор', help_text='Введите модель процессора', max_length=50)
#     gpu = models.CharField(verbose_name='Видеокарта', help_text='Введите модель видеокарты', max_length=50)
#     ram_gb = models.PositiveSmallIntegerField(verbose_name='Объём оперативной памяти', help_text='Введите объём оперативной памяти в ГБ')
#     storage_gb = models.PositiveSmallIntegerField(verbose_name='Объём накопителя', help_text='Введите объём накопителя в ГБ')
#     os = models.CharField(verbose_name='Операционная система', help_text='Введите название операционной системы', max_length=30)
#     is_gaming = models.BooleanField(verbose_name='Игровой компьютер', help_text='Укажите, является ли компьютер игровым', default=False)
#     price = models.DecimalField(verbose_name='Цена', help_text='Введите цену компьютера', max_digits=10, decimal_places=2)
#
#
# class Project(models.Model):
#     name = models.CharField(verbose_name='Название проекта', help_text='Введите название проекта', max_length=200)
#     start_date = models.DateField(verbose_name='Дата начала проекта', help_text='Укажите дату начала проекта')
#     end_date = models.DateField(verbose_name='Дата окончания проекта', help_text='Укажите дату окончания проекта')
#     budget = models.DecimalField(verbose_name='Бюджет проекта', help_text='Введите бюджет проекта', max_digits=12, decimal_places=2)
#     progress = models.PositiveSmallIntegerField(verbose_name='Процент выполнения', help_text='Введите процент выполнения проекта')
#     description = models.TextField(verbose_name='Описание проекта', help_text='Введите описание проекта')
#     is_completed = models.BooleanField(verbose_name='Проект завершён', help_text='Укажите, завершён ли проект', default=False)
#     repository_url = models.URLField(verbose_name='URL репозитория', help_text='Введите URL репозитория проекта')
#     manager = models.CharField(verbose_name='Менеджер проекта', help_text='Введите имя менеджера проекта', max_length=50)
#     slug = models.SlugField(verbose_name='Слаг проекта', help_text='Введите слаг проекта', max_length=255, unique=True)
#
#
# class Ticket(models.Model):
#     flight_number = models.CharField('Номер рейса', help_text='Введите номер рейса', max_length=20)
#     departure_airport = models.CharField('Аэропорт вылета', help_text='Введите аэропорт вылета', max_length=30)
#     arrival_airport = models.CharField('Аэропорт прилёта', help_text='Введите аэропорт прилёта', max_length=30)
#     departure_time = models.DateTimeField('Дата и время вылета', help_text='Укажите дату и время вылета')
#     arrival_time = models.DateTimeField('Дата и время прилёта', help_text='Укажите дату и время прилёта')
#     seat_number = models.CharField('Номер места', help_text='Введите номер места', max_length=3)
#     passenger_name = models.CharField('Имя пассажира', help_text='Введите имя пассажира', max_length=50)
#     price = models.DecimalField('Цена билета', help_text='Введите цену билета', max_digits=8, decimal_places=2)
#     is_refundable = models.BooleanField('Билет возвратный', help_text='Укажите, является ли билет возвратным', default=False)
#     booking_reference = models.CharField('Номер бронирования', help_text='Введите номер бронирования', max_length=50, unique=True)
#
#
# class Event(models.Model):
#     name = models.CharField('Название мероприятия', help_text='Введите название мероприятия', max_length=100)
#     location = models.CharField('Место проведения', help_text='Введите место проведения мероприятия', max_length=250)
#     start_time = models.DateTimeField('Дата и время начала', help_text='Укажите дату и время начала мероприятия')
#     end_time = models.DateTimeField('Дата и время окончания', help_text='Укажите дату и время окончания мероприятия')
#     description = models.TextField('Описание мероприятия', help_text='Введите описание мероприятия')
#     organizer = models.CharField('Организатор мероприятия', help_text='Введите имя организатора мероприятия', max_length=50)
#     is_free = models.BooleanField('Мероприятие бесплатное', help_text='Укажите, является ли мероприятие бесплатным', default=True)
#     capacity = models.PositiveIntegerField('Вместимость мероприятия', help_text='Введите вместимость мероприятия')
#     registration_deadline = models.DateTimeField('Окончание регистрации', help_text='Укажите дату и время окончания регистрации')
#     website_url = models.URLField('Ссылка на сайт', help_text='Введите ссылку на сайт мероприятия')
#
#
# class UserProfile(models.Model):
#     username = models.CharField('Имя пользователя', help_text='Укажите уникальное имя пользователя для входа в систему', max_length=50, unique=True)
#     first_name = models.CharField('Имя', help_text='Введите имя', max_length=50)
#     last_name = models.CharField('Фамилия', help_text='Введите фамилию', max_length=50)
#     email = models.EmailField('Электронный адрес', help_text='Введите электронный адрес', unique=True)
#     birth_date = models.DateField('Дата рождения', help_text='Укажите дату рождения')
#     is_active = models.BooleanField('Активен', help_text='Укажите, активен ли аккаунт', choices={True: 'Активен', False: 'Отключен'}, default=True)
#     phone_number = models.CharField('Номер телефона', help_text='Введите номер телефона', max_length=20, blank=True)
#     registration_date = models.DateTimeField('Дата регистрации', auto_now_add=True)
#     registration_ip = models.GenericIPAddressField('IP адрес регистрации', editable=False, null=True)
#     last_login = models.DateTimeField('Последний вход', auto_now=True)
#     last_login_ip = models.GenericIPAddressField('IP адрес последнего входа', editable=False, null=True)
#
#
# class CustomerReview(models.Model):
#     product_name = models.CharField('Название продукта', help_text='Введите название продукта', max_length=200)
#     customer_name = models.CharField('Имя', help_text='Введите имя', max_length=150)
#     review_text = models.TextField('Текст отзыва', help_text='Введите текст отзыва')
#     rating = models.PositiveSmallIntegerField('Оценка', help_text='Выберите оценку от 1 до 5',
#                                               choices={
#                                                   1:'1 Звезда',
#                                                   2:'2 Звезды',
#                                                   3:'3 Звезды',
#                                                   4:'4 Звезды',
#                                                   5:'5 Звёзд',
#                                               },
#                                               default=5)
#     review_date = models.DateField('Дата отзыва', auto_now_add=True)
#     is_approved = models.BooleanField('Отзыв подтверждён', help_text='Укажите подтверждён ли отзыв', default=False)
#     likes_count = models.PositiveIntegerField('Количество лайков', default=0, editable=False)
#     dislikes_count = models.PositiveIntegerField('Количество дизлайков', default=0, editable=False)
#     email = models.EmailField('Электронная почта', help_text='Введите электронную почту')
#     ip_address = models.GenericIPAddressField('IP адрес клиента', editable=False, null=True)
#
#
# from django.core.validators import FileExtensionValidator
#
#
# class Movie(models.Model):
#     title = models.CharField('Название фильма', help_text='Введите название фильма', max_length=100)
#     slug = models.SlugField('Слаг фильма', help_text='Введите слаг фильма', max_length=150, unique=True)
#     director = models.CharField('Имя режиссёра', help_text='Введите имя режиссёра', max_length=50)
#     release_year = models.PositiveSmallIntegerField('Год выпуска', help_text='Введите год выпуска фильма')
#     duration = models.PositiveSmallIntegerField('Продолжительность', help_text='Введите продолжительность фильма в минутах')
#     genre = models.CharField('Жанр фильма', help_text='Введите жанр фильма', max_length=100)
#     rating = models.FloatField('Рейтинг фильма', help_text='Введите рейтинг фильма')
#     description = models.TextField('Описание фильма', help_text='Введите описание фильма')
#     poster = models.ImageField('Постер фильма',
#                                help_text='Загрузите постер фильма',
#                                blank=True,
#                                upload_to='posters',
#                                validators=[FileExtensionValidator(allowed_extensions=('png', 'jpg', 'jpeg'))],
#                                default='posters/default.jpg')
#     trailer_url = models.URLField('Ссылка на трейлер', help_text='Введите ссылку на трейлер фильма')
#     budget = models.DecimalField('Бюджет фильма', help_text='Введите бюджет фильма', max_digits=12, decimal_places=2)
#
#
# class Album(models.Model):
#     title = models.CharField('Название альбома', help_text='Введите название альбома', max_length=200)
#     slug = models.SlugField('Слаг альбома', help_text='Введите слаг альбома', max_length=255, unique=True)
#     artist = models.CharField('Имя исполнителя', help_text='Введите имя исполнителя', max_length=50)
#     release_date = models.DateField('Дата выпуска альбома', help_text='Укажите дату выпуска альбома')
#     genre = models.CharField('Жанр альбома', help_text='Введите жанр альбома', max_length=100)
#     record_label = models.CharField('Лейбл звукозаписи', help_text='Введите название лейбла звукозаписи', max_length=50)
#     number_of_tracks = models.PositiveSmallIntegerField('Количество треков', help_text='Укажите количество треков в альбоме')
#     cover_art = models.ImageField('Обложка альбома',
#                                   help_text='Загрузите обложку альбома',
#                                   blank=True,
#                                   upload_to='album_covers',
#                                   validators=[FileExtensionValidator(allowed_extensions=('png', 'jpg', 'jpeg', 'gif'))],
#                                   default='album_covers/default.jpg')
#     price = models.DecimalField('Цена альбома', help_text='Введите цену альбома', max_digits=8, decimal_places=2)
#     is_available = models.BooleanField('Альбом доступен', help_text='Укажите, доступен ли альбом для покупки',
#                                        choices={True:'Доступен', False:'Не доступен'},
#                                        default=True)
#
#
# class Track(models.Model):
#     title = models.CharField('Название трека', help_text='Введите название трека', max_length=200)
#     slug = models.SlugField('Слаг трека', help_text='Введите слаг трека', max_length=255, unique=True)
#     artist = models.CharField('Имя исполнителя', help_text='Введите имя исполнителя', max_length=50)
#     album = models.CharField('Название альбома', help_text='Введите название альбома', max_length=150, blank=True)
#     duration = models.PositiveSmallIntegerField('Длительность трека', help_text='Введите длительность трека в секундах')
#     release_date = models.DateField('Дата выпуска', help_text='Укажите дату выпуска трека')
#     genre = models.CharField('Жанр музыки', help_text='Введите жанр музыки', max_length=50)
#     audio_file = models.FileField('Аудиофайл',
#                                   help_text='Загрузите аудиофайл',
#                                   upload_to='audio',
#                                   validators=[FileExtensionValidator(allowed_extensions=('mp3', 'wav', 'ogg'))])
#     cover_art = models.ImageField('Обложка альбома',
#                                   help_text='Загрузите обложку альбома',
#                                   blank=True,
#                                   upload_to='covers',
#                                   validators=[FileExtensionValidator(allowed_extensions=('png', 'jpg', 'jpeg'))],
#                                   default='covers/default.jpg')
#     plays_count = models.PositiveIntegerField('Количество прослушиваний', default=0, editable=False)
#
# import uuid
# from django.core.validators import FileExtensionValidator
# from django.db import models
#
#
# class Message(models.Model):
#     EXTENTSIONS = ('txt', 'doc', 'docx', 'xls', 'xlsx', 'ppt', 'pptx', 'pdf')
#
#     id = models.UUIDField('Уникальный идентификатор', primary_key=True, default=uuid.uuid4, editable=False)
#     sender = models.CharField('Отправитель сообщения', help_text='Введите имя отправителя', max_length=100)
#     recipient = models.CharField('Получатель сообщения', help_text='Введите имя получателя', max_length=100)
#     subject = models.CharField('Тема сообщения', help_text='Введите тему сообщения', max_length=200)
#     body = models.TextField('Текст сообщения', help_text='Введите текст сообщения')
#     sent_at = models.DateTimeField('Дата и время отправки', auto_now_add=True)
#     is_read = models.BooleanField('Сообщение прочитано', help_text='Укажите, прочитано ли сообщение',
#                                   choices={True: 'Прочитано', False: 'Не прочитано'}, default=False)
#     priority = models.CharField('Приоритет сообщения',
#                                 help_text='Выберите приоритет сообщения',
#                                 max_length=1,
#                                 choices={
#                                     'L': 'Низкий',
#                                     'M': 'Средний',
#                                     'H': 'Высокий',
#                                 },
#                                 default='M')
#     attachment = models.FileField('Файл вложения',
#                                   help_text='Загрузите файл вложения к сообщению',
#                                   blank=True,
#                                   upload_to='attachments',
#                                   validators=[FileExtensionValidator(allowed_extensions=EXTENTSIONS)],
#                                   )
