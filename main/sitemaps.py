from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse

class StaticViewSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.5

    def items(self):
        return [
            'home',
            'about',
            'contact',
            'portfolio',
            'services',
            'industrial_gases',
            'medical_gases',
            'cryogenic_equipment',
            'gas_cylinders',
            'gas_installations',
            'technical_services',
        ]

    def location(self, item):
        return reverse(item)
