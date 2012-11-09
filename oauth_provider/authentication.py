from tastypie.authentication import Authentication

from .models import Consumer

class ConsumerAuthentication(Authentication):
    def is_authenticated(self, request, **kwargs):

        consumer_key = request.POST.get('consumer_key', None)
        consumer_key = request.GET.get('consumer_key', consumer_key)

        try:
            consumer = Consumer.objects.get(key=consumer_key)
            return True
        except:
            return False
