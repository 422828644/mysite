from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

from tutorial.items import RunnoItem


class RunnoSpider(CrawlSpider):
    name = "Runno"
    allowed_domains = ["runoob.com"]
    start_urls = [
        'https://www.runoob.com/python3'
    ]
    rules = [Rule(LinkExtractor(allow=['/python3-\S+.html']), callback='parse_runno')]

    def parse_runno(self, response):
        runno = RunnoItem()
        runno['url'] = response.url
        runno['title'] = response.xpath("//div[@id='content']/h1/text()").extract()
        runno['content'] = response.xpath("//div[@class='tutintro']").extract()
        yield runno
        return runno
