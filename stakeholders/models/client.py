from django.db import models
import uuid
from django.utils.timezone import now

class Client(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    start = models.DateTimeField(default=now)  # Defaults to the current timestamp
    end = models.DateTimeField(default='infinity')  # PostgreSQL-specific 'infinity'


