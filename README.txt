PRE-ALPHA

Name: cmsplugin-faq
Description: duplicate of django-cms2's Text plugin: adds a 'topic' field and link anchors in templates; CMSFaqEntryPlugin creates FAQ entries (questions & answers), CMSFaqListPlugin creates <a> anchor list of FAQ entries, on the same page
Download: http://bitbucket.org/tehfink/cmsplugin-faq/

Requirements:
- django-cms-2.0: rev 63a124cfda6c10b9f4831da0627a9f80b64e675c
- django: 1.1

Last tested with:
- django-cms-2.0: rev 63a124cfda6c10b9f4831da0627a9f80b64e675c
- django: rev 11600

Setup
- make sure requirements are installed and properly working
- add cmsplugin_faq to python path
- add 'cmsplugin_faq' to INSTALLED_APPS
- run 'python manage.py syncdb'
- add plugins to pages

Optional
- define CMSPLUGIN_FAQLIST_CSS_CHOICES in settings
- copy cmsplugin_faq/templates/plugins/cmsplugin_faq/ to your project directory

Todo:
- allow CMSFaqListPlugin plugin to be on a different page than CMSFaqEntryPlugin
- add ability to set css for faq entries: CMSPLUGIN_FAQENTRY_CSS_CHOICES
- test with TinyMCE (should work)
- subclass Text plugin when this is possible


Examples:

CMSPLUGIN_FAQLIST_CSS_CHOICES = (('0', ''),('1', 'faq-list-entry'),('2', 'faq-list-entry-small'),)
- adds an optional css class to the entry in the faq list in the plugin template


Note:
This is not great code, but it works. Please tell me how to make it better!