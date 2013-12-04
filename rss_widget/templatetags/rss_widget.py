from django.conf import settings
from django.template import loader, Context, Library
import feedparser

register = Library()

@register.simple_tag
def rss_widget(template_name='', feed_url=''):
    _settings = getattr(settings, 'RSS_WIDGET', {})
    template_name = template_name or _settings.get('template_name', '')
    feed_url = feed_url or _settings.get('feed_url', '')
    feed = feedparser.parse(feed_url)
    template = loader.get_template(template_name)
    return template.render(Context({'feed': feed}))
