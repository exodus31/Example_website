# Generated by Django 4.0.5 on 2022-09-20 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Objects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('geography', models.CharField(default='The Geography of Asgard is dominated by huge mountains.', max_length=100)),
                ('history', models.CharField(default='History of Asgard goes back a millenia.', max_length=100)),
                ('culture', models.CharField(default='Culturally Asgard remains a mystery to the passer by', max_length=100)),
                ('language', models.CharField(default='Language barriers in Asgard do not allow outsiders to live.', max_length=100)),
            ],
        ),
    ]