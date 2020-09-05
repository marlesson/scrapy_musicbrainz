# -*- coding: utf-8 -*-
import scrapy
import pandas as pd

class ArtistSpider(scrapy.Spider):
    name       = 'Artist'
    allowed_domains = ['musicbrainz.org']
    df_idx     = pd.read_csv('artist_id_indices.csv')
    start_urls = ['https://musicbrainz.org/artist/'+str(row.artist_id) for i, row in df_idx.iterrows()]



    def parse(self, response):

        name   = response.css("dl.properties dd.sort-name ::text").extract_first() 
        type   = response.css("dl.properties dd.type ::text").extract_first() 
        gender = response.css("dl.properties dd.gender ::text").extract_first() 
        begin_date = response.css("dl.properties dd.begin-date ::text").extract_first() 
        begin_area = response.css("dl.properties dd.begin_area ::text").extract_first() 
        area   = response.css("dl.properties dd.area ::text").extract_first() 
        area   = response.css("dl.properties dd.area ::text").extract_first() 
        rate   = response.css("span.current-rating ::text").extract_first() 
        genre  = "".join(response.css("div.genre-list ::text").extract())
        tags  = "".join(response.css("div#sidebar-tag-list ::text").extract())

        yield {
            'uri': response.url,
            'id': response.url.split("/")[-1],
            'name': name,
            'type': type,
            'gender': gender,
            'begin_date': begin_date,
            'begin_area': begin_area,
            'area': area,
            'genre': genre,
            'tags': tags,
            'rating': rate

        }
#content > div.wikipedia-extract > div