from rest_framework.response import Response
from .models import Pereval
from .serializer import PerevalSerializer, PerevalDetailSerializer, PerevalCreateSerializer
from rest_framework.views import APIView
from rest_framework import generics, status


class PerevalListView(APIView):
    """ Вывод списка перевалов """

    def get(self, request):
        pereval = Pereval.objects.all()
        serializer = PerevalSerializer(pereval, many=True)
        return Response(serializer.data)


class PerevalCreateView(generics.CreateAPIView):
    queryset = Pereval.objects.all()
    serializer_class = PerevalCreateSerializer


    def create(self, request, *args, **kwargs):
        super(PerevalCreateView, self).create(request, args, kwargs)
        response = {'status': status.HTTP_200_OK,
                    'message': 'null',
                    'result': request.data}
        return Response(response)


class PerevalDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pereval.objects.all()
    serializer_class = PerevalSerializer

    def retrieve(self, request, *args, **kwargs):
        super(PerevalDetailView, self).retrieve(request, args, kwargs)
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data = serializer.data
        response = {'status': status.HTTP_200_OK,
                    'message': 'null',
                    'result': data}
        return Response(response)

    def patch(self, request, *args, **kwargs):
        super(PerevalDetailView, self).patch(request, args, kwargs)
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data = serializer.data
        response = {'status': status.HTTP_200_OK,
                    'message': 'null',
                    'result': data}
        return Response(response)

    def delete(self, request, *args, **kwargs):
        super(PerevalDetailView, self).delete(request, args, kwargs)
        response = {'status': status.HTTP_200_OK,
                    'message': 'null'}
        return Response(response)