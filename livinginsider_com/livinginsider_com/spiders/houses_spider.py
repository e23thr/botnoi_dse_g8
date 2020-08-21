import scrapy


class HousesSpider(scrapy.Spider):
    name = "houses"

    def start_requests(self):
        url = 'https://www.livinginsider.com/searchword/Home/Buysell/1/%E0%B8%A3%E0%B8%A7%E0%B8%A1%E0%B8%9B%E0%B8%A3%E0%B8%B0%E0%B8%81%E0%B8%B2%E0%B8%A8-%E0%B8%82%E0%B8%B2%E0%B8%A2-%E0%B8%9A%E0%B9%89%E0%B8%B2%E0%B8%99.html'
        while url != None:
            yield scrapy.Request(url=url, callback=self.parse_list, method="POST")
            url = None

    def parse_list(self, response):
        row = response.css("section.block-inside > .container > .row")[-1]
        print(len(row.css(".istock-list .item-desc a")))
        for item in row.css(".istock-list"):
            url = item.css(".item-desc a::attr(href)").get()
            yield scrapy.Request(url=url, callback=self.parse_data)

    def parse_data(self, response):
        thumbs_list = response.css(
            '#overview > .fotorama.visible-xs > img::attr(src)')
        # thumbs_list = thumbs_list.css('.fotorama__wrap')
        yield {
            "url": response.url,
            "area": response.css(".web-head-capacity-detail.hidden-xs>div>div")[0].css("div::text").getall(),
            "images": thumbs_list.getall()
        }
