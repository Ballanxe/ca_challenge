# Generated by Django 2.1.2 on 2018-11-03 15:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('companies', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('rating', models.PositiveSmallIntegerField()),
                ('title', models.CharField(db_index=True, max_length=64)),
                ('summary', models.TextField(max_length=10000)),
                ('ip_address', models.GenericIPAddressField(blank=True, null=True)),
                ('company', models.ForeignKey(default='', on_delete=django.db.models.deletion.DO_NOTHING, related_name='rating', to='companies.Company')),
                ('reviewer', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='rating', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Review',
                'verbose_name_plural': 'Reviews',
            },
        ),
    ]
