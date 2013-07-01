from django.conf import settings
from django.template import loader, Context, Library
import feedparser

register = Library()

@register.simple_tag
def rss_widget(template_name='', feed_url=''):
    template_name = template_name or getattr(settings, 'RSS_WIDGET', {}).get('template_name', '')
    feed_url = feed_url or getattr(settings, 'RSS_WIDGET', {}).get('feed_url', '')
    feed = feedparser.parse(feed_url)
    template = loader.get_template(template_name)
    return template.render(Context({'feed': feed}))
