# GET PUT POST DELETE

from .models import *
from .serializers import *
from rest_framework.viewsets import ModelViewSet

class DirectorView(ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = DirectorSerializer

class MovieView(ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class PlanView(ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = PlanSerializer

class UserPlanView(ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = UserPlanSerializer

class FavoriteMovieView(ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = FavoriteMovieSerializer

    