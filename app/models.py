from django.db import models
import uuid


class Game(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, db_index=True, unique=True)
    is_active = models.BooleanField(default=True)
    created_timestamp = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100)
    url = models.URLField()
    author = models.CharField()
    publised_date = models.DateField()

