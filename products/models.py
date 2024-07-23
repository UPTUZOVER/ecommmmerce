from django.db import models
from django.utils.translation import gettext_lazy as _  # Lokalizatsiya uchun _ funksiyasini import qilamiz

from parler.models import TranslatableModel, TranslatedFields
from categories.models import Category






class Product(TranslatableModel):
    translations = TranslatedFields(
        title=models.CharField(max_length=200, unique=True, verbose_name=_("Mahsul nomi")),
        description=models.TextField(blank=True, verbose_name=_("Mahsul tavsifi")),
    )

    categories = models.ForeignKey(Category, verbose_name=_("Turkum"), on_delete=models.CASCADE)
    image_main = models.ImageField(upload_to='images/', verbose_name=_("Asosiy rasmi"), null=True, blank=True)
    count = models.IntegerField(null=True, verbose_name=_("Maxulot miqdori"))
    price = models.DecimalField(verbose_name=_("Maxulot narxi"), max_digits=10, decimal_places=2,null=True, default=0)
    discount = models.IntegerField(verbose_name=_("chegirmna"), null=True, blank=True)
    true_price = models.DecimalField(verbose_name=_("oxirgi narx"), max_digits=10, decimal_places=2, blank=True, null=True)
    img1 = models.ImageField(upload_to='images/', verbose_name=_("Birinchi rasm"), null=True, blank=True)
    img2 = models.ImageField(upload_to='images/', verbose_name=_("Ikkinchi rasm"), null=True, blank=True)
    img3 = models.ImageField(upload_to='images/', verbose_name=_("Uchinchi rasm"), null=True, blank=True)
    updated_on = models.DateTimeField(auto_now=True, verbose_name=_("Yangilangan sana"))
    created_on = models.DateTimeField(auto_now_add=True, verbose_name=_("Yaratilgan sana"))

    def save(self, *args, **kwargs):
        if self.discount is not None and self.price is not None:
            self.true_price = self.price - (self.price * self.discount / 100)
        super().save(*args, **kwargs)
            
    def cat(self):
        return self.categories.title

    class Meta:
        ordering = ['-created_on'] 
        verbose_name = _("Product") 
        verbose_name_plural = _("Products")  

    def __str__(self):
        return self.title


































