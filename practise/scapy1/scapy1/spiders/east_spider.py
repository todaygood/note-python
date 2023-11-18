
import scrapy

class DmozSpider(scrapy.Spider):
    name = "dmoz"

    start_urls = [
        "https://www.solarbe.com/"

    ]

    def parse(self, response):
        filename = "solarbe.html"
        print("-------",filename)
        with open(filename, 'wb') as f:
            f.write(response.body)