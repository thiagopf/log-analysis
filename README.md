# Log-Analysis

The log-analysis program gets data from the news database and creates 3 report files.

The news database is made in PostgreSQL and was made for a news website. It has 3 tables: authors,log and articles.

*Database news*

authors(name,bio,id)  
log(path,ip,method,status,time,id)  
articles(author,title,slug,lead,body,time,id)

*The report files that are created,contains:*

1 - The 3 most view articles.  
2 - The authors who has most views articles.  
3 - The day which has more than 1% of request errors.

## Getting Started

### Prerequisites

What things you need to install the software

```
Python 2.7
Vagrant
VirtualBox
psycopg2
```
### Installing

#### Python 2.7
```
$ sudo apt install python2.7
```
#### psycopg2
```
sudo pip install psycopg2
```

#### VirtualBox
Download and install virtualbox from https://www.virtualbox.org/wiki/Downloads

#### Vagrant
Download and install from https://www.vagrantup.com/downloads.html

#### Log-analysis

Clone the GitHub repository

```
$ git clone https://github.com/thiagopf/log-analysis.git
```
Or Download the GitHub repository

```
Opens https://github.com/thiagopf/log-analysis.git on web browser
Click on 'Clone or download' and 'Download ZIP'
```

### Configurations


#### Virtual Machine
How to setup the virtual Machine. First get the machine Configurations.
```
git clone git@github.com:udacity/fullstack-nanodegree-vm.git
```
Now you have a new folder. Get inside the folder called vagrant like this:
```
$ cd FSND-Virtual-Machine/vagrant/
```
Start your VM
```
$ vagrant up
```
Log on VM
```
$ vagrant ssh
```
#### Create views
Create the views on the news db.
##### top10articles
```
CREATE VIEW top10articles as SELECT articles.title, count(log.path) as views
FROM log JOIN articles ON log.path = concat('/article/', articles.slug)
GROUP BY articles.title, log.path
ORDER BY views DESC
LIMIT 10;
```

##### top10authors
```
CREATE VIEW top10authors as SELECT authors.name, count(log.path) as views
FROM log, articles, authors
WHERE log.path = concat('/article/', articles.slug) and authors.id = articles.author
GROUP BY authors.name
ORDER BY views DESC
LIMIT 10;
```
##### percentage_errors_day
```
CREATE VIEW percentage_errors_day as
SELECT *, cast((errors * 100)/cast(views as float) as decimal(18,2)) as percentage
FROM (select to_char(time,'FMMonth DD,YYYY') as data,
count(CASE WHEN status <> '200 OK' then 1 ELSE NULL END) as errors,
count(status) as views
FROM log
GROUP BY data
ORDER BY errors DESC) as t_table;
```


### Running
Just run the log.py file
```
$ python log.py
```

## Authors

* **Thiago Pereira Fernandes** - *Initial work* - [thiagopf](https://github.com/thiagopf)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details
