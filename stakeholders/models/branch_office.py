import uuid
from django.db import models
from django.utils.timezone import now
import datetime

class BranchOffice(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    start = models.DateTimeField(auto_now_add=True)
    end = models.DateTimeField(default=datetime.datetime.max)  # Python-compatible representation
