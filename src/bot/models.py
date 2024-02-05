from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.timezone import now


class State(models.Model):
    title = models.CharField(max_length=255, verbose_name=_("to'liq nomi"))
    attr = models.CharField(max_length=255, null=True, blank=True, verbose_name=_("qisqacha nomi"))

    objects = models.Manager()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = _('Xolatlar')
        verbose_name = _('Xolat')
        db_table = 'state'


class Organization(models.Model):
    title = models.CharField(max_length=255, verbose_name=_("To'liq nomi"))
    attr = models.CharField(max_length=255, null=True, blank=True, verbose_name=_("Qisqa nomi"))
    address = models.CharField(max_length=255, null=True, blank=True, verbose_name=_("Manzil"))
    phone = models.CharField(max_length=255, null=True, blank=True, verbose_name=_("Telefon"))
    description = models.TextField(null=True, blank=True, verbose_name=_("Tavsif"))
    leader = models.CharField(max_length=255, null=True, blank=True, verbose_name=_("Rahbar"))

    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Yaratilgan sana"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Yangilangan sana"))

    objects = models.Manager()

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.title = self.title.upper() if self.title else self.title
        self.attr = self.attr.upper() if self.attr else self.attr
        self.updated_at = now()
        super(Organization, self).save(*args, **kwargs)
        return self

    class Meta:
        verbose_name_plural = _('Tashkilotlar')
        verbose_name = _('Tashkilot')
        db_table = 'organization'

class PaymentType(models.Model):
    title = models.CharField(max_length=255, verbose_name=_("To'liq nomi"))
    attr = models.CharField(max_length=255, null=True, blank=True, verbose_name=_("Qisqa nomi"))

    state = models.ForeignKey(State, on_delete=models.SET_NULL, null=True, verbose_name=_("Xolat"))

    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Yaratilgan sana"))
    updated_at = models.DateTimeField(auto_now=True, null=True, verbose_name=_("O'zgartirilgan sana"))

    objects = models.Manager()

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.title = self.title.upper() if self.title else self.title
        self.updated_at = now()
        super(PaymentType, self).save(*args, **kwargs)
        return self

    class Meta:
        verbose_name_plural = _('To\'lov turlari')
        verbose_name = _('To\'lov turi')
        db_table = 'payment_type'


class FuelType(models.Model):
    title = models.CharField(max_length=255, verbose_name=_("To'liq nomi"))
    attr = models.CharField(max_length=255, null=True, blank=True, verbose_name=_("Qisqa nomi"))

    state = models.ForeignKey(State, on_delete=models.SET_NULL, null=True, verbose_name=_("Xolat"))

    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Yaratilgan sana"))
    updated_at = models.DateTimeField(auto_now=True, null=True, verbose_name=_("O'zgartirilgan sana"))

    objects = models.Manager()

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.title = self.title.upper() if self.title else self.title
        self.updated_at = now()
        super(FuelType, self).save(*args, **kwargs)
        return self

    class Meta:
        verbose_name_plural = _('Yoqilg\'i turlari')
        verbose_name = _('Yoqilg\'i turi')
        db_table = 'fuel_type'


# class Fuel(models.Model):
#     title = models.CharField(max_length=255, verbose_name=_("Yoqilg'i nomi"))
#     fuel_type = models.ForeignKey(FuelType, on_delete=models.SET_NULL, null=True, verbose_name=_("Yoqilg'i turi"))
#
#     state = models.ForeignKey(State, on_delete=models.SET_NULL, null=True, verbose_name=_("Xolat"))
#
#     created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Yaratilgan sana"))
#     updated_at = models.DateTimeField(auto_now=True, null=True, verbose_name=_("O'zgartirilgan sana"))
#
#     objects = models.Manager()
#
#     def __str__(self):
#         return self.title
#
#     def save(self, *args, **kwargs):
#         self.title = self.title.upper() if self.title else self.title
#         self.updated_at = now()
#         super(Fuel, self).save(*args, **kwargs)
#         return self
#
#     class Meta:
#         verbose_name_plural = _('Yoqilg\'i')
#         verbose_name = _('Yoqilg\'i')
#         db_table = 'fuel'
