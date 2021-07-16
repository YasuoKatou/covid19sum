from django.db import models

# Create your models here.
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.

class DaillyPatients(models.Model):
    target_date = models.DateField()
    area_code = models.CharField(max_length=10)
    patients = models.BigIntegerField()

    weekDayConv = [2, 3, 4, 5, 6, 7, 1]

    class Meta:
        db_table = 'dailly_patients'
        unique_together = (('target_date', 'area_code'),)

    def getLastTargetDate():
        d = DaillyPatients.objects.all().aggregate(models.Max('target_date'))
        d1 = d['target_date__max']
        return d1, DaillyPatients.weekDayConv[d1.weekday()]

class Summary(models.Model):
    last_update = models.DateField()
    area_code = models.CharField(max_length=10)
    total = models.BigIntegerField()

    class Meta:
        db_table = 'summary'
        unique_together = (('last_update', 'area_code'),)
