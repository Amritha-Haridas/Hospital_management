# Generated by Django 4.1.1 on 2023-03-17 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Department_head', '0002_rename_description_headdb_des_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employeedb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ename', models.CharField(max_length=30)),
                ('eimages', models.ImageField(default='null.jpg', upload_to='Image')),
                ('eage', models.IntegerField()),
                ('enumber', models.CharField(max_length=30)),
                ('desc', models.CharField(max_length=30)),
            ],
        ),
    ]
