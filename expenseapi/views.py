from rest_framework import generics
from .serializers import CompanySerializer, BillingSerializer
from .models import Company, Billing

class CreateView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new instance."""
        serializer.save()

class DetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""

    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class CreateexpView(generics.ListCreateAPIView):

    queryset = Billing.objects.all()
    serializer_class = BillingSerializer

    def perform_create(self, serializer):
        serializer.save()

class DetailsexpView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Billing.objects.all()
    serializer_class = BillingSerializer

# COMPANY BASED VIEWS START: /companies/ realsolutions||merojob||rojgari||aayulogic

class RealsolutionsView(generics.ListCreateAPIView):
    queryset = Company.objects.filter(company_name="Real Solutions")
    serializer_class = CompanySerializer

class MerojobView(generics.ListCreateAPIView):
    queryset = Company.objects.filter(company_name="Merojob")
    serializer_class = CompanySerializer

class RojgariView(generics.ListCreateAPIView):
    queryset = Company.objects.filter(company_name="Rojgari")
    serializer_class = CompanySerializer

class AayulogicView(generics.ListCreateAPIView):
    queryset = Company.objects.filter(company_name="Aayulogic")
    serializer_class = CompanySerializer

# COMPANY BASED VIEWS END