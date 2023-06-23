import uuid

from django.db import models
from django.utils import timezone
from django_extensions.db.models import (
    TimeStampedModel,
    ActivatorModel,
    TitleSlugDescriptionModel
)


class Model(models.Model):
    Id = models.UUIDField(primary_key=True, db_index = True,default=uuid.uuid4, editable=False)
    
    class Meta:
        abstract = True


class DateModel(models.Model):
	DateCreatedAt = models.DateTimeField(editable=False,default=timezone.now)

	class Meta:
		abstract = True
		ordering = ['-DateCreatedAt']

class CustomModel(Model,TitleSlugDescriptionModel,TimeStampedModel,ActivatorModel):
	class Meta:
		abstract = True