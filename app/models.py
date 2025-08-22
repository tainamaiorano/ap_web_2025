from django.db import models
from django.contrib.auth.models import User
#para alterar caracteristicas do usuário do django
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .user_manager import CustomUserManager #usar ponto quando estiver na mesma pasta o que quiser importar e .. para fora da pasta

CATEGORIES = [
    ('HORROR','Terror'),
    ('COMEDY','Comédia'),
    ('FICTION','Ficção'),
    ('DRAMA','Drama'),
    ('ACTION','Ação'),
]

class CustomUser(AbstractBaseUser, PermissionsMixin): #username, email e senha é padrao do django pedir e ser obrigatorio 
    name = models.CharField(max_length=255) # no djando tem nomee sobrenome, quis em um unico os dois
    email = models.EmailField(unique=True) # já é obrigatorio mas não o unique
    cpf = models.CharField(max_length=12, unique=True) 
    phone_number = models.CharField(max_length=15, null=True, blank=True, unique=True) 
    birth_date = models.DateField(null=True, blank=True)

    #pode acessar tela do django ou não 
    is_staff = models.BooleanField(default=False)
    #se o usuario esta ativo ou não
    is_active = models.BooleanField(default=True)

    #fala que o login agora é por email ao inves do padrao username
    USERNAME_FIELD = "email"

    #o que é obigatorio alem das que o django já obriga
    REQUIRED_FIELDS = ["cpf"] 

    objects = CustomUserManager()


class Director(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Movie(models.Model): 
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    category = models.CharField(max_length=100, choices=CATEGORIES)
    published_date = models.DateField()
    photo = models.TextField()
    classification = models.IntegerField()
    directors = models.ManyToManyField(Director)

    def __str__(self):
        return self.title

class Plan(models.Model):
    name = models.CharField(max_length=150)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name
    
class UserPlan(models.Model):
    plan_FK = models.ForeignKey(Plan, related_name='UserPlan_plan_FK', on_delete=models.CASCADE)
    user_FK = models.ForeignKey(CustomUser, related_name='UserPlan_user_FK', on_delete=models.CASCADE)
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f'{self.user_FK.username}-{self.plan_FK.name}'

class FavoriteMovie(models.Model):
    movie_FK = models.ForeignKey(Movie, related_name='FavoriteMovie_movie_FK', on_delete=models.CASCADE)
    user_FK = models.ForeignKey(CustomUser, related_name='FavoriteMovie_user_FK', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user_FK.username}-{self.movie_FK.name}'
    

