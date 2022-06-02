import scrapy


def scrapy_page(url, parse_page = None):
    """
    Scrapy a page and return the content
    """
    return scrapy.Request(url=url)


url = "https://questure.poliziadistato.it/servizio/stranieri/?lang=italian&mime=1&pratica=20FI037333&invia=Invia"
page = scrapy_page(url, "div.content")

print(page.headers)
