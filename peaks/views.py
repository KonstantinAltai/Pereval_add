from rest_framework.response import Response
from .models import Pereval
from .serializer import PerevalSerializer, PerevalDetailSerializer
from rest_framework.views import APIView


class PerevalListView(APIView):
    """ Вывод списка перевалов """

    def get(self, request):
        pereval = Pereval.objects.all()
        serializer = PerevalSerializer(pereval, many=True)
        return Response(serializer.data)


class PerevalDetailView(APIView):
    """ Вывод сведений о перевале"""

    def get(self, request, pk):
        pereval = Pereval.objects.get(id=pk)
        serializer = PerevalDetailSerializer(pereval)
        return Response(serializer.data)


class PerevalCreateView(APIView):
    '''Добавление сведений о перевале'''

    def post(self, request):
        serializer = PerevalDetailSerializer(data=request.data)
        if serializer.is_valid():
            try:
                serializer.save()
                return Response(status=200)
            except ValueError:
                return Response(status=201)