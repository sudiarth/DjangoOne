from django.db import models
from apps.auth_user.models import User

class Movie(models.Model):
    
    api_id = models.IntegerField(unique=True)
    url = models.CharField(max_length=64, unique=True)
    name = models.CharField(max_length=64)
    image = models.CharField(max_length=128, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def parse_json(self, data):
        self.api_id = data['show']['id']
        self.url = data['show']['url']
        self.name = data['show']['name']
        try:
            self.image = data['show']['image']['medium']
        except:
            self.image = None

class Like(models.Model):
    
    user = models.ForeignKey(User, related_name='users_liked', on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, related_name='movies_liked', on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)