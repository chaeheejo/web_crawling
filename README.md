# web_crawling
Web crawling in MAC with python.

## Document
[document](https://blog.naver.com/60cogml/223157006828) in Korean

## Installation
```bash
$ pip install requests
$ pip install bs4
```

## Usage
```python
#assign crawling address
address = "your address"

#parsing
value = soup.find("your tag", {"class" : "your class name"})

#get text
text = value.get_text()
```

## Current output
```
Today Exchange Rate
1,300.00
```
