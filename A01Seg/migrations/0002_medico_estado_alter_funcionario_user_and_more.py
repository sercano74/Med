# Generated by Django 5.1.2 on 2024-10-31 22:44

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('A01Seg', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='medico',
            name='estado',
            field=models.CharField(blank=True, choices=[('0', 'No activo'), ('1', 'Activo'), ('2', 'Vacaciones')], default=0, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='funcionario',
            name='user',
            field=models.OneToOneField(help_text='Usuario con perfil de funcionario', on_delete=django.db.models.deletion.RESTRICT, related_name='funcionarios', to=settings.AUTH_USER_MODEL, verbose_name='Funcionario'),
        ),
        migrations.AlterField(
            model_name='medico',
            name='experiencia',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='medico',
            name='user',
            field=models.OneToOneField(help_text='Usuario con perfil de médico', on_delete=django.db.models.deletion.RESTRICT, related_name='medicos', to=settings.AUTH_USER_MODEL, verbose_name='Médico'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='estado',
            field=models.CharField(blank=True, choices=[('0', 'Sin actividad'), ('1', 'Con hora tomada'), ('2', 'Exámenes pendientes'), ('3', 'Diagnosticado'), ('4', 'Eliminado')], default=0, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='user',
            field=models.OneToOneField(help_text='Usuario con perfil de paciente', on_delete=django.db.models.deletion.RESTRICT, related_name='pacientes', to=settings.AUTH_USER_MODEL, verbose_name='Paciente'),
        ),
    ]
