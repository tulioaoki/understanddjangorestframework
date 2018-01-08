from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from api.models import Subscription
from api.serializers import CoreSerializer


class SubsList(APIView):
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