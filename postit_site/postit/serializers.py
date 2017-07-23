from rest_framework.serializers import(
    ModelSerializer,
    HyperlinkedIdentityField,
    SerializerMethodField
    )

from .models import Post

class PostCreateUpdateSerializer(ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Post
        fields = [ 
            #'id',
            'title', 
            #'slug',
            'content',
            'publish',
           
        ]
post_detail_url = HyperlinkedIdentityField(
        view_name='posts-api:detail',
        lookup_field='slug'
        )               

class PostDetailSerializer(ModelSerializer):
    url=post_detail_url
    user = SerializerMethodField()
    markdown = SerializerMethodField()
    class Meta:
        model = Post
        fields = [
            'user',
            'url',
            'id',
            'title', 
            'slug',
            'markdown',
            'content',
            'publish'
        ]
    def get_markdown(self, obj):
        return obj.get_markdown()      
    
    def get_user(self, obj):
        return str(obj.user.username)      

class PostListSerializer(ModelSerializer):
    url=post_detail_url
    user = SerializerMethodField()
    delete_url = HyperlinkedIdentityField(
        view_name='posts-api:delete',
        lookup_field='slug'
        )
    class Meta:
        model = Post
        fields = [
            'url',
            'user',
            'title',  
            'content',
            'publish',
            'delete_url'
        ]  

    def get_user(self, obj):
        return str(obj.user.username)    
           