import os

class Config:
NEWS_API_KEY = '6923221c2b374f8bbb9e30c6e2cbcfd1'
NEWS_API_SOURCE_URL ='https://newsapi.org/v2/everything?language=en&sources={}&apiKey={}'
CAT_API_URL='https://newsapi.org/v2/top-headlines?country=us&category={}&apiKey={}'

class ProductionConfig(Config):
    '''
    '''
    pass


class DevelopmentConfig(Config):
    '''
    '''
    DEBUG=True

config_options = {
    'dev': DevelopmentConfig,
    'prod': ProductionConfig
}
