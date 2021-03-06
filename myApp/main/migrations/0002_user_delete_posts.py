# Generated by Django 4.0.2 on 2022-04-12 00:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_name', models.CharField(max_length=30, verbose_name='Аты')),
                ('Last_name', models.CharField(max_length=30, verbose_name='Тегі')),
                ('phone_number', models.IntegerField(verbose_name='Нөмір')),
                ('Data_Birth', models.DateField(verbose_name='Туған жылы')),
                ('ISBN', models.CharField(max_length=15, verbose_name='ЖСН')),
                ('email', models.CharField(max_length=50, verbose_name='Почта')),
                ('password', models.CharField(max_length=8, verbose_name='Құпия сөз')),
                ('password1', models.CharField(max_length=8, verbose_name='Құпия сөзді қайталыныз')),
            ],
        ),
        migrations.DeleteModel(
            name='Posts',
        ),
    ]
