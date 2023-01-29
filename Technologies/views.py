from .serializers import Technology, TechnologySerializer
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView, Response, status, Request
from rest_framework import generics
from django.forms.models import model_to_dict


class TechnologyListCreateView(generics.ListCreateAPIView):
    queryset = Technology.objects.all()
    serializer_class = TechnologySerializer


class TechnologyUpdateView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Technology.objects.all()
    serializer_class = TechnologySerializer

    lookup_url_kwarg = "technology_id"

    def delete(self, req: Request, technology_id: int) -> Response:
        import ipdb

        def order_index(tech):
            return tech["index"]

        technology = get_object_or_404(Technology, id=technology_id)
        technology.delete()

        tech_db = Technology.objects.all().order_by("index")
        """ technologies_db = [model_to_dict(tech) for tech in tech_db]
        technologies_db.sort(key=order_index) """

        for index, newTech in enumerate(tech_db):
            setattr(newTech, "index", index + 1)
            newTech.save()

        return Response("", status.HTTP_204_NO_CONTENT)
