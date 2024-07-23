from rest_framework import generics
from .models import Cart, CartItem
from .serializers import CartSerializer, CartItemSerializer

class CartItemListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = CartItemSerializer
    queryset = CartItem.objects.all()

    def perform_create(self, serializer):
        cart = self.request.user.cart  # Assuming the user has a `cart` attribute
        serializer.save(cart=cart)

        
class CartItemRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CartItemSerializer
    queryset = CartItem.objects.all()

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)

        
class CartListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = CartSerializer
    queryset = Cart.objects.all()

    def perform_create(self, serializer):
        serializer.save(session_id=self.request.session.session_key)

class CartRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CartSerializer
    queryset = Cart.objects.all()

    def get_queryset(self):
        return self.queryset

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def perform_destroy(self, instance):
        instance.delete()




