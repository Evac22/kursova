# Generated by Django 4.2.1 on 2023-05-18 19:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0008_ticket_schedule_id_ticket_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.users'),
        ),
    ]
