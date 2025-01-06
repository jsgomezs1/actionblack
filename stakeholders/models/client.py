from django.db import models
import uuid
from django.utils.timezone import now

class Client(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    star = models.DateTimeField(auto_now_add=True)  # Defaults to the current timestamp
    end = models.DateTimeField(default='infinity')  # PostgreSQL-specific 'infinity'

"""
ALTER TABLE public.stakeholders_client
ALTER COLUMN id SET DEFAULT gen_random_uuid();

ALTER TABLE public.stakeholders_client
ALTER COLUMN "start" SET DEFAULT now();


ALTER TABLE public.stakeholders_client
ALTER COLUMN "end" SET DEFAULT 'infinity'::timestamptz;

"""


