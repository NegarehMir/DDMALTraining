from rest_framework.generics import ListAPIView, RetrieveAPIView
from catalogue.models.composed import Composed


class ComposedListView(ListAPIView):
    #Handels GET "/composeds/"
    pass



class ComposedDetailView(RetrieveAPIView):
    # HAndles GET "/composeds/1/"
    pass
