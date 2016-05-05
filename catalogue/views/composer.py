from rest_framework.generics import ListAPIView, RetrieveAPIView
from catalogue.models.composer import Composer


class ComposerListView(ListAPIView):
    #Handels GET "/composers/"
    pass



class ComposerDetailView(RetrieveAPIView):
    # HAndles GET "/composers/1/"
    pass
