import datetime

class AliexpressItem():

    def __init__(
        self, name: str = None, max_price: int = None, min_price: int = None, image_urls: list = None, 
        url: str = None, thumbnail_url: str = None, discount_rate: float = None, favorite_count: int = None
        ):
        self.name = name
        self.max_price = max_price
        self.min_price = min_price
        self.thumbnail_url = thumbnail_url
        self.image_urls = image_urls
        self.url = url
        self.favorite_count = favorite_count
        self.discount_rate = discount_rate


    def to_dict(self):
        return self.__dict__.copy()
    
