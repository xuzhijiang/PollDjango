from django.test import TestCase
from .models import OAuthConfig


class OAuthConfigTest(TestCase):
    def config_save_test(self):
        c = OAuthConfig()
        c.type = 'weibo'
        c.appkey = 'appkey'
        c.appsecret = 'appsecret'
        c.save()
