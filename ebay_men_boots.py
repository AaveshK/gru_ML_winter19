# -*- coding: utf-8 -*-
import scrapy


class EbayMenBootsSpider(scrapy.Spider):
    name = 'ebay_men_boots'
    start_urls = ['https://www.ebay.com/b/Mens-Boots/11498/bn_56522']
    def parse(self, response):
        #Extract data using css selectors
        item_name=response.css('.s-item__title::text').extract()
        price=response.css('.s-item__price::text').extract()

        #Making extracted data row wise
        for item in zip(item_name,price):
        #create a dictionary to store the scraped info
            scraped_info = {
                'item_name': item[0], #item[0] means product in the list and so on,, i index tells what value to assign
                'price' : item[1],
            }

        #yiled or give the scraped info to scrapy
        yield scraped_info
