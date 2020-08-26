from django.db import models
import uuid


# Create your models here.
class Seller(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    company_name = models.TextField(max_length=128)
    brand = models.TextField(max_length=128)
    status = models.TextField()
    portfolio_size = models.IntegerField()
    origin = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    blocked = models.BooleanField()
    blocked_reason = models.TextField()
