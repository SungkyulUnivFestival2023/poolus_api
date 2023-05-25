from django.shortcuts import render
from .serializers import VisitorsSerializer
from rest_framework import generics, mixins, status
from rest_framework.response import Response
from .models import Visitors

class VisitorsView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Visitors.objects.all()
    serializer_class = VisitorsSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
	
    # def post(self, request, *args, **kwargs):
    #     user_ip = self.get_client_ip(request)
    #     data = request.data.copy()
    #     data['ip_address'] = user_ip
    #     serializer = self.get_serializer(data=data)
    #     serializer.is_valid(raise_exception=True)
    #     self.perform_create(serializer)
    #     headers = self.get_success_headers(serializer.data)
    #     return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    def post(self, request, *args, **kwargs):
        user_ip = self.get_client_ip(request)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer, ip_address=user_ip)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    
    def perform_create(self, serializer, ip_address=None):
        serializer.save(ip_address=ip_address)
    # def get_client_ip(self, request):
    #     x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    #     if x_forwarded_for:
    #         ip = x_forwarded_for.split(',')[0]
    #     else:
    #         ip = request.META.get('REMOTE_ADDR')
    #     return ip
    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0].strip()
        else:
            ip = request.META.get('REMOTE_ADDR', '')
        return ip if ip else Response(status=status.HTTP_403_FORBIDDEN)
    # 403에러 뜨면, 이미 작성한 사용자라고 프론트에서 뜨워줘야함
    # 403이 아닌 다른 코드로 할 수 있음