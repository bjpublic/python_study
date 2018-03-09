# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Play(models.Model):
    original = models.CharField(max_length=30, blank=True, null=True)
    encrypted = models.CharField(max_length=200, blank=True, null=True)
    decrypted = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'play'


class Supermarket(models.Model):
    itemno = models.IntegerField(db_column='Itemno', blank=True, null=True)  # Field name made lowercase.
    category = models.CharField(db_column='Category', max_length=20, blank=True, null=True)  # Field name made lowercase.
    foodname = models.CharField(db_column='FoodName', max_length=30, blank=True, null=True)  # Field name made lowercase.
    company = models.CharField(db_column='Company', max_length=20, blank=True, null=True)  # Field name made lowercase.
    price = models.IntegerField(db_column='Price', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'supermarket'
