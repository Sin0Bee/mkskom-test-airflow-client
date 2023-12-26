from datetime import datetime

from django.db import models
from django.db.models import QuerySet
from pydantic import BaseModel


class DAGData(BaseModel):
    name: str
    interval: int
    context: str
    pk: int | None = None
    file_path: str | None = None
    create_at: datetime | None = None
    update_at: datetime | None = None
    status: bool | None = None
    on_delete: bool | None = None
    is_active: bool | None = None

    def to_dict(self):
        ...


class MetaDAG(models.Model):
    name = models.CharField(max_length=255)
    file_path = models.TextField(blank=True, null=True)
    context = models.TextField(blank=True, null=True)
    interval = models.PositiveIntegerField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=False)
    on_delete = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"ID: {self.pk} | NAME: {self.name} | SYS_ID: <{id(self)}>"
