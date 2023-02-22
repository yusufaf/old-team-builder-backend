from django.db import models
import uuid

# Create your models here.

class Team(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, 
                            editable=True,
                            unique=True,
                            )
    name = models.CharField(max_length=100)
    description = models.TextField()
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    players = models.JSONField(default=dict)
    
    def _str_(self):
        return self.name
    
