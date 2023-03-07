# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from catalog.models import Author


class AuthorTestCase(TestCase):
    fixtures = ["catalog/tests/fixtures/authors_fixture.json"]

    def test_str_representation(self):
        author = Author.objects.get(id=1)
        self.assertEquals(author.pseudonym, str(author))

