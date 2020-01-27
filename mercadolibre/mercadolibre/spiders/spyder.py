import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from mercadolibre.Item import MercadolibreItem
from scrapy.exception import CloseSpider

class MercadoSpider(CrawlSpider):

	name = 'mercado'
	item_count = 0
	
	allowed_domain = ['www.mercadolibre.com.mx']
	starts_urls = ['https://listado.mercadolibre.com.mx/impresoras#D[A:impresoras]']

	rules = {
		Rule(LinkExtractor(allow = (),restrict_xpath = ('//li[@class="andes-pagination__button andes-pagination__button--next"]/a')))
		Rule(LinkExtractor(allow = (),restrict_xpath = ('//h2[@class = "item__title list-view-item-title"]')),
			callback = 'parse_item', follow = False)

	}

	def parse_item(self, response):
		mml_item = MercadolibreItem()
		
		#info del producto
		ml_item['titulo'] = response.xpath('normalize-space(//*[@id="root-app"]/div/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/h1/text())').extract()
		ml_item['precio'] = response.xpath('normalize-space(//*[@id="root-app"]/div/div[2]/div[1]/div[1]/div[1]/div[2]/div[2]/div/div/span/span[2]/text())').extract()
		self.item_count += 1

		if self.item > 20:
			raise CloseSpider('Item_exceeded')
		yield ml_item
