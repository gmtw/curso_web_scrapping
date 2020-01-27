import scrapy

class spider_gdp_dept(scrapy.Spider):
	"""docstring for gdp_dept"""
	name  = 'gdp_dept'
	allowed_domains = ['worldpopulationreview.com']
	start_urls = ['http://worldpopulationreview.com/countries/countries-by-national-debt/']

	def parse(self,response):
		rows = response.xpath('(//table[@class = "table table-striped"]/tbody/tr)')

		for row in rows:
			country_name = row.xpath(".//td[1]/a/text()").get()
			gdp_dept = row.xpath(".//td[2]/text()").get()
			yield {
                'country_name':country_name,
                'gdp_dept': gdp_dept
            }
			





