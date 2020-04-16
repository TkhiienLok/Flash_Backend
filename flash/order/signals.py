from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

# noinspection PyProtectedMember
from flash._auth.models import MyUser
from flash.order.models import Order, OrderedProduct


@receiver(post_save, sender=Order)
def find_courier(sender, instance, created, **kwargs):
    """
    For created order find courier that have less undone orders
    """
    if created:
        courier = None

        for user in MyUser.objects.all():
            # 4 - Courier role id
            if user.role == 4:

                if not courier:
                    courier = user

                if user.undone_orders.count() < courier.undone_orders.count():
                    courier = user

        instance.set_courier(courier)


@receiver(post_save, sender=OrderedProduct)
def recalculate_price(sender, instance, created, **kwargs):
    """
    After creating or updating ordered product in order, recalculate overall price
    """
    order = instance.order

    order.calculate_price()


@receiver(post_delete, sender=OrderedProduct)
def recalculate_price_after_delete(sender, instance, **kwargs):
    """
    After deleting ordered product in order, recalculate overall price
    """
    order = instance.order

    order.calculate_price()
