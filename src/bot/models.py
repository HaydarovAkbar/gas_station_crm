from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.timezone import now

LANGUAGES = (
    ('uz', _('O\'zbek')),
    ('ru', _('Русский')),
    ('en', _('English')),
)


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


class FuelColumn(models.Model):
    title = models.CharField(max_length=255, verbose_name=_("To'liq nomi"))
    attr = models.CharField(max_length=255, null=True, blank=True, verbose_name=_("Qisqa nomi"))

    state = models.ForeignKey(State, on_delete=models.SET_NULL, null=True, verbose_name=_("Xolat"))

    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Yaratilgan sana"))
    updated_at = models.DateTimeField(auto_now=True, null=True, verbose_name=_("O'zgartirilgan sana"))

    organ = models.ForeignKey(Organization, on_delete=models.SET_NULL, null=True, verbose_name=_("Tashkilot"))

    objects = models.Manager()

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.title = self.title.upper() if self.title else self.title
        self.updated_at = now()
        super(FuelColumn, self).save(*args, **kwargs)
        return self

    class Meta:
        verbose_name_plural = _('Yoqilg\'i ustunlari')
        verbose_name = _('Yoqilg\'i ustuni')
        db_table = 'fuel_column'


class FuelStorage(models.Model):
    size = models.IntegerField(verbose_name=_("Hajmi [litr]"))
    input_price = models.FloatField(verbose_name=_("Kirim narxi"))
    output_price = models.FloatField(verbose_name=_("Chiqim narxi"))
    organization = models.ForeignKey(Organization, on_delete=models.SET_NULL, null=True, verbose_name=_("Tashkilot"))
    fuel_type = models.ForeignKey(FuelType, on_delete=models.SET_NULL, null=True, verbose_name=_("Yoqilg'i turi"))

    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Yaratilgan sana"))
    updated_at = models.DateTimeField(auto_now=True, null=True, verbose_name=_("O'zgartirilgan sana"))

    objects = models.Manager()

    def __str__(self):
        return str(self.size)

    def save(self, *args, **kwargs):
        self.updated_at = now()
        super(FuelStorage, self).save(*args, **kwargs)
        return self

    class Meta:
        verbose_name_plural = _('Yoqilg\'i ombori')
        verbose_name = _('Yoqilg\'i ombori')
        db_table = 'fuel_storage'


class Fuel(models.Model):
    day = models.DateField(verbose_name=_("Kun"))
    fuel_type = models.ForeignKey(FuelType, on_delete=models.SET_NULL, null=True, verbose_name=_("Yoqilg'i turi"))

    purchase = models.FloatField(verbose_name=_("Xarid"), null=True, blank=True)
    sale = models.FloatField(verbose_name=_("Sotish"), null=True, blank=True)
    balance = models.FloatField(verbose_name=_("Qoldiq"), null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Yaratilgan sana"))
    updated_at = models.DateTimeField(auto_now=True, null=True, verbose_name=_("O'zgartirilgan sana"))

    objects = models.Manager()

    def __str__(self):
        return str(self.day)

    def save(self, *args, **kwargs):
        self.updated_at = now()
        super(Fuel, self).save(*args, **kwargs)
        return self

    class Meta:
        verbose_name_plural = _('Yoqilg\'i')
        verbose_name = _('Yoqilg\'i')
        db_table = 'fuel'
        indexes = [
            models.Index(fields=['day', 'fuel_type']),
        ]


class FuelPrice(models.Model):
    day = models.ForeignKey(Fuel, on_delete=models.SET_NULL, null=True, verbose_name=_("Kun"))
    fuel_type = models.ForeignKey(FuelType, on_delete=models.SET_NULL, null=True, verbose_name=_("Yoqilg'i turi"))
    payment_type = models.ForeignKey(PaymentType, on_delete=models.SET_NULL, null=True, verbose_name=_("To'lov turi"))
    size = models.FloatField(verbose_name=_("Hajmi [litr]"))

    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Yaratilgan sana"))
    updated_at = models.DateTimeField(auto_now=True, null=True, verbose_name=_("O'zgartirilgan sana"))

    objects = models.Manager()

    def __str__(self):
        return str(self.day)

    def save(self, *args, **kwargs):
        self.updated_at = now()
        super(FuelPrice, self).save(*args, **kwargs)
        return self

    class Meta:
        verbose_name_plural = _('Yoqilg\'i narxi')
        verbose_name = _('Yoqilg\'i narxi')
        db_table = 'fuel_price'


class FuelColumnPointer(models.Model):
    fuel_column = models.ForeignKey(FuelColumn, on_delete=models.SET_NULL, null=True, verbose_name=_("Yoqilg'i ustuni"))
    day = models.ForeignKey(Fuel, on_delete=models.SET_NULL, null=True, verbose_name=_("Kun"))
    size_first = models.FloatField(verbose_name=_("Hajmi kun boshida [litr]"), null=True, blank=True)
    size_last = models.FloatField(verbose_name=_("Hajmi kun oxirida [litr]"), null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Yaratilgan sana"))
    updated_at = models.DateTimeField(auto_now=True, null=True, verbose_name=_("O'zgartirilgan sana"))

    objects = models.Manager()

    def __str__(self):
        return str(self.size_first)

    def save(self, *args, **kwargs):
        self.updated_at = now()
        super(FuelColumnPointer, self).save(*args, **kwargs)
        return self

    class Meta:
        verbose_name_plural = _('Yoqilg\'i ustuni ko\'rsatgichlari')
        verbose_name = _('Yoqilg\'i ustuni ko\'rsatgichlari')
        db_table = 'fuel_column_pointer'


class UserTypes(models.Model):
    title = models.CharField(max_length=255, verbose_name=_("To'liq nomi"))

    state = models.ForeignKey(State, on_delete=models.SET_NULL, null=True, verbose_name=_("Xolat"))

    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Yaratilgan sana"))

    objects = models.Manager()

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.title = self.title.upper() if self.title else self.title
        self.updated_at = now()
        super(UserTypes, self).save(*args, **kwargs)
        return self

    class Meta:
        verbose_name_plural = _('Foydalanuvchi turlari')
        verbose_name = _('Foydalanuvchi turi')
        db_table = 'user_types'


class User(models.Model):
    username = models.CharField(max_length=255, verbose_name=_("Foydalanuvchi nomi"))
    chat_id = models.BigIntegerField(verbose_name=_("Chat ID"))
    fullname = models.CharField(max_length=255, null=True, blank=True, verbose_name=_("To'liq ismi"))
    state = models.ForeignKey(State, on_delete=models.SET_NULL, null=True, verbose_name=_("Xolat"))
    language = models.CharField(max_length=2, default='uz', verbose_name=_("Til"), choices=LANGUAGES)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Yaratilgan sana"))
    updated_at = models.DateTimeField(auto_now=True, null=True, verbose_name=_("O'zgartirilgan sana"))
    roles = models.ManyToManyField(UserTypes, verbose_name=_("Foydalanuvchi turlari"), related_name='user_roles')

    phone = models.CharField(max_length=255, null=True, blank=True, verbose_name=_("Telefon"))
    position = models.CharField(max_length=255, null=True, blank=True, verbose_name=_("Lavozimi"))

    organization = models.ManyToManyField(Organization, verbose_name=_("Tashkilotlar"),
                                          related_name='user_organization')

    objects = models.Manager()

    def __str__(self):
        return self.username

    def get_fullname(self):
        return self.fullname + ' - ' + str(self.chat_id)

    def get_user(self):
        try:
            return self.fullname + ' - ' + str(self.created_at.strftime('%d-%m-%Y %H:%M'))
        except:
            return str(self.chat_id) + ' - ' + str(self.created_at.strftime('%d-%m-%Y %H:%M'))

    def save(self, *args, **kwargs):
        self.updated_at = now()
        super(User, self).save(*args, **kwargs)
        return self

    class Meta:
        verbose_name_plural = _('Foydalanuvchilar')
        verbose_name = _('Foydalanuvchi')
        db_table = 'user'


class SaleFuel(models.Model):
    day = models.DateField(verbose_name=_("Kun"))
    fuel_type = models.ForeignKey(FuelType, on_delete=models.SET_NULL, null=True, verbose_name=_("Yoqilg'i turi"))
    size = models.FloatField(verbose_name=_("Hajmi [litr]"), null=True, blank=True)
    payment_type = models.ForeignKey(PaymentType, on_delete=models.SET_NULL, null=True, verbose_name=_("To'lov turi"))
    price = models.FloatField(verbose_name=_("Narxi"), null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Yaratilgan sana"))
    updated_at = models.DateTimeField(auto_now=True, null=True, verbose_name=_("O'zgartirilgan sana"))

    objects = models.Manager()

    def __str__(self):
        return str(self.day)

    def save(self, *args, **kwargs):
        self.updated_at = now()
        super(SaleFuel, self).save(*args, **kwargs)
        return self

    class Meta:
        verbose_name_plural = _('Sotilgan yoqilg\'i')
        verbose_name = _('Sotilgan yoqilg\'i')
        db_table = 'sale_fuel'
        indexes = [
            models.Index(fields=['day', 'fuel_type', 'payment_type']),
        ]