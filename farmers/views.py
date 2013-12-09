from farmers.models import Farmer, Receipt
from farmers.serializers import FarmerSerializer, ReceiptSerializer
from rest_framework import generics
from rest_framework import permissions
from django.contrib.auth.models import User
from farmers.serializers import UserSerializer
from farmers.permissions import IsOwnerOrReadOnly
from rest_framework import renderers
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework import renderers
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.decorators import link


class FarmerViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = Farmer.objects.all()
    serializer_class = FarmerSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)
    filter_fields = ('farmer_idx','farmer_id','first_name','last_name','alias','res_address', 'res_parish','tel_number','cell_number','verified_status','dob','agri_activity')




#    @link(renderer_classes=[renderers.StaticHTMLRenderer])
#    def highlight(self, request, *args, **kwargs):
#        farmer = self.get_object()
#        return Response(farmer.highlighted)
#
#    def pre_save(self, obj):
#        obj.owner = self.request.user

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ReceiptViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `detail` receipts.
    """
    queryset = Receipt.objects.all()
    serializer_class = ReceiptSerializer
    filter_fields = ('farmer_idx', 'receipt_no', 'rec_range1', 'rec_range2', 'investigation_status', 'remarks')
