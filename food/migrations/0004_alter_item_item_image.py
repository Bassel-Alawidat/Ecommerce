# Generated by Django 4.2.3 on 2023-07-20 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0003_item_user_name_alter_item_item_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='item_image',
            field=models.CharField(default='https://cdn-icons-png.flaticon.com/512/2737/2737035.png', max_length=500),
        ),
    ]
