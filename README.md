# botnoi_dse_g8 scraper

Note: assume to run from command line (mine is Mac's terminal) and you are in the project directory

## Prequisites

1. Python 3.8+
2. virtualenv (recommended)
3. pip

## Setup virtualenv

```
% virtualenv env
```

1. Use environment (if virtualenv is installed or skip to No.2)

```
% source env/bin/activate
```

2. Install dependencies/requirements

```
% pip install -r requirements.txt
```

1. To scraper livinginsider.com

```
% scrapy runspider -o data/livinginsider.csv livinginsider_com/livinginsider_com/spiders/houses_spider.py
```

4. To clean data

```
% rm -fr data/*
```
