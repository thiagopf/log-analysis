#!/usr/bin/env python
# -*- coding: utf-8 -*-
import psycopg2


def report_creator(conn, query, vars=None, file_name="report.txt"):
    '''
    Creates a report file with the result of the query
    :param conn: The connection with db
    :param query: The query to be executed
    :param vars: In case your query has variable
    :param file_name: Name of the file
    '''
    # Create a file
    file = open(file_name, 'w')

    # Open a cursor to perform database operations
    cur = conn.cursor()

    # Query the database and obtain data as Python objects
    cur.execute(query, vars)
    rows = cur.fetchall()

    # Write the values on the file
    for values in rows:
        file.write(' —— '.join(str(x) for x in values)+'\n')

    cur.close()
    print('Report file created: %s' % file_name)


if __name__ == "__main__":
    # Connect to an existing database
    conn = psycopg2.connect("dbname=news")
    # Create the report about the most view articles
    report_creator(conn, 'select title, concat(views::varchar,%s) as views \
                         from top10articles limit 3;', vars=(' views',),
                         file_name="toparticles.txt")
    # Create the report about the view articles by authors
    report_creator(conn, 'select name, concat(views::varchar,%s) as views \
                         from top10authors;', vars=(' views',),
                         file_name="topauthors.txt")
    # Create the report about the percentage of errors per day greater than 1
    report_creator(conn, 'select data, concat(percentage,%s) as percentage \
                         from percentage_errors_day where percentage > 1;',
                         vars=('% errors',), file_name="errors.txt")
    conn.close()
