# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Listing(models.Model):

    #__Listing_FIELDS__
    id = models.IntegerField(null=True, blank=True)
    link = models.CharField(max_length=255, null=True, blank=True)

    #__Listing_FIELDS__END

    class Meta:
        verbose_name        = _("Listing")
        verbose_name_plural = _("Listing")


class Game(models.Model):

    #__Game_FIELDS__
    title = models.CharField(max_length=255, null=True, blank=True)
    id = models.IntegerField(null=True, blank=True)
    join_link = models.CharField(max_length=255, null=True, blank=True)
    game_type = models.CharField(max_length=255, null=True, blank=True)

    #__Game_FIELDS__END

    class Meta:
        verbose_name        = _("Game")
        verbose_name_plural = _("Game")



#__MODELS__END
