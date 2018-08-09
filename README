# Log-Analysis

The program creates reports files based on the data from news database.


## Prerequisites

What things you need to install the software

```
Python 2.7
```
## Installing

Clone the GitHub repository

```
$ git clone https://github.com/thiagopf/log-analysis.git
```
Or Download the GitHub repository

```
Opens https://github.com/thiagopf/log-analysis.git on web browser
Click on 'Clone or download' and 'Download ZIP'
```

## Configurations
Create the views on the news db.

### top10articles
```
CREATE VIEW top10articles as SELECT articles.title, count(log.path) as views FROM log JOIN articles ON log.path = concat('/article/', articles.slug) GROUP BY articles.title ORDER BY log.path DESC LIMIT 10;
```
### top10authors
```
CREATE VIEW top10authors as SELECT authors.name, count(log.path) as views FROM log, articles, authors where log.path = concat('/article/', articles.slug) and authors.name = articles.author GROUP BY authors.name ORDER BY views DESC LIMIT 10;
```
### percentage_errors_day
```
CREATE VIEW percentage_errors_day as SELECT *, cast((errors * 100)/cast(views as float) as decimal(18,2)) as percentage FROM (select to_char(time,'FMMonth DD,YYYY') as data,count(CASE WHEN status <> '200 OK' then 1 ELSE NULL END) as errors, count(status) as views FROM log GROUP BY data ORDER BY errors DESC) as t_table;
```


## Running
Just run the log.py file
```
$ python log.py
```

## Authors

* **Thiago Pereira Fernandes** - *Initial work* - [thiagopf](https://github.com/thiagopf)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details
