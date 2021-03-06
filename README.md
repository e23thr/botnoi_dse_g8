# botnoi_dse_g8 scraper

Note: assume to run from command line (mine is Mac's terminal) and you are in the project directory

## Prequisites

1. Python 3.8+
2. pip
3. virtualenv (recommended) [How to install](https://virtualenv.pypa.io/en/latest/installation.html)

## (Optional) Install virtualenv using pip

```
% python -m pip install --user virtualenv
```

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

## To scrape data from website

Before scraping you have to be in livinginsider_com directory by running command below

```
% cd scraper
```

### Scrape houses and save to csv file

```
% scrapy crawl -o ../data/houses.csv houses
```

### Scrape condos and save to csv file

```
% scrapy crawl -o ../data/condos.csv condos
```

## To clean data

```
% rm -fr data/*
```
