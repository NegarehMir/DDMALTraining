import csv
from django.core.management.base import BaseCommand
from catalogue.models.source import Source
from catalogue.models.archive import Archive
from catalogue.models.composer import Composer
from catalogue.models.composition import Composition
from catalogue.models.composed import Composed


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


    def _get_composition(self, row):
        composition, created = Composition.objects.get_or_create(title=row['composition_name']);

        if created:
            if row['composition_name']:
                composition.title = row['composition_name']
            composition.save()

        return composition


    def _get_composer(self, row):
        if row['composer'].startswith('?'):
            composer, created = Composer.objects.get_or_create(name=row['composer'][1:]);
        else:
            composer, created = Composer.objects.get_or_create(name=row['composer']);

        if created:
            if row['composer']:
                composer.name = row['composer']
            composer.save()

        return composer



    def handle(self, *args, **options):
        print('Deleting sources')
        Source.objects.all().delete()
        print('Deleting archive')
        Archive.objects.all().delete()
        print('Deleting composer')
        Composer.objects.all().delete()
        print('Deleting composition')
        Composition.objects.all().delete()
        print('Deleting composed')
        Composed.objects.all().delete()

        with open('diamm_excerpt.csv', 'r') as csvfile:
            contents = csv.DictReader(csvfile)


            for rownum, row in enumerate(contents):
                print("Importing row {0}".format(rownum))
                source = self._get_source(row)
                archive = self._get_archive(row)
                composition = self._get_composition(row)
                composer = self._get_composer(row)
                composed = Composed()

                if not source.archive:
                    source.archive = archive
                    source.save()

                if not composition.source:
                    composition.source = source
                    composition.save()

                if not composition.composer:
                    if composer.name == "no composer/anon":
                        composition.anonymous = True
                    composition.composer = composer
                    composition.save()

                if composer.name.startswith('?'):
                    composed.certain = False
                    composer.name = composer.name[1:]
                    composer.save()
                if not composed.composition:
                    composed.composition = composition
                if not composed.composer:
                    composed.composer = composer
                composed.save()










