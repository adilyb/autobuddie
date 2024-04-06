from django.forms import ModelForm
from product.models import ProductModel

class ProductForm(ModelForm):
    class Meta:
        model = ProductModel
        exclude = ('status','created_on','updated_on', 'uploaded_by')