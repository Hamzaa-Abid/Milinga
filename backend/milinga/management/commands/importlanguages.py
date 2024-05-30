from django.core.management.base import BaseCommand, CommandError
from django.conf.locale import LANG_INFO
from subjects.models import Subject
from django.utils import translation
from django.utils.translation import gettext as _

from subjects.models import Subject

class Command(BaseCommand):
    help = 'Imports language names into subjects from django.conf.locale.LANG_INFO'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        oSubjectLanguages = {}
        for lang in LANG_INFO:
            lang = lang.lower()
            if not 'name' in LANG_INFO[lang]:
                self.stdout.write("{} hat kein 'name'".format(lang))
                continue
            if not hasattr(oSubjectLanguages, lang):
                oSubjectLanguages[lang] = { 'subject_en': LANG_INFO[lang]['name']}
            for lang_trans in LANG_INFO:
                sAttrName = 'subject_'+lang_trans
                if hasattr(Subject, sAttrName):
                    with translation.override(lang_trans):
                        oSubjectLanguages[lang]['subject_'+lang_trans] = _(LANG_INFO[lang]['name'])
        
        for lang_code, oSubjectLanguageTrans in oSubjectLanguages.items():
            # self.stdout.write(lang_code + ': ' + oSubjectLanguageTrans['subject_en'] + ' - ' + oSubjectLanguageTrans['subject_km'])
            for lang_code2, oSubjectLanguageTrans2 in oSubjectLanguages.items():
                if oSubjectLanguageTrans == oSubjectLanguageTrans2 or lang_code > lang_code2:
                    continue
                for k, v in oSubjectLanguageTrans2.items():
                    if oSubjectLanguageTrans[k] == v and v != None:
                        self.stdout.write("{} und {} heißt auf {} = {}".format(oSubjectLanguageTrans['subject_en'], oSubjectLanguageTrans2['subject_en'], k, v))
                        oSubjectLanguageTrans[k] = None
                        oSubjectLanguageTrans2[k] = None
                    if v != None and len(v) > 50:
                        self.stdout.write("{} ({}) in {} ist zu lang!".format(v, oSubjectLanguageTrans2['subject_en'], k))
                    

            # for k, v in oSubjectLanguageTrans.items():
            #     self.stdout.write(k + ':' + v)
            Subject.objects.update_or_create(
                subject_en = oSubjectLanguageTrans['subject_en'],
                defaults = oSubjectLanguageTrans,
            )
