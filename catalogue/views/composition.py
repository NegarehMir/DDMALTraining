from rest_framework.generics import ListAPIView, RetrieveAPIView
from catalogue.models.composition import Composition


class CompositionListView(ListAPIView):
    #Handels GET "/compositions/"
    queryset = Composition.objects.all()
    serializer_class = CompositionSerializer



class CompositionDetailView(RetrieveAPIView):
    # HAndles GET "/compositions/1/"
    pass
