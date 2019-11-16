# Generated by Django 2.2.6 on 2019-11-16 09:56

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('name', models.EmailField(max_length=50)),
                ('nickname', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=50)),
                ('type', models.CharField(choices=[('Полный пакет', 'full'), ('Бесплатный пакет', 'free')], default='Бесплатный пакет', max_length=30)),
                ('checkfield', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]