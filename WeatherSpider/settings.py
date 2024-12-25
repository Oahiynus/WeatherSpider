BOT_NAME = 'WeatherSpider'
SPIDER_MODULES = ['WeatherSpider.spiders'] 
NEWSPIDER_MODULE = 'WeatherSpider.spiders'
ITEM_PIPELINES = {
'WeatherSpider.pipelines.WeatherspiderPipeline':1,
}