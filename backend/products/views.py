from rest_framework import generics, authentication,mixins, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
# from django.http import Http404
from django.shortcuts import get_object_or_404

from .models import Product
from products.serializers import ProductSerializer

class ProductListCreateApiView(generics.ListCreateAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    authentication_classes=[authentication.SessionAuthentication]
    permission_classes=[permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        title=serializer.validated_data.get('title')
        content=serializer .validated_data.get('content')

        if content is None:
            content=title
        serializer.save(content=content)



class ProductDetailApiView(generics.RetrieveAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    lookup_field='pk'


class ProductUpdateApiView(generics.UpdateAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    lookup_field='pk'

    def perform_update(self, serializer):
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response({
            "error": "invalid data"
        })

class ProductDestroyApiView(generics.DestroyAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    lookup_field='pk'


    def perform_destroy(self, instance):
        instance.delete()
        return Response({
            "success": f"deleted object <{instance.title}>"
        }
        )
    


class ProductMixinView(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    generics.GenericAPIView
    ):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer

    def get(self, request, *args, **kwargs):
        pk= kwargs.get('pk')
        if pk:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)