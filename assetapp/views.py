from django.contrib.auth.models import Group, User
from rest_framework import permissions, viewsets

from assetapp.serializers import GroupSerializer, UserSerializer, AssetSerializer
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from .models import Asset

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all().order_by('name')
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

class AssetViewSet(viewsets.ModelViewSet):
    queryset = Asset.objects.all()
    serializer_class = AssetSerializer

    def list(self, request):
        serializer = AssetSerializer(self.queryset, many=True, context={'request': request})
        return Response({'data': serializer.data})
       
    def create(self, request):
      asset = AssetSerializer(data=request.data)

      if asset.is_valid():
        asset.save()
        return Response(status=200)
      else:
         return Response(status=422)
