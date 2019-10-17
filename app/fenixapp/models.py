from django.db import models


class MomoRequest(models.Model):
    """
    Model class for user Momo requests
    """
    date_created = models.DateTimeField(auto_now_add=True)
    user_number = models.CharField(max_length=20, editable=False)
    amount = models.IntegerField()
    payment_note = models.CharField(max_length=300, null=True)
    request_status = models.CharField(max_length=70, null=True)
    transaction_ref = models.TextField()
    callback_id = models.TextField(null=True)


    def __str__(self):
        return "MomoRequest obj"
