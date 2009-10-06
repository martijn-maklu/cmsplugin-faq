from django.db import models
from django.utils.translation import ugettext_lazy as _
from cms.models import CMSPlugin, Page
from django.conf import settings
from django.utils.html import strip_tags
from django.utils.text import truncate_words
from cms.plugins.text.utils import plugin_admin_html_to_tags, plugin_tags_to_admin_html
from django.conf import settings

class FaqEntry(CMSPlugin):
    """Copy of Text plugin model, plus additional 'topic' Charfield"""
    topic = models.CharField(_("Topic"),max_length=500, help_text=_('FAQ entry topic'))
    body = models.TextField(_("body"))
   
    def _set_body_admin(self, text):
        self.body = plugin_admin_html_to_tags(text)

    def _get_body_admin(self):
        return plugin_tags_to_admin_html(self.body)

    body_for_admin = property(_get_body_admin, _set_body_admin, None,
                              """
                              body attribute, but with transformations
                              applied to allow editing in the
                              admin. Read/write.
                              """)
    
    def __unicode__(self):
#        return u"%s" % (truncate_words(strip_tags(self.body), 3)[:30]+"...")
        return u"%s" % (truncate_words(self.topic, 5)[:30]+"...")


#get custom css from settings or use default
CMSPLUGIN_FAQLIST_CSS_CHOICES = getattr(settings,"CMSPLUGIN_FAQLIST_CSS_CHOICES", (('0', ''),('1', 'faq-list-entry'),('2', 'faq-list-entry-small'),) )

class FaqList(CMSPlugin):
    """Model to give FaqList plugin various options"""

    css = models.CharField(_('CSS class'), max_length=1, choices=CMSPLUGIN_FAQLIST_CSS_CHOICES, default='0', help_text=_('Additional CSS class to apply'))

    def __unicode__(self):
        return u"%s" % (self.page.get_page_title())