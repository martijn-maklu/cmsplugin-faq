from django import template
from cmsplugin_faq.models import FaqEntry
register = template.Library()


class LatestFAQsNode(template.Node):
    """
    parses & checks arguments passed to ``get_latest_faqs``; returns applicable Queryset of recently added CMSFaqPlugin models descendant from and including the current page
    """

    def __init__(self, num, varname):
        num, varname

        #'All' means slicing with [:None] , which returns everything
        if num == 'All' or num == 'all':
            num = None
        else:
            num = abs(int(num))
        self.num = num

        self.varname = varname

    def render(self, context):

        #apparently publisher_is_draft has different meanings depending on the status of CMS_MODERATOR?
        from django.conf import settings
        if settings.CMS_MODERATOR:
            #this seems logical
            PUBLISHER_STATE = False
        else:
            #this does not seem logical
            PUBLISHER_STATE = True

        #the current django-cms Page of the template tag
        page = context['current_page']

        #shortcircuit for django admin
        if page is not 'dummy':

            #get published descendant Pages of the current Page
            subpages = page.get_descendants().filter(publisher_is_draft=PUBLISHER_STATE)

            #list of all published faq plugins for descendant and current page
            allfaqs= []

            #get published plugins for this page
            for faq in page.cmsplugin_set.filter(plugin_type='CMSFaqEntryPlugin', publisher_is_draft=PUBLISHER_STATE):
                allfaqs.append(faq)

            #get published plugins for each subpage
            for subpage in subpages:
                for subpagefaq in subpage.cmsplugin_set.filter(plugin_type='CMSFaqEntryPlugin', publisher_is_draft=PUBLISHER_STATE):
                    allfaqs.append(subpagefaq)

#            import ipdb; ipdb.set_trace()

            #shortened list according to given argument
            faqs = allfaqs[:self.num]

            context[self.varname] = faqs

        return ''

@register.tag('get_latest_faqs')
def get_latest_faqs(parser, token):
    """
    A django-cms templatetag for returning recently added CMSFaqPlugin models.
    Note that the tag only returns Faq plugins descendant from the current page.

    Some common case examples::

        {% get_latest_faqs All as latest_faqs %}
        {% for latest in latest_faqs %}
            ...
        {% endfor %}

        {% get_latest_faqs 3 as latest_faqs %}
        {% for latest in latest_faqs %}
            ...
        {% endfor %}

    Supported arguments are: ``All``, ``all``, positive integers, and zero
    """

    #split up arguments
    bits = token.split_contents()

    #knock off the first argument
    bits.pop(0)
    num = bits[0]
    varname = bits[2]

    if len(bits) != 3:
        raise template.TemplateSyntaxError, "get_latest tag takes exactly three arguments"
    if bits[1] != 'as':
        raise template.TemplateSyntaxError, "second argument to get_latest tag must be 'as'"
    return LatestFAQsNode(num, varname)