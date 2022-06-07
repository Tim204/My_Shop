from celery import shared_task
from django.conf import settings
from orders.models import Order

@shared_task
def payment_completed(order_id):
    """
    Task to send an e-mail notification when an order is
    successfully created.
    """
    order = Order.objects.get(id=order_id)