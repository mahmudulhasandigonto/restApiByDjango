# Generated by Django 4.1.1 on 2022-10-10 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_delete_cart'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cart_name', models.CharField(max_length=225)),
                ('cart_price', models.DecimalField(decimal_places=10, max_digits=19)),
                ('cart_tax', models.DecimalField(decimal_places=10, max_digits=19)),
                ('cart_quantity', models.IntegerField()),
            ],
        ),
    ]
