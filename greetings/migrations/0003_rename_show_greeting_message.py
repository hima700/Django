

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('greetings', '0002_rename_message_greeting_show'),
    ]

    operations = [
        migrations.RenameField(
            model_name='greeting',
            old_name='Show',
            new_name='message',
        ),
    ]
