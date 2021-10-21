from django.db import models
from scanner.consts import Consts
from django.db import models
import uuid


class Scan(models.Model):

    # Status choices 
    SCAN_STATUS_CHOICES = [
        (Consts.ACCEPTED,'Accepted'),
        (Consts.RUNNING,'Running'),
        (Consts.ERROR,'Error'),
        (Consts.COMPLETE,'Complete'),
        (Consts.NOT_FOUND,'Not-Found')
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    status = models.CharField(max_length=15, choices=SCAN_STATUS_CHOICES, default=Consts.ACCEPTED)
    creation_time = models.DateTimeField(auto_now_add=True)
