import pysolr
from rest_framework.generics import GenericAPIView
from catalogue import settings
from rest_framework.response import Response
import pdb

class SearchListView(GenericAPIView):
    # set up solr instance
    #valid_keys.ap #= ['pk', 'type', 'shelfmark', 'name', 'start_date']


    def get(self, request, *args, **kwargs):
        template_name = "search/search_list.html"
        params = []
        search_results = []
        #print("request= {0}, pk = {1}".format(request.GET, request.GET['fsdkjhfsdlf']))
        # for key, value in request.GET:
        #     params.append((key, value))
        #     print("key={0}, value={1}".format(key, value))
        # if request.GET.len > 0:
        #     type = request.GET.get('type', default=None)
        #     pk = request.GET.get('pk', default=None)
        #
        #     shelfmark = request.GET.get('shelfmark', default=None)
        #     name = request.GET.get('name', default=None)
        #     start_date = request.GET.get('start_date', default=None)
        #     end_date = request.GET.get('end_date', default=None)
        #     surface = request.GET.get('surface', default=None)
        #
        #     #source attr
        #     #for key in request.GET.keys():
        #
        #
        #     if request.GET.has_key('type'):
        #         request.GET.get('type')
        #
        # print("params= {0}".format(params))
        #
        # params = {
        #     'fq': ['type:source', 'pk:{0}'.format(source_pk)]
        # }
        # q = self.server.search("*:*", **params)

        pk = request.GET.get('pk', default=None)
        params = {
            'fq': ['pk:{0}'.format(pk)]
        }
        solr = pysolr.Solr(settings.SOLR['SERVER'], timeout=20
                           )
        solr_search = solr.search('*:*', **params)#request.GET)
        print('solr_search: {0}'.format(solr_search))
        #pdb.set_trace()
        for result in solr_search:
            search_results.append(result)
        response = Response(search_results, 200, template_name)
        return response





