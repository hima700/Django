

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('greetings', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='greeting',
            old_name='message',
            new_name='Show',
        ),
    ]
