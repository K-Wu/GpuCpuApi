# Scraping with Scrapy

https://scrapy.org/


## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

What things you need to install the software and how to install them?

- [Scrapy](https://scrapy.org/download/)

#### Before 

Go to your database and take admin **api_key**.

Remplace **apiKey** in <em>spiders/multi_spider.py</em>.

#### Run
In /scraping, execute the following command:

```bash
scrapy crawl -O ./out.json ssds
```

Great Scrapy Quick Started Example: https://www.trickster.dev/post/scrapy-simplified-developing-a-single-file-web-scraper/
