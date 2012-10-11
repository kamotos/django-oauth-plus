from profile.merge import ProfileMerge
from models import Consumer, Token

class ConsumerMerge(ProfileMerge):
    model = Consumer


class TokenMerge(ProfileMerge):
    model = Token