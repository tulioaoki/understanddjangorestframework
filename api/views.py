from django.http import Http404
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from api.models import Subscription
from api.serializers import CoreSerializer
from api.serializers import UserSerializer
from api.permissions import IsOwnerOrReadOnly
from rest_framework import permissions
from django.contrib.auth.models import User


class SubsList(APIView):

    http_method_names = ['get', 'post',]
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get(self,request, format=None):
        objects = Subscription.objects.all()
        serializer = CoreSerializer(objects, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CoreSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SubsDetail(APIView):
    http_method_names = ['get','put','delete']

    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)

    def get_object(self,pk):
        try:
            return Subscription.objects.get(pk=pk)
        except Subscription.DoesNotEXist:
            raise Http404
    def get(self,request,pk, format=None):
        objects = self.get_object(pk)
        serializer = CoreSerializer(objects)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        core = self.get_object(pk)
        serializer = CoreSerializer(core, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk,format=None):
        to_be_deleted = self.get_object(pk)
        to_be_deleted.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class UserList(generics.ListAPIView):
    http_method_names = ['get',]
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):    http_method_names = ['get',]

    queryset = User.objects.all()
    serializer_class = UserSerializer