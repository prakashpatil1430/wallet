from django.db import models
from django.contrib.auth.models import User

import uuid
from django.db import models
  
class Wallet(models.Model):
    customer = models.CharField(max_length=50)
    id = models.UUIDField(primary_key = True,default = uuid.uuid4,editable = False)
    owned_by = models.UUIDField(default = uuid.uuid4,editable = False)
    status = models.BooleanField(default=False)
    enabled_at =models.DateTimeField(auto_now_add = True)
    balance = models.IntegerField()
    



    # other fields

