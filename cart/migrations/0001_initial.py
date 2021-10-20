# Generated by Django 3.2.8 on 2021-10-20 16:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('goods', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.CharField(max_length=50)),
                ('order_addr', models.CharField(max_length=100)),
                ('order_reci', models.CharField(max_length=50)),
                ('order_phon', models.CharField(max_length=20)),
                ('order_ship', models.IntegerField(verbose_name=5)),
                ('order_extr', models.CharField(max_length=300)),
                ('order_stat', models.IntegerField(choices=[(1, 'Pending payment'), (2, 'Pending delivery'), (3, 'Pending receipt'), (4, 'Order completed')], default=1)),
            ],
        ),
        migrations.CreateModel(
            name='OrderGoods',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goods_numb', models.IntegerField()),
                ('goods_info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goods.goodsinfo')),
                ('goods_order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cart.orderinfo')),
            ],
        ),
    ]
