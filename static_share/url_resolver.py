# -*- coding: utf-8 -*-
import urllib

def compute_full_url(url, parameters):
	"""
	Converts page url and parameter dictionary into a sharable static link with relevant get parameters
	"""
	querystring = urllib.urlencode(parameters)
	full_url ='{}?{}'.format(url, querystring)
	return full_url


def get_parameter_dictionary(syntax, **kwargs):
	"""
	Conversion of static_share names to get parameter name for network.
	For example conversion of 'url' to 'source' and 'text' to 't' for Twitter.
	"""
	parameters = {}

	for key, value in syntax.iteritems():
		if key in kwargs:
			parameters[value] = kwargs[key]
	return parameters


def get_share_url(share_url, syntax, **kwargs):
	"""
	Combine share url given the syntax for the specific social network into a full url
	"""
	parameters = get_parameter_dictionary(syntax, **kwargs)
	return compute_full_url(share_url, parameters)
