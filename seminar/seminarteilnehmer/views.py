from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from seminarteilnehmer.models import Teilnehmer
from .serializers import TeilnehmerSerializer
# Create your views here.

@api_view(['GET'])
def getAll(request):
    teilnehmer = Teilnehmer.objects.all()
    serializer = TeilnehmerSerializer(teilnehmer, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getOne(request, teilnehmer_id):
    teilnehmer = Teilnehmer.objects.filter(id=teilnehmer_id)
    serializer = TeilnehmerSerializer(teilnehmer, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def post(request):
    serializer = TeilnehmerSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['PUT'])
def put(request, teilnehmer_id):
    teilnehmer = Teilnehmer.objects.filter(id = teilnehmer_id).first()
    if teilnehmer:
        serializer = TeilnehmerSerializer(teilnehmer,data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    serializer = TeilnehmerSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)

    

@api_view(['PATCH'])
def patch(request, teilnehmer_id):
    teilnehmer = Teilnehmer.objects.filter(id = teilnehmer_id).first()
    if teilnehmer:
        serializer = TeilnehmerSerializer(teilnehmer,data=request.data ,partial=True)
        if serializer.is_valid() and request.data:
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        message = {'message': 'No parameters delivered...'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)
    message = {'message': 'there is no Teilnehmer with this id...'}
    return Response(message, status=status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
def delete(request, teilnehmer_id):
    teilnehmer = Teilnehmer.objects.filter(id=teilnehmer_id)
    if teilnehmer:
        teilnehmer = Teilnehmer.objects.filter(id=teilnehmer_id).delete()
        message = {'message': 'specified Teilnehmer was deleted'}
        return Response(message, status=status.HTTP_200_OK)
    message = {'message': 'there is no Teilnehmer with this id...'}
    return Response(message, status=status.HTTP_404_NOT_FOUND)
