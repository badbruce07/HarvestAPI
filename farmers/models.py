from django.db import models
from rest_framework.authtoken.models import Token

from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

@receiver(post_save, sender=get_user_model())
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class Farmer(models.Model):

    farmer_idx =  models.CharField(max_length=100, blank=False, default='')
    farmer_id =  models.CharField(max_length=100, blank=False, default='', primary_key=True)
    first_name = models.CharField(max_length=100, null=True, default='')
    last_name = models.CharField(max_length=100, null=True, default='')
    alias = models.CharField(max_length=100, null=True, default='')
    res_address = models.CharField(max_length=200, null=True, default='')
    res_parish = models.CharField(max_length=20, null=True, default='')
    tel_number = models.CharField(max_length=20, null=True, default='')
    cell_number = models.CharField(max_length=20, null=True, default='')
    verified_status = models.CharField(max_length=3, null=True, default='')
    dob = models.DateTimeField()
    agri_activity = models.CharField(max_length=150, null=True, default='')
    owner = models.ForeignKey('auth.User', related_name='farmers', default='1', null=True)
    last_updated = models.DateTimeField(auto_now_add=True, null=True)
#    receipts = models.ForeignKey('Receipt', related_name='receipts', null=True)

    class Meta:
        ordering = ('last_updated',)

    def __unicode__(self):
            return 'Farm Activity: %s' % (self.agri_activity)

class Receipt(models.Model):

    receipt_no =  models.CharField(max_length=100, null=False, default='', primary_key=True)
    rec_range1 = models.CharField(max_length=100, null=True, default='')
    rec_range2 = models.CharField(max_length=100, null=True, default='')
    investigation_status = models.CharField(max_length=100, null=True, default='')
    last_updated = models.DateTimeField(auto_now_add=True, null=True)
    remarks = models.CharField(max_length=200, null=True, default='')
    farmer = models.ForeignKey(Farmer)

    class Meta:
        ordering = ('last_updated',)

    def __unicode__(self):
        return 'Receipt no: %s' % (self.receipt_no)

class Farm(models.Model):

#    farmer_id = models.CharField(max_length=100, null=False, default='')
    farmer_idx = models.CharField(max_length=100, null=False, default='')
    farm_address = models.CharField(max_length=255, default='')
    farm_id = models.CharField(max_length=100, default='', primary_key=True)
    parish = models.CharField(max_length=30, default='')
    district = models.CharField(max_length=50, default='')
    extension = models.CharField(max_length=50, default='')
    farm_size = models.CharField(max_length=50, default='', null=True)
    lat = models.CharField(max_length=50, default='', null=True)
    long = models.CharField(max_length=50, default='', null=True)
    farm_status = models.CharField(max_length=50, default='')
    farmer = models.ForeignKey(Farmer)

    class Meta:
        ordering = ('district',)

    def __unicode__(self):
        return 'Farm Info - Parish %s Address %s Farm Status %s' % (self.parish, self.farm_address, self.farm_status)

class Crop(models.Model):

    crop_name = models.CharField(max_length=100, default='')
    common_name = models.CharField(max_length=30, default='', null=True)
    estimated_vol = models.DecimalField(max_digits=10, default='', null=True, decimal_places=2)
    variety = models.CharField(max_length=50, default='', null=True)
    plant_date = models.CharField(max_length=50, default='', null=True)
    count = models.CharField(max_length=50, default='', null=True)
    area = models.CharField(max_length=50, default='', null=True)
    status = models.CharField(max_length=50, default='', null=True)
    exp_date = models.CharField(max_length=50, default='', null=True)
    farm = models.ForeignKey(Farm)

    class Meta:
        ordering = ('crop_name',)


class Livestock(models.Model):

    livestock_name = models.CharField(max_length=100, default='')
    count = models.CharField(max_length=50, default='', null=True)
    capacity = models.CharField(max_length=50, default='', null=True)
    stage = models.CharField(max_length=50, default='', null=True)
    farm = models.ForeignKey(Farm)

    class Meta:
        ordering = ('livestock_name',)

class Price(models.Model):

    price_id =  models.CharField(max_length=100, null=False, default='', primary_key=True)
    price  = models.DecimalField(max_digits=10, default='', null=True, decimal_places=2)
    public = models.CharField(max_length=10, default='', null=True)
    price_point = models.CharField(max_length=50, default='', null=True)
    parish = models.CharField(max_length=50, default='', null=True)
    commodity = models.CharField(max_length=50, default='', null=True)
    crop_code = models.CharField(max_length=50, default='', null=True)
    units = models.CharField(max_length=50, default='', null=True)
    variety = models.CharField(max_length=50, default='', null=True)
    batch_date = models.DateField(max_length=50, default='', null=True)
    published_on = models.DateField(max_length=50, default='', null=True)
    extension = models.CharField(max_length=50, default='', null=True)

    class Meta:
        ordering = ('published_on',)
