from rest_framework.generics import ListAPIView, RetrieveAPIView
from catalogue.models.archive import Archive
from catalogue.serializers.website.archive import ArchiveSerializer

class ArchiveListView(ListAPIView):
    #Handels GET "/archives/"
    template_name = "archive/archive_list.html"
    queryset = Archive.objects.all()
    serializer_class = ArchiveSerializer



class ArchiveDetailView(RetrieveAPIView):
    # HAndles GET "/archives/1/"
    template_name = "archive/archive_detail.html"
    queryset = Archive.objects.all()
    serializer_class = ArchiveSerializer
