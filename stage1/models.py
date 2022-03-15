import textwrap
from django.db import models

class OneThing(models.Model):
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)


class ThingsToLearn(models.Model):
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)


class ImproveHabits(models.Model):
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)


class SocialLife(models.Model):
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)


class LeisureActivity(models.Model):
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)


class FamilyLife(models.Model):
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)


class Career(models.Model):
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)


class Qualities(models.Model):
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)


class IdealFuture(models.Model):
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)


class FutureToAvoid(models.Model):
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

