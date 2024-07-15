from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from website.models import Property

class StaticViewSitemap(Sitemap):
    priority = 0.5
    changefreq = 'daily'
    
    def items(self):
        return ['website:index','website:property' ,'website:about', 'website:contact']
    
    def location(self, item):
        return reverse(item)

class PropertySitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.5

    def items(self):
        return Property.objects.filter(status=True)

    def lastmod(self, obj):
        return obj.published_date
       



