## pkdex

一个简单的爬虫，用来爬取[口袋百科](http://www.pokemon.name/wiki/%E5%AE%9D%E5%8F%AF%E6%A2%A6%E5%88%97%E8%A1%A8)的精灵信息。并存在pokedex.json文件中。该网站的[robots.txt](http://www.pokemon.name/robots.txt)

### 使用

```
python spider_man.py
```

### 项目说明

#### 爬虫架构

- 爬虫调度器：统筹以下模块

- URL管理器：管理URL链接，维护已经爬取的URL和未爬取的URL集合

- HTML下载器：从URL管理器中获取未爬取的链接，并下载

- HTML解析器：获取HTML下载器下载的网页，从中解析出新的URL链接给URL管理器，解析出数据给数据存储器

- 数据存储器：将数据存储在文件或者数据库中

### TODO

- 增量爬取

- 数据库存储
