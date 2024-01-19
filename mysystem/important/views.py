from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model
from django.http import HttpResponse
from .serializers import UserSerializer, profile_info
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import status
from rest_framework.views import APIView
from .models import UserProfile


class UserViewset(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated,]
    serializer_class = UserSerializer
    queryset = get_user_model().objects.all()


class UserProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get_code(request, *args, **kwargs):
        code = str(kwargs.get('ref_code'))
        try:
            profile = UserProfile.objects.get(code=code)
            request.session['ref_profile'] = profile.id
            print('id', profile.id)
        except:
            pass
        print(request.session.get_expiry_date())

    def get(self, request):
        user_profile = UserProfile.objects.get(user=request.user)
        serializer_class = profile_info(user_profile)
        return Response(serializer_class.data, status=status.HTTP_200_OK)
