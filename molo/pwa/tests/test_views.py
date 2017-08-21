# -*- coding: utf-8 -*-
import json
from django.contrib.auth.models import User

from django.core.urlresolvers import reverse
from django.test import TestCase, Client

from molo.profiles.models import UserProfile
from molo.core.tests.base import MoloTestCaseMixin


class RegistrationTokenTestCase(TestCase, MoloTestCaseMixin):
    def setUp(self):
        self.mk_main()
        self.client = Client()
        self.user = User.objects.create_user(
            username="tester",
            email="tester@example.com",
            password="0000")

    def test_update_registration_token(self):
        self.client.login(username='tester', password='0000')
        response = self.client.post(
            reverse('registration-token-view'),
            {'body': json.dumps({'registration_id': '1234'})})
        self.assertEquals(response, 'Token Updated')
