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

    # def post(self,request, *args, **kwargs):
    #     pass

class PerevalDetailView(APIView):
    """ Вывод сведений о перевале"""
    def get(self, request, pk):
        pereval=Pereval.objects.get(id=pk)
        serializer = PerevalDetailSerializer(pereval)
        return Response(serializer.data)
