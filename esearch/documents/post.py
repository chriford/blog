from django_elasticsearch_dsl import Document, fields
from django_elasticsearch_dsl.registries import registry

from blog.models import Post
from security.models import User


@registry.register_document
class PostDocument(Document):
    category = fields.ObjectField(properties=dict(name=fields.TextField()))
    owner = fields

    class Index:
        name = "posts"
        settings = {
            "number_of_shards": 1,
            "number_of_replicas": 0,
        }

    class Django:
        model = Post
        fields = [
            "title",
            "description",
        ]
