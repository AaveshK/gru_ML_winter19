# -*- coding: utf-8 -*-
import scrapy


class EbayMenBootsSpider(scrapy.Spider):
    name = 'ebay_men_boots'
    start_urls = ['https://www.ebay.com/b/Mens-Boots/11498/bn_56522']


    def parse(self, response):

        print("procesing:"+response.url)
        #Extract data using css selectors
        product_name=response.css('.s-item__title::text').extract()
        price_range=response.css('.s-item__price::text').extract()
        
        row_data=zip(product_name,price_range)

        #Making extracted data row wise
        for item in row_data:
            #create a dictionary to store the scraped info
            scraped_info = {
                #key:value
                'product_name' : item[0], #item[0] means product in the list and so on, index tells what value to assign
                'price_range' : item[1],
            }

            #yield or give the scraped info to scrapy
            yield scraped_info
