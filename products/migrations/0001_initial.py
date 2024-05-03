# Generated by Django 4.2.7 on 2024-05-03 21:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='product_name')),
                ('model', models.CharField(max_length=255, verbose_name='product_model')),
                ('release_date', models.DateField(verbose_name='product_release_date')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='company_products', to='main.company', verbose_name='company_name')),
            ],
        ),
    ]
