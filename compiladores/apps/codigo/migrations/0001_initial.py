<<<<<<< HEAD
# Generated by Django 2.0.5 on 2018-05-17 18:23
=======
# Generated by Django 2.0.5 on 2018-05-17 14:53
>>>>>>> 2c134556564fbfb5e50c9cc71f2d3503aae54c65

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
            name='Codigo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.TextField()),
                ('cantidadEjecuciones', models.PositiveSmallIntegerField()),
                ('FechaCreacion', models.DateTimeField(auto_now_add=True)),
                ('idUsuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
