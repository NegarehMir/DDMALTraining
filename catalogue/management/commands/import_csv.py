import csv
from django.core.management.base import BaseCommand
from catalogue.models.source import Source
from catalogue.models.archive import Archive


class Command(BaseCommand):
    def _get_source(self, row):
        source, created = Source.objects.get_or_create(shelfmark=row['shelfMark']);

        if created:
            if row['sourceName']:
                source.name = row['sourceName']
            if row['startdate']:
                source.start_date= row['startdate']
            if row['enddate']:
                source.end_date= row['enddate']
            if row['sourceType']:
                source.type= row['sourceType']
            if row['dateComments']:
                source.comments= row['dateComments']
            if row['surface']:
                source.surface= row['surface']
            source.save()

        return source

    def _get_archive(self, row):
        archive, created = Archive.objects.get_or_create(name=row['archiveName']);

        if created:
            if row['archiveName']:
                archive.name = row['archiveName']
            if row['archiveCitarary']:
                archive.city = row['archiveCitarary']
            if row['siglum']:
                archive.siglum = row['siglum']
            if row['archiveCountry']:
              archive.country = row['archiveCountry']
            archive.save()

        return archive



    def handle(self, *args, **options):
        print('Deleting sources')
        Source.objects.all().delete()
        print('Deleting archive')
        Archive.objects.all().delete()

        with open('diamm_excerpt.csv', 'r') as csvfile:
            contents = csv.DictReader(csvfile)


            for rownum, row in enumerate(contents):
                print("Importing row {0}".format(rownum))
                source = self._get_source(row)
                archive = self._get_archive(row)