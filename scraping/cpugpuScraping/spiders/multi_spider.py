import scrapy

from scrapy.http import JsonRequest
from scrapy.crawler import CrawlerProcess

apikey = 90294

class CpusSpider(scrapy.Spider):
    name = "cpus"

    def start_requests(self):
        urls = [
            'https://www.techpowerup.com/cpu-specs/?released=2020&sort=name',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)            

    def parse(self, response):
        company_name = ""
        for cpu in response.xpath('//*[@class="processors"]//tr'):

            current_company_name = cpu.xpath('*[@class="mfgr"]//text()').extract_first()
            if current_company_name == "AMD":
                company_name = current_company_name

            if current_company_name == "Intel":
                company_name = current_company_name

            data = {
                'company' : company_name,
                'product_name': cpu.xpath('td[1]//a//text()').extract_first(),
                'code_name': cpu.xpath('td[2]//text()').extract_first(),
                'cores': cpu.xpath('td[3]//text()').extract_first(),
                'clock': cpu.xpath('td[4]//text()').extract_first(),
                'socket': cpu.xpath('td[5]//text()').extract_first(),
                'process': cpu.xpath('td[6]//text()').extract_first(),
                'l3_cache': cpu.xpath('td[7]//text()').extract_first(),
                'tdp': cpu.xpath('td[8]//text()').extract_first(),
                'released': cpu.xpath('td[9]//text()').extract_first(),
            }    

            # print(data)  

            yield data     

            # yield JsonRequest(url='http://localhost/api/cpu/add', headers={'X-AUTH-TOKEN':apikey}, data=data)

class GpusSpider(scrapy.Spider):
    name = "gpus"

    def start_requests(self):
        urls = [
            'https://www.techpowerup.com/gpu-specs/?released=2020&sort=name',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)            

    def parse(self, response):
        company_name = ""
        for gpu in response.xpath('//*[@class="processors"]//tr'):

            current_company_name = gpu.xpath('*[@class="mfgr"]//text()').extract_first()
            if current_company_name == "AMD":
                company_name = current_company_name

            if current_company_name == "Intel":
                company_name = current_company_name

            if current_company_name == "NVIDIA":
                company_name = current_company_name  
                
            data = {
                'company' : company_name,
                'product_name': gpu.xpath('td[1]//a//text()').extract_first(),
                'gpu_chip': gpu.xpath('td[2]//a//text()').extract_first(),
                'release_date': gpu.xpath('td[3]//text()').extract_first(),
                'bus': gpu.xpath('td[4]//text()').extract_first(),
                'memory': gpu.xpath('td[5]//text()').extract_first(),
                'gpu_clock': gpu.xpath('td[6]//text()').extract_first(),
                'memory_clock': gpu.xpath('td[7]//text()').extract_first(),
            }                  

            # print(data)

            yield data       

            # yield JsonRequest(url='http://localhost/api/gpu/add', headers={'X-AUTH-TOKEN':apikey}, data=data)

#process = CrawlerProcess()
#process.crawl(CpusSpider)
#process.crawl(GpusSpider)
#process.start()