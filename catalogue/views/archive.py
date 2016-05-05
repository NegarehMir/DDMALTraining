from rest_framework.generics import ListAPIView, RetrieveAPIView
from catalogue.models.archive import Archive


class ArchiveListView(ListAPIView):
    #Handels GET "/archives/"
    pass



class ArchiveDetailView(RetrieveAPIView):
    # HAndles GET "/archives/1/"
    pass
