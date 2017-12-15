from rest_framework import serializers
from .models import Company, Billing
from django.utils.timezone import now

class BillingSerializer(serializers.ModelSerializer):

    days_remaining = serializers.SerializerMethodField()

    def get_days_remaining(self, obj):
        return ((obj.payment_date - now().date())/(60*60*24))

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Billing
        fields = ('id', 'expense', 'amount', 'payment_date', 'pay_status', 'days_remaining')

class CompanySerializer(serializers.ModelSerializer):

    billings = BillingSerializer(many=True, read_only=True)
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Company
        fields = ('id' ,'company_name', 'department_name', 'billings', 'date_created', 'date_modified')
