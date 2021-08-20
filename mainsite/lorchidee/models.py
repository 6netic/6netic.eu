from django.db import models


class TimePlan(models.Model):
    """ Fields for TimePlan """

    jour = models.DateField()
    heure = models.CharField(max_length=5, blank=True, null=True)
    patient = models.CharField(max_length=65, blank=True, null=True)
    addrTel = models.CharField(max_length=255, blank=True, null=True)
    cotation = models.CharField(max_length=255, blank=True, null=True)
    assure = models.CharField(max_length=50, blank=True, null=True)
    honoraire = models.CharField(max_length=50, blank=True, null=True)
    finTraitement = models.CharField(max_length=50, blank=True, null=True)
    commentaires = models.CharField(max_length=255, blank=True, null=True)


    class Meta:
        managed = True
        db_table = 'timeplan'
