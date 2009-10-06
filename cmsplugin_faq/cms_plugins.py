from cms.plugin_pool import plugin_pool
from cms.plugin_base import CMSPluginBase
from cms.models import CMSPlugin
from django.utils.translation import ugettext_lazy as _
from models import FaqEntry, FaqList
from forms import FaqEntryForm
from widgets.wymeditor_widget import WYMEditor
from utils import plugin_tags_to_user_html
from django.forms.fields import CharField, BooleanField
from django.forms import TextInput
from settings import USE_TINYMCE
from django.conf import settings


class CMSFaqEntryPlugin(CMSPluginBase):
    """Copy of Text plugin, includes 'topic' Charfield"""

    model = FaqEntry
    name = _("FAQ Entry")
    form = FaqEntryForm
    render_template = "plugins/cmsplugin_faq/faq_entry.html"
    change_form_template = "cms/plugins/text_plugin_change_form.html"

    def get_editor_widget(self, request, plugins):
        """
        Returns the Django form Widget to be used for
        the text area
        """
        if USE_TINYMCE and "tinymce" in settings.INSTALLED_APPS:
            from cms.plugins.text.widgets.tinymce_widget import TinyMCEEditor
            return TinyMCEEditor(installed_plugins=plugins)
        else:
            return WYMEditor(installed_plugins=plugins)

    def get_form_class(self, request, plugins):
        """
        Returns a subclass of Form to be used by this plugin
        """
        # We avoid mutating the Form declared above by subclassing
        class FaqEntryPluginForm(self.form):
            pass

        widget = self.get_editor_widget(request, plugins)
        FaqEntryPluginForm.declared_fields["body"] = CharField(widget=widget, required=False)
        return FaqEntryPluginForm

    def get_form(self, request, obj=None, **kwargs):
        plugins = plugin_pool.get_text_enabled_plugins(self.placeholder)
        form = self.get_form_class(request, plugins)
        kwargs['form'] = form # override standard form
        return super(CMSFaqEntryPlugin, self).get_form(request, obj, **kwargs)

    def render(self, context, instance, placeholder):
        context.update({
            'body':plugin_tags_to_user_html(instance.body, context, placeholder),
            'topic':instance.topic,
            'placeholder':placeholder,
            'object':instance
        })
        return context

plugin_pool.register_plugin(CMSFaqEntryPlugin)


class CMSFaqListPlugin(CMSPluginBase):
    """Lists all FaqEntry plugins on the same page as this plugin"""

    model = FaqList
    name = _("FAQ List")
    render_template = "plugins/cmsplugin_faq/faq_list.html"
    
    def render(self, context, instance, placeholder):
        import pprint

#        pprint.pprint(dir(instance))
#        pprint.pprint(dir(instance.page.cmsplugin_set))
#        plugins = instance.page.cmsplugin_set.all()
#        pprint.pprint(plugins)

        #get all FaqEntryPlugin on this page
        plugins = instance.page.cmsplugin_set.filter(plugin_type='CMSFaqEntryPlugin')
#        pprint.pprint(plugins)
        
        faqentry_plugins = []

        #make a list of the faqentry plugin objects
        for plugin in plugins:
            faqentry_plugins.append(plugin.faqentry)
#            pprint.pprint(plugin.faqentry.topic)
#            pprint.pprint(dir(plugin.faqentry.topic))

        context.update({'faq_list':faqentry_plugins, 'placeholder':placeholder})
        context.update({'css' : instance.get_css_display()})
        return context

plugin_pool.register_plugin(CMSFaqListPlugin)