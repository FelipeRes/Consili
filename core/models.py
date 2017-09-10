from django.contrib.auth import get_user_model
from django.utils.translation import ugettext_lazy as _
from django.db import models
from djmoney.models.fields import MoneyField
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from rest_framework.authtoken.models import Token

from core.mixins import DefaultModelMixin

User = get_user_model()


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class Profile(DefaultModelMixin):

    user = models.ForeignKey(User, verbose_name=_('User'), related_name='profile')

    @property
    def username(self):
        return self.user.username

    @property
    def full_name(self):
        return self.user.first_name + " " + self.user.last_name

    @property
    def email(self):
        return self.user.email

    def is_owner(self, request):
        return self.user == request.user

    def __str__(self):
        return self.username + " at " + self.email


class Category(DefaultModelMixin):

    name = models.CharField(max_length=64)
    color = models.CharField(max_length=7)
    created_by = models.ForeignKey(Profile, related_name="categories_created")

    def is_owner(self, request):
        return self.created_by.user == request.user

    def __str__(self):
        return self.name


class Task(DefaultModelMixin):

    title = models.CharField(max_length=128)
    description = models.CharField(max_length=256)
    starting_at = models.DateTimeField()
    ending_at = models.DateTimeField()
    created_by = models.ForeignKey(Profile, related_name="tasks_created")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="tasks")
    members = models.ManyToManyField(Profile, related_name="tasks")

    def is_owner(self, request):
        return self.created_by.user == request.user

    def __str__(self):
        return self.title


class Purchase(DefaultModelMixin):

    title = models.CharField(max_length=128)
    description = models.CharField(max_length=256)
    price = MoneyField(verbose_name=_('Price'), max_digits=8, decimal_places=2,
                       default_currency='BRL', editable=True, null=True, blank=False)
    created_by = models.ForeignKey(Profile, related_name="purchases_created")
    tasks = models.ManyToManyField(Task, related_name="purchases")

    def is_owner(self, request):
        return self.created_by.user == request.user

    def __str__(self):
        return self.title


class Risk(DefaultModelMixin):

    PROBABILITY_CHOICES = (
        (0,  _("Impossible")),
        (20, _("A bit likely")),
        (40, _("Likely")),
        (60, _("Very likely")),
        (80, _("Almost certain")),
    )

    title = models.CharField(max_length=128)
    description = models.CharField(max_length=256)
    probability = models.IntegerField(choices=PROBABILITY_CHOICES, default=0)
    tasks = models.ManyToManyField(Task, related_name="risks")
    created_by = models.ForeignKey(Profile, related_name="risks_created")

    def is_owner(self, request):
        return self.created_by.user == request.user

    def __str__(self):
        return self.title + " - Chance of happening: %d%%" % self.probability

