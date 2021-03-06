# Generated by Django 4.0.4 on 2022-04-30 10:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user_info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Mobel_User_Name', models.CharField(blank=True, max_length=256, null=True)),
                ('Mobel_Email_Address', models.CharField(blank=True, max_length=256, null=True)),
                ('Mobel_Password', models.CharField(blank=True, max_length=256, null=True)),
            ],
            options={
                'verbose_name_plural': 'User Information',
            },
        ),
        migrations.CreateModel(
            name='vice_President_vote_count',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('person_get_vote', models.CharField(blank=True, max_length=256, null=True)),
                ('user_con', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app_1.user_info')),
            ],
            options={
                'verbose_name_plural': 'vice President vote',
            },
        ),
        migrations.CreateModel(
            name='senator_vote_count',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('person_get_vote_1', models.CharField(blank=True, max_length=256, null=True)),
                ('person_get_vote_2', models.CharField(blank=True, max_length=256, null=True)),
                ('person_get_vote_3', models.CharField(blank=True, max_length=256, null=True)),
                ('person_get_vote_4', models.CharField(blank=True, max_length=256, null=True)),
                ('person_get_vote_5', models.CharField(blank=True, max_length=256, null=True)),
                ('person_get_vote_6', models.CharField(blank=True, max_length=256, null=True)),
                ('person_get_vote_7', models.CharField(blank=True, max_length=256, null=True)),
                ('person_get_vote_8', models.CharField(blank=True, max_length=256, null=True)),
                ('person_get_vote_9', models.CharField(blank=True, max_length=256, null=True)),
                ('person_get_vote_10', models.CharField(blank=True, max_length=256, null=True)),
                ('person_get_vote_11', models.CharField(blank=True, max_length=256, null=True)),
                ('person_get_vote_12', models.CharField(blank=True, max_length=256, null=True)),
                ('person_get_vote_13', models.CharField(blank=True, max_length=256, null=True)),
                ('person_get_vote_14', models.CharField(blank=True, max_length=256, null=True)),
                ('person_get_vote_15', models.CharField(blank=True, max_length=256, null=True)),
                ('person_get_vote_16', models.CharField(blank=True, max_length=256, null=True)),
                ('person_get_vote_17', models.CharField(blank=True, max_length=256, null=True)),
                ('person_get_vote_18', models.CharField(blank=True, max_length=256, null=True)),
                ('person_get_vote_19', models.CharField(blank=True, max_length=256, null=True)),
                ('person_get_vote_20', models.CharField(blank=True, max_length=256, null=True)),
                ('person_get_vote_21', models.CharField(blank=True, max_length=256, null=True)),
                ('person_get_vote_22', models.CharField(blank=True, max_length=256, null=True)),
                ('person_get_vote_23', models.CharField(blank=True, max_length=256, null=True)),
                ('person_get_vote_24', models.CharField(blank=True, max_length=256, null=True)),
                ('person_get_vote_25', models.CharField(blank=True, max_length=256, null=True)),
                ('person_get_vote_26', models.CharField(blank=True, max_length=256, null=True)),
                ('person_get_vote_27', models.CharField(blank=True, max_length=256, null=True)),
                ('person_get_vote_28', models.CharField(blank=True, max_length=256, null=True)),
                ('person_get_vote_29', models.CharField(blank=True, max_length=256, null=True)),
                ('person_get_vote_30', models.CharField(blank=True, max_length=256, null=True)),



                ('user_con', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app_1.user_info')),
            ],
            options={
                'verbose_name_plural': 'senator vote',
            },
        ),
        migrations.CreateModel(
            name='President_vote_count',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('person_get_vote', models.CharField(blank=True, max_length=256, null=True)),
                ('user_con', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app_1.user_info')),
            ],
            options={
                'verbose_name_plural': 'President vote',
            },
        ),
    ]
