# Generated by Django 5.0.1 on 2024-07-29 10:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_alter_sysmenu_order_num_alter_sysmenu_parent_id'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='sysmenu',
            table='sys_menu',
        ),
        migrations.AlterModelTable(
            name='sysrole',
            table='sys_role',
        ),
        migrations.AlterModelTable(
            name='sysrolemenu',
            table='sys_role_menu',
        ),
        migrations.AlterModelTable(
            name='sysuserrole',
            table='sys_user_role',
        ),
    ]
