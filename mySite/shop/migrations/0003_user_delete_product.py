# Generated by Django 4.1.2 on 2022-10-07 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_product_category_product_image_product_price_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=50)),
                ('user_email', models.CharField(default='', max_length=50)),
                ('age', models.CharField(default='', max_length=50)),
                ('additionalInfo', models.CharField(max_length=300)),
                ('dateOfBirth', models.DateField()),
                ('profileImage', models.ImageField(default='', upload_to='shop/images')),
            ],
        ),
        migrations.DeleteModel(
            name='Product',
        ),
    ]
