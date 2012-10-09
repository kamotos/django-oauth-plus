import factory
from django_factory_boy.auth import UserF

from models import Token, Consumer, Resource

class ResourceFactory(factory.Factory):
    FACTORY_FOR = Resource

class ConsumerFactory(factory.Factory):
    FACTORY_FOR = Consumer


class TokenFactory(factory.Factory):
    FACTORY_FOR = Token

    consumer = factory.SubFactory(ConsumerFactory)
    resource = factory.SubFactory(ResourceFactory)
    user = factory.SubFactory(UserF)
    token_type = 2

    @classmethod
    def _prepare(cls, create, **kwargs):
        token = super(TokenFactory, cls)._prepare(create, **kwargs)
        token.generate_random_codes()
        return token