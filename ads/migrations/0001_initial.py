# Generated by Django 4.1.7 on 2023-02-25 17:48

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
            name='Ads',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='عنوان آگهی')),
                ('describtion', models.TextField(max_length=1000, verbose_name='توضیحات آگهی')),
                ('payment_type', models.CharField(choices=[('agreement', 'توافقی'), ('fixed', 'مقطوع')], max_length=120, verbose_name='نوع پرداخت')),
                ('price', models.PositiveBigIntegerField(blank=True, null=True, verbose_name='مبلغ')),
            ],
            options={
                'verbose_name_plural': 'آگهی ها',
            },
        ),
        migrations.CreateModel(
            name='AdsPictures',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(upload_to='Ads/AdsPictures/', verbose_name='تصویر آگهی')),
                ('ads', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ads.ads')),
            ],
            options={
                'verbose_name_plural': 'تصاویر آگهی ',
            },
        ),
        migrations.CreateModel(
            name='AdsCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='عنوان دسته بندی')),
                ('header', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ads.adscategory', verbose_name='سر گروه')),
            ],
            options={
                'verbose_name_plural': 'دسته بندی آگهی ها',
            },
        ),
        migrations.AddField(
            model_name='ads',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ads', to='ads.adscategory', verbose_name='دسته بندی'),
        ),
        migrations.AddField(
            model_name='ads',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='کاربر'),
        ),
    ]