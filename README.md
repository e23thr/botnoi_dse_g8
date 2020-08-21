# botnoi_dse_g8 scraper

## Prequisites

1. Python 3.8+
2. virtualenv
3. pip or pip3

## Setup

1. Use environment

```
% source env/bin/activate
```

2. Install dependencies/requirements

```
% pip install -r requirements.txt
```

1. To scraper livinginsider.com

```
% scrapy runspider -o data/livinginsider.json livinginsider_com/livinginsider_com/spiders/houses_spider.py
```

4. To clean data

```
% rm -fr data/*
```
