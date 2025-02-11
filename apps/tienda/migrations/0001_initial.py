# Generated by Django 5.0.1 on 2024-02-02 05:46

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Categorias',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
                ('activo', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name_plural': 'Categorias',
            },
        ),
        migrations.CreateModel(
            name='Productos',
            fields=[
                ('codigo', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='tienda_images')),
                ('marca', models.CharField(max_length=50)),
                ('precio', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('modo_uso', models.TextField(blank=True, null=True)),
                ('ingredientes', models.TextField(blank=True, null=True)),
                ('conservacion', models.TextField(blank=True, null=True)),
                ('destacado', models.BooleanField(default=True)),
                ('activo', models.BooleanField(default=True)),
                ('stock', models.PositiveIntegerField(default=0)),
                ('stock_minimo', models.PositiveIntegerField(default=1)),
                ('descuento', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('precio_oferta', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tienda.categorias')),
            ],
            options={
                'verbose_name_plural': 'Producto',
            },
        ),
        migrations.CreateModel(
            name='Estadistica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad_vendida', models.PositiveIntegerField(default=0)),
                ('total_ventas', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tienda.productos')),
            ],
        ),
        migrations.CreateModel(
            name='Resena',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comentario', models.TextField()),
                ('calificacion', models.PositiveIntegerField(default=5)),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tienda.productos')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
