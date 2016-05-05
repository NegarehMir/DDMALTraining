from rest_framework.generics import ListAPIView, RetrieveAPIView
from catalogue.models.composed import Composed


class SourceListView(ListAPIView):
    #Handels GET "/composeds/"
    pass



class SourceDetailView(RetrieveAPIView):
    # HAndles GET "/composeds/1/"
    pass
