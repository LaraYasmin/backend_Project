from django.db import models
from uuid import uuid4
from django.db.models.fields import SlugField

class Category(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, unique=True) 

    class Meta:
        verbose_name_plural = 'categories' 
    def __str__(self):
        return self.name
        
class Product(models.Model):
    category = models.ForeignKey(Category, related_name='product', on_delete=models.CASCADE) #relacionado a qual categoria está esse produto
    title = models.CharField(max_length=40) #título do produto
    description = models.TextField(blank=True, max_length=255) #descrição do produto
    id_product = models.UUIDField(primary_key=True, default=uuid4, editable=False ) #id do produto
    image = models.ImageField(upload_to='images/') #imagem do produto (1 imagem por agora)
    price = models.DecimalField(max_digits=4, decimal_places=2) #preço do produto, max 4 digitos, e 2 espaços de casas decimais
    slug = models.SlugField(max_length=255) #slug do endereço do produto
    in_stock = models.BooleanField(default=True) #diz se está em estoque

    class Meta:
        verbose_name_plural = 'Products'
    
    def __str__(self):
        return self.title

  

