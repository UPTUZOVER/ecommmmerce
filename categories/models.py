
from django.db import models  # Django modellarini import qilamiz
from django.utils.translation import gettext_lazy as _  # Lokalizatsiya uchun _ funksiyasini import qilamiz
from parler.models import TranslatableModel, TranslatedFields  # TranslatableModel va TranslatedFieldsni import qilamiz
import uuid
from django.contrib.auth import get_user_model
from django.dispatch import receiver
from django.db.models.signals import post_save
 
class Category(TranslatableModel):
    # Kategoriya ma'lumotlarini tarjima qilish uchun maydonlar
    translations = TranslatedFields(
        title=models.CharField(max_length=150, verbose_name=_("Kategoriya")),
    )
    updated_on = models.DateTimeField(auto_now=True)  # So'nggi yangilanish sanasi
    created_on = models.DateTimeField(auto_now_add=True)  # Yaratilgan sana

    def __str__(self):
        return self.title  # Tarjima qilingan kategoriya nomi

    class Meta:
        verbose_name = _("Kategoriya")  # Kategoriya
        verbose_name_plural = _("Kategoriyalar")  # Kategoriyalar
