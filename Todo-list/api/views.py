from rest_framework import viewsets
from api.models import Todo

from api.serializers import TodoSerializer


class TodoViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    search_fields = ('title', 'description')

    def get(self, request):
        data=Todo.objects.filter(user=request.user.id)
    
   