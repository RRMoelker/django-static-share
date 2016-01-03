django-static-share
===================

Quickly share a page using static links (urls) on various social networks.
Template tags are provided for:

* Facebook
* Google+
* Twitter

## Installation

Either install directly:
`pip install git+https://github.com/RRMoelker/django-static-share.git#egg=static_share`

Or add the following line to your requirements file:
`-e git+https://github.com/RRMoelker/django-static-share.git#egg=static_share`

## Usage

1. Add `static_share` to your `INSTALLED_APPS`
2. Add '{% load static_share %}' to your template
3. Add an anchor tag and use 'share_url' tag for the href. For example: ```<a href='{% share_url "twitter" "http://test.com/currentpage/" text="This page is awesome" target="_blank" %}'>Share via Twitter</a>```

## Examples
```
<a href='{% share_url "facebook" "http://test.com/currentpage/" title="Awesome page" target="_blank" %}'>Share via Facebook</a>
<a href='{% share_url "googleplus" "http://test.com/currentpage/" target="_blank" %}'>Share via Google+</a>
<a href='{% share_url "twitter" "http://test.com/currentpage/" text="This page is awesome" target="_blank" %}'>Share via Twitter</a>
```

## Tag arguments
Depending on the social network different parameters can be passed to the template tag.

* Facebook: title
* Google+: none
* Twitter: text


## Requirements
Django
