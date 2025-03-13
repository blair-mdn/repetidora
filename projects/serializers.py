from rest_framework  import serializers
from .models import Projects

class ProjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = ('id', 'title', 'description', 'technology', 'created_at')
        read_only_fields = ('created_at',)