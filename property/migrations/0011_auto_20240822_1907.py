# Generated by Django 2.2.24 on 2024-08-22 16:07

from django.db import migrations
import phonenumbers


def format_phonenumber(phone):
    try:
        parsed_phone = phonenumbers.parse(phone, "RU")
    except phonenumbers.phonenumberutil.NumberParseException:
        return None
    if phonenumbers.is_possible_number(parsed_phone) and phonenumbers.is_valid_number(
        parsed_phone
    ):
        pure_phone = phonenumbers.format_number(
            parsed_phone, phonenumbers.PhoneNumberFormat.E164
        )
        return pure_phone


def fill_owner_pure_phone(apps, schema_editor):
    Flat = apps.get_model("property", "Flat")
    flats = Flat.objects.all()
    
    for flat in flats.iterator():
        flat.owner_pure_phone = format_phonenumber(flat.owners_phonenumber)
        flat.save()


class Migration(migrations.Migration):

    dependencies = [
        ("property", "0010_flat_owner_pure_phone"),
    ]

    operations = [
        migrations.RunPython(fill_owner_pure_phone),
    ]
