import scrapy
from scrapy.loader import ItemLoader
from oscar_winners.items import MovieItem

class OscarWinnersSpider(scrapy.Spider):
    #identity
    name = 'oscarwinners'

    #requests
    def start_requests(self):
        url= "https://www.imdb.com/list/ls053710248/"

        yield scrapy.Request(url=url, callback=self.parse)
        
    def parse(self, response):
        for movie in response.selector.xpath("//div[@class='lister-item-content']"):
            loader = ItemLoader(item= MovieItem(), selector=movie, response= response)
            loader.add_xpath('Title',".//h3[@class='lister-item-header']/a")
            loader.add_xpath('Rating',".//div[@class='ipl-rating-star small']//span[2]")
            loader.add_xpath('Genre',".//p[@class='text-muted text-small'][1]/span[5]")

            yield loader.load_item()

        