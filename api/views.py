from rest_framework.response import Response
from rest_framework.views import APIView


class APIRoot(APIView):

    def get(self, request):

        data = {
            "profiles": "http://localhost:8000/api/profiles/",
            "categories": "http://localhost:8000/api/categories/",
            "tasks": "http://localhost:8000/api/tasks/",
            "risks": "http://localhost:8000/api/risks/",
            "purchases": "http://localhost:8000/api/purchases/",
        }

        return Response(data)
