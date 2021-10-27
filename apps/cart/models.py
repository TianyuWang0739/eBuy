from django.db import models


# Create the order information model here.
class OrderInfo(models.Model):
    # Kinds of order status
    status = (
        (1, 'Pending payment'),
        (2, 'Pending delivery'),
        (3, 'Pending receipt'),
        (4, 'Order completed'),
    )

    # Order Number
    order_id = models.CharField(max_length=50)
    # Receiving address
    order_addr = models.CharField(max_length=100)
    # Recipient
    order_reci = models.CharField(max_length=50)
    # Contact number
    order_phon = models.CharField(max_length=20)
    # Shipping cost
    order_ship = models.IntegerField(5)
    # Order extra information
    order_extr = models.CharField(max_length=300)
    # Order status
    order_stat = models.IntegerField(default=1, choices=status)


# Create the order goods model
class OrderGoods(models.Model):
    # Product Information
    goods_info = models.ForeignKey('goods.GoodsInfo', on_delete=models.CASCADE)
    # Number of items
    goods_numb = models.IntegerField()
    # Product order
    goods_order = models.ForeignKey('OrderInfo', on_delete=models.CASCADE)
