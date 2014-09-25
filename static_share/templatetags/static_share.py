# -*- coding: utf-8 -*-
from django import template

# from static_share.url_resolver import *
from .. import url_resolver

register = template.Library()

network_conf = {
	'facebook': {
		'share_url': 'https://www.facebook.com/sharer/sharer.php',
		'syntax': {
			'page_url': 'u',
			'title': 't',
		}
	},
	'googleplus': {
		'share_url': 'https://plus.google.com/share',
		'syntax': {
			'page_url': 'url',
		}
	},
	'twitter': {
		'share_url': 'https://twitter.com/intent/tweet',
		'syntax': {
			'page_url': 'source',
			'text': 'text',
		}
	},
}

@register.simple_tag()
def share_url(network, page_url, **kwargs):
	"""
	Get static share url for social network
	 network: network name (e.g. "twitter", "facebook")
	 page_url: page url to share
	"""
	conf = network_conf[network]
	share_url = conf['share_url']
	syntax = conf['syntax']

	return url_resolver.get_share_url(share_url, syntax, page_url=page_url, **kwargs)