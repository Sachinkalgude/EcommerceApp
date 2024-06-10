from django.db import models
from authentication.models import Users
import uuid
# Create your models here.

class BaseModel(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4,primary_key=True,editable=False)
    created_at = models.DateTimeField(auto_now=True)
    updtaed_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        abstract = True
    
class Categories(BaseModel):
    name = models.CharField(max_length=24,unique=True)
    
    def __str__(self):
        return f"{self.name}-{self.uuid}"
    
class Product(BaseModel):
    categories = models.ForeignKey(Categories,on_delete=models.CASCADE)
    name = models.CharField(max_length=26)
    image = models.ImageField(upload_to="product_image")
    discription = models.TextField()
    product_price = models.IntegerField(default=0)
    product_demo_price = models.IntegerField(default=0)
    
    
    def __str__(self):
        return f"{self.name} - {self.categories} - {self.image}"

class Cart(BaseModel):
    user = models.OneToOneField(Users,on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.user.first_name}"
    
class CartItems(BaseModel):
    cart = models.ForeignKey(Cart,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    
    def __str__(self):
        return f"{self.cart}-{self.quantity}-{self.product.name}"
    
    def total_cost(self):
        return self.product.product_price * self.quantity
