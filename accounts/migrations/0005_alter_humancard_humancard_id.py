# Generated by Django 5.1.4 on 2024-12-20 04:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_alter_humancard_humancard_id_alter_humancard_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='humancard',
            name='humancard_id',
            field=models.AutoField(editable=False, primary_key=True, serialize=False),
        ),
    ]