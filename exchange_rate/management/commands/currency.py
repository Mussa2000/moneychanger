import csv
import os

from django.core.management.base import BaseCommand
from exchange_rate.models import Currency



class Command(BaseCommand):
    help = "Load currencies from a CSV file"

    def handle(self, *args, **kwargs):
        file_path = os.path.join(os.getcwd(), "currency.csv") 

        if not os.path.exists(file_path):
            self.stderr.write(self.style.ERROR("File not found"))
            return

        created, skipped = 0, 0

        seen_countries = set()

        with open(file_path, newline='', encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                country = row.get("Entity", "").strip()
                name = row.get("Currency", "").strip()
                code = row.get("AlphabeticCode", "").strip()

                if not country or not name or not code:
                    continue

                if country in seen_countries:
                    skipped += 1
                    continue

                seen_countries.add(country)

                if not Currency.objects.filter(code=code).exists():
                    Currency.objects.create(
                        country=country,
                        name=name,
                        code=code,
                    )
                    created += 1
                else:
                    skipped += 1

        self.stdout.write(self.style.SUCCESS(f"{created} currencies created, {skipped} skipped"))
