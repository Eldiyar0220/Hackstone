from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models


class MyUserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, email, password, **extra_fields):
        email = self.normalize_email(email)
        user = self.model(email=email)     #user = User(username=username, email=(email)  -> user.save())
        user.set_password(password)
        user.create_activation_code()  # создает активацию кода
        user.save(using=self._db)
        return user




    def create_superuser(self, email, password=None,  **extra_fields):
        email = self.normalize_email(email)
        user = self.model(email=email)
        user.set_password(password)
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class MyUser(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=False)
    activation_code = models.CharField(max_length=50, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = MyUserManager()

    def __str__(self):
        return self.email

    def create_activation_code(self):
        """вариант 1
        1.1 hashlib.md5(self.email * self.id)).encode() --> hexdigest()
        2. get_random_string(50, allowed_char=['which symbols are allowed in this string'])
        3. uuid
        4. datetime.datetime.now() or time.time() + timetamp() 01.01.1978
         """
        import hashlib
        string = self.email + str(self.id)
        encode_string = string.encode()
        md5_object = hashlib.md5(encode_string)
        activation_code = md5_object.hexdigest()
        #чтобы у каждого юзера была разные цифры
        self.activation_code = activation_code
#TODO: create activation code


