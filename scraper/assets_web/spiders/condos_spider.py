import scrapy
import re
import time
import sys


class CondosSpider(scrapy.Spider):
    name = "condos"

    def start_requests(self):
        # url = "https://www.livinginsider.com/searchword/Condo/Buysell/1/%E0%B8%A3%E0%B8%A7%E0%B8%A1%E0%B8%9B%E0%B8%A3%E0%B8%B0%E0%B8%81%E0%B8%B2%E0%B8%A8-%E0%B8%82%E0%B8%B2%E0%B8%A2-%E0%B8%84%E0%B8%AD%E0%B8%99%E0%B9%82%E0%B8%94.html"
        url = 'https://www.livinginsider.com/living_zone/13/Condo/Buysell/1/%E0%B8%A3%E0%B8%B1%E0%B8%8A%E0%B8%94%E0%B8%B2-%E0%B8%AB%E0%B9%89%E0%B8%A7%E0%B8%A2%E0%B8%82%E0%B8%A7%E0%B8%B2%E0%B8%87.html'
        yield scrapy.Request(url=url, callback=self.parse_listing_page)

    def parse_listing_page(self, response):
        print("Scraping: ", response.url)
        list_selector = ".istock-list:not(.sticky):not(.sticky-banner) > div.item-desc a::attr(href)"
        urls = response.css(list_selector).getall()
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse_data)
        next_page_url = ""
        paginates = response.css("ul.pagination > li > a")
        for anchor in paginates:
            anchor_text = anchor.css("*::text").get()
            if anchor_text.find("Next") != -1:
                next_page_url = anchor.css("*::attr(href)").get()
        if (next_page_url != ""):
            yield scrapy.Request(url=next_page_url, callback=self.parse_listing_page)

    def parse_data(self, response):
        print("Parsing data", response.url)
        thumbs_list = response.css(
            'img.mbSlideDown::attr(src)').getall()
        if len(thumbs_list) < 1:
            print("Error no thumb list", response.url)
            sys.exit(1)

        # for idx, thumb in enumerate(thumbs_list):
        idx = 0
        thumb = thumbs_list[idx]
        yield {
            "url": response.url,

            "description": response.css("#detail-topic h1.font-Sarabun::text").get().strip(),

            "price": response.css("#detail-topic p.price-detail::text").get().strip(),

            "area": re.sub("\<\/div\>", "", re.sub(r"^\<.+\<img.+\"\>", "", "".join(response.css("#property-inform>div.row>div:nth-last-child(2)").get().splitlines()))),

            "bedrooms": re.sub("\<\/div\>", "", re.sub(r"^\<.+\<img.+\"\>", "", "".join(response.css("#property-inform>div.row>div:nth-last-child(1)>div:nth-child(1)").get().splitlines()))),

            "restrooms": re.sub("\<\/div\>", "", re.sub(r"^\<.+\<img.+\"\>", "", "".join(response.css("#property-inform>div.row>div:nth-last-child(1)>div:nth-child(2)").get().splitlines()))),

            "floors": re.sub("\<\/div\>", "", re.sub(r"^\<.+\<img.+\"\>", "", "".join(response.css("#property-inform>div.row>div:nth-last-child(1)>div:nth-child(3)").get().splitlines()))),

            "images": thumb,

            "image_index": idx
        }
