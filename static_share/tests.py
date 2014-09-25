# -*- coding: utf-8 -*-
from django.template import Template, Context, TemplateSyntaxError
from unittest import TestCase

class StaticShareTestCase(TestCase):
	
	def test_working_tag(self):
		"""
			Test template tag working
			Very basic, does not test parameters
		"""
		rendered = Template(
			'{% load static_share %}'
			'{% share_url "twitter" "http://test.com" %}'
		).render(Context())
		self.assertEqual(rendered,"https://twitter.com/intent/tweet?source=http%3A%2F%2Ftest.com")