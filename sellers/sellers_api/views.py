from rest_framework import viewsets
from .models import Seller
from .serializers import SellerSerializer


# Create your views here.
class SellerApi(viewsets.ModelViewSet):
    queryset = Seller.objects.all().order_by('created_at')
    serializer_class = SellerSerializer
