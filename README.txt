BETA

Name: cmsplugin-faq
Description: duplicate of django-cms2's Text plugin: adds a 'topic' field and link anchors in templates; CMSFaqEntryPlugin creates FAQ entries (questions & answers); CMSFaqListPlugin creates <a> anchor list of FAQ entries, on the same page; CMSFaqEntryLinkPlugin links to specific or random CMSFaqEntries
Download: http://bitbucket.org/tehfink/cmsplugin-faq/

Requirements:
- django-cms-2 = master 2.0.2
- django = 1.1.1

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
- test with TinyMCE (should work)
- subclass Text plugin when this is possible
- add migrations (south)

NB:
- if you have CMS_MODERATOR enabled, you will see an issue where the FaqEntryLinkPlugin lists FaqEntries twice; the second listing is apparently an empty item. see: http://groups.google.com/group/django-cms/browse_thread/thread/3bc43ed4eb7c5467/2c4af3741bdbaa2d?lnk=gst&q=cms_moderator#2c4af3741bdbaa2d

Examples:

CMSPLUGIN_FAQENTRY_CSS_CHOICES = (('1', 'featured'),)
- adds an optional css class to the faq entry in the plugin template


Note:
This is not great code, but it works. Please tell me how to make it better!