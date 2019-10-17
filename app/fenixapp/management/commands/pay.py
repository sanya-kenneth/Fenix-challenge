from django.core.management.base import BaseCommand, CommandError
from app.fenixapp.momoapi_client import collection_client
from app.fenixapp.models import MomoRequest


class Command(BaseCommand):
    help = 'Enables clients to make payments through mobile money'

    def handle(self, *args, **options):
        phone_number = input("Please enter your phone number:  ")
        amount = input("Please enter the amount you want to pay:  ")
        payer_message = "remote payment"
        response = collection_client.requestToPay(
            mobile=phone_number,
            amount=amount,
            external_id="123456789",
            payee_note="remote payment",
            payer_message=payer_message,
            currency="EUR"
        )
        self.stdout.write("**** Processing your request. Please wait ****")
        transaction_ref = response['transaction_ref']
        momorequest = MomoRequest(user_number=phone_number, amount=amount, payment_note=payer_message,
                                  request_status='PENDING', transaction_ref=transaction_ref)
        momorequest.save()
        check_status = collection_client.getTransactionStatus(
            transaction_id=transaction_ref)
        if check_status['status'] == 'SUCCESSFUL':
            momorequest.request_status = check_status['status']
            momorequest.save()
            self.stdout.write("**** Your request was successful ****")
