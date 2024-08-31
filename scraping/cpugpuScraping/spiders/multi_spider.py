import scrapy

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


            yield data     


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


            yield data       


class SsdsSpider(scrapy.Spider):
    name = "ssds"

    def start_requests(self):
        urls = [
            'https://www.techpowerup.com/ssd-specs/search/?market=2&released={year}'.format(year=y) for y in range(2014, 2025)
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)            

    def parse(self, response):
        for idx_ssd, ssd in enumerate(response.xpath('//*[@class="drives-desktop-table"]//tr')):
            # The first two rows are empty
            if idx_ssd < 2:
                continue


            data = {
                'product_name': ssd.xpath('td[1]//div//a//text()').extract_first(),
                'max_capacity': ssd.xpath('td[1]//div//div//a[last()]//text()').extract_first(),
                'link': ssd.xpath('td[1]//div//a//@href').extract_first(),
                'type': ssd.xpath('td[2]//text()').extract_first().replace("\n", "").replace("\t", ""),
                'format': ssd.xpath('td[3]//text()').extract_first(),
                'interface': ssd.xpath('td[4]//text()').extract_first(),
                'released': ssd.xpath('td[5]//text()').extract_first(),
                'controller': ssd.xpath('td[6]//text()').extract_first().replace("\n", "").replace("\t", ""),
                'dram': ssd.xpath('td[7]//text()').extract_first().replace("\n", "").replace("\t", ""),
            }    


            yield data     

