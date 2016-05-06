import pysolr
from rest_framework.generics import GenericAPIView
from catalogue import settings
from django.utils import six


class SearchListView(GenericAPIView):
    # set up solr instance
    template_name = "source/source_detail.html" #TODO make a search template
    #valid_keys.ap #= ['pk', 'type', 'shelfmark', 'name', 'start_date']

    def get(self, request, *args, **kwargs):
        params = []
        print("request= {0}, pk = {1}".format(request.GET, request.GET['fsdkjhfsdlf']))
        # for key, value in request.GET:
        #     params.append((key, value))
        #     print("key={0}, value={1}".format(key, value))
        if request.GET.len > 0:
            type = request.GET.get('type', default=None)
            pk = request.GET.get('pk', default=None)
            if type =
                valid_keys =

            #source attr
            for key in request.GET.keys():

            # shelfmark = request.GET.get('shelfmark', default=None)
            # name = request.GET.get('name', default=None)
            # start_date = request.GET.get('start_date', default=None)
            # end_date = request.GET.get('end_date', default=None)
            # surface

            if request.GET.has_key('type'):
                request.GET.get('type')

        print("params= {0}".format(params))

        solr = pysolr.Solr(settings.SOLR['SERVER'], timeout=20)
        solr.search('*.*')




