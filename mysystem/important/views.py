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
from django.shortcuts import get_object_or_404
from django.http import HttpResponse


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

    def get_or_create_user_profile(self, user):
        try:
            user_profile = UserProfile.objects.get(user=user)
        except UserProfile.DoesNotExist:
            # New User Create kar deta hain
            user_profile = UserProfile.objects.create(user=user)
        return user_profile

    def get(self, request):
        # try:
        user_profile = self.get_or_create_user_profile(user=request.user)
        serializer = profile_info(user_profile)
        return Response(serializer.data, status=status.HTTP_200_OK)
        # except UserProfile.DoesNotExist:
        #     return Response({'error': 'UserProfile not found'}, status=status.HTTP_404_NOT_FOUND)


def profile_by_reference(request, code):
    profile = get_object_or_404(UserProfile, code=code)
    return HttpResponse(f"User Profile: {profile.user.username}")
