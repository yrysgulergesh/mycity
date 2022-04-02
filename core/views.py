from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response


from .serializers import ProprosalListSerializer, ProprosalSerializer, ProprosalCreateSerializer, ProprosalSerializer
from .models import Proprosal


class ProprosalListAPIView(APIView):
    def get(self, request, *args, **kwargs):
        proposals = Proprosal.objects.all()
        proprosals_json = ProprosalListSerializer(proposals, many=True)
        return Response(data=proprosals_json.data)


class ProprosalCreateAPIView(APIView):
    def post(self, request, *args, **kwargs):
        data = request.POST
        serializer = ProprosalCreateSerializer(data=data)
        if serializer.is_valid():
            proprosal = serializer.save()
            json_data = ProprosalSerializer(instance=proprosal)

            return Response(json_data.data, 201)
        return Response(
            data={
                'message': 'Data not valid',
                'errors': serializer.errors
            }, 
            status=400
        )

class ProprosalRetrieveAPIView(RetrieveAPIView):
        queryset = Proprosal.objects.all()
        serializer_class = ProprosalSerializer
