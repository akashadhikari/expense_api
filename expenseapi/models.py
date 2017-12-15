from django.db import models

class Company(models.Model):
    """This class represents the bucketlist model."""
    COMPANY_NAMES = (
        ('Real Solutions', 'Real Solutions Pvt. Ltd.'),
        ('Merojob', 'Merojob'),
        ('Rojgari', 'Rojgari Services'),
        ('Aayulogic', 'Aayulogic'),
    )

    DEP_NAMES = (
        ('MARCOM', 'MARCOM'),
        ('ADMIN', 'Admin'),
        ('FINANCE', 'Finance'),
        ('IT', 'IT'),
        ('HR', 'HR'),
    )
    company_name = models.CharField(max_length=255, choices=COMPANY_NAMES)
    department_name = models.CharField(max_length=255, choices=DEP_NAMES)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "{}".format(self.company_name)

class Billing(models.Model):
    # expense, amount, payment_date, remaining, status
    PAY_STATUSES = (
        ('Paid', 'Paid'),
        ('Unpaid', 'Unpaid'),
        ('Pending', 'Pending'),
    )

    company = models.ForeignKey(Company, related_name='billings', on_delete=models.CASCADE)
    expense = models.CharField(max_length=255, blank=False, unique=False)
    amount = models.DecimalField(max_digits=10, decimal_places=2, blank=False)
    payment_date = models.DateField()
    pay_status = models.CharField(max_length=10, choices=PAY_STATUSES)

    # Define unique together and ordering withing class Meta

    def __str__(self):
        return "{}".format(self.expense)
