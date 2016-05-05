from rest_framework.generics import ListAPIView, RetrieveAPIView
from catalogue.models.composed import Composed
from catalogue.serializers.website.composed import ComposedSerializer


class ComposedListView(ListAPIView):
    #Handels GET "/composeds/"
    template_name = "composed/composed_list.html"
    queryset = Composed.objects.all()
    serializer_class = ComposedSerializer


class ComposedDetailView(RetrieveAPIView):
    # HAndles GET "/composeds/1/"
    template_name = "composed/composed_detail.html"
    queryset = Composed.objects.all()
    serializer_class = ComposedSerializer

