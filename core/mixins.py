# coding: utf-8
from django.db import models


class TimestampMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    @property
    def when(self):
        return self.created_at.strftime('%d/%m/%Y')


class SoftDeleteMixin(models.Model):

    class Meta:
        abstract = True

    is_visible = models.BooleanField(default=True)


class DefaultModelMixin(TimestampMixin, SoftDeleteMixin):

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        # self.clean()
        self.full_clean()
        super(DefaultModelMixin, self).save(*args, **kwargs)