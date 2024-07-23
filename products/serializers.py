from parler_rest.serializers import TranslatableModelSerializer
from parler_rest.fields import TranslatedFieldsField
from products.models import Product
from categories.models import Category
from rest_framework.serializers import ModelSerializer


class ProductSerializer(TranslatableModelSerializer, ModelSerializer):
    translations = TranslatedFieldsField(shared_model=Product)

    class Meta:
        model = Product
        fields = ('id', "title", 'categories', "cat", 'translations', 'image_main', 'count', 'price', "discount", 'true_price', 'img1', 'img2', 'img3', 'updated_on')
        ref_name = 'ProductSerializer'

    def get_discount_percent(self, instance):
        if instance.discount:
            return int((instance.discount / instance.price) * 100)
        return 0

    def to_representation(self, instance):
        data = super().to_representation(instance)
        if instance.discount is not None:
            data['price'] = instance.true_price
        return data

    def get_categories_display(self, instance):
        return ", ".join([str(cat.title) for cat in instance.categories.all()])
    
class CategorySerializer(TranslatableModelSerializer):
    translations = TranslatedFieldsField(shared_model=Category)  # Kategoriya tarjimalarini ko'rsatish uchun
    prod_obj = ProductSerializer(source='product_set', many=True, read_only=True)  # ProductSerializer ni ko'rsatish uchun

    class Meta:
        model = Category
        fields = ('id', 'title', 'translations', 'prod_obj')


