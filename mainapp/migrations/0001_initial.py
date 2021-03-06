# Generated by Django 4.0.2 on 2022-03-28 04:14

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
            name='Category',
            fields=[
                ('category_id', models.AutoField(primary_key=True, serialize=False)),
                ('category_middle', models.CharField(max_length=256)),
                ('category_color', models.CharField(max_length=256)),
                ('category_product', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('review_id', models.AutoField(primary_key=True, serialize=False)),
                ('category_product', models.CharField(max_length=256)),
                ('review_number', models.IntegerField()),
                ('review_content', models.TextField()),
                ('first_status', models.BooleanField(default=False)),
                ('second_status', models.BooleanField(default=False)),
                ('dummy_status', models.BooleanField(default=False)),
                ('labeled_user_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SecondLabeledData',
            fields=[
                ('second_labeled_id', models.AutoField(primary_key=True, serialize=False)),
                ('second_labeled_emotion', models.CharField(max_length=256)),
                ('second_labeled_target', models.CharField(max_length=256)),
                ('second_labeled_expression', models.CharField(max_length=256)),
                ('category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.category')),
                ('review_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.review')),
            ],
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('result_id', models.AutoField(primary_key=True, serialize=False)),
                ('result_emotion', models.CharField(max_length=256)),
                ('result_target', models.CharField(max_length=256)),
                ('result_expression', models.CharField(max_length=256)),
                ('second_labeled_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.secondlabeleddata')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(null=True, upload_to='profile/')),
                ('name', models.CharField(max_length=256, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='FirstLabeledData',
            fields=[
                ('first_labeled_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_labeled_emotion', models.CharField(max_length=256)),
                ('first_labeled_target', models.CharField(max_length=256)),
                ('first_labeled_expression', models.CharField(max_length=256)),
                ('category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.category')),
                ('review_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.review')),
            ],
        ),
    ]
