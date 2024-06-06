# Generated by Django 3.2 on 2024-06-05 13:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_type', models.PositiveSmallIntegerField(choices=[(1, 'Charge'), (2, 'Purchase'), (3, 'Received Transfer'), (4, 'Sent Transfer')], default=1)),
                ('amount', models.BigIntegerField()),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='transactions', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
