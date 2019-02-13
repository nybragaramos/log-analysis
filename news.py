#!/usr/bin/env python3
import psycopg2
DBNAME = "news"


# Query data from the database, open and close the connection
def query_db(request):
    conn = psycopg2.connect(database=DBNAME)
    cursor = conn.cursor()
    cursor.execute(request)
    results = cursor.fetchall()
    conn.close()
    return results


# query the 3 most popular post, most popular first
query_pop_articles = """SELECT title, COUNT(*) AS views
    FROM articles, log
    WHERE path LIKE concat('%', slug, '%')
    GROUP BY path, title
    ORDER BY views DESC
    LIMIT 3;"""


# query all authors, most popular first
query_pop_authors = """SELECT name, COUNT(*) AS views
    FROM articles, authors, log
    WHERE authors.id = articles.author
    AND path LIKE concat('%', slug, '%')
    GROUP BY name
    ORDER BY views DESC;
    """


# query the days where the error rate is greater then 1%
query_days_high_error = """WITH error_requests AS (
       SELECT time::date AS day, COUNT(*) AS error
       FROM log
       WHERE status NOT LIKE '%200%'
       GROUP BY day
       ORDER BY day DESC
      ), all_requests AS (
       SELECT time::date AS day, COUNT(*)::float AS all
       FROM log
       GROUP BY day
       ORDER BY day DESC
      ), error_rate AS (
       SELECT error_requests.day AS day,
          (error_requests.error*100/all_requests.all) AS rate
       FROM error_requests, all_requests
       WHERE error_requests.day = all_requests.day
      )
    SELECT day, concat(ROUND(rate::numeric, 2),'%')
    FROM error_rate
    WHERE rate >=1
    ORDER BY rate DESC
    """


# call the queries and write the result at the log file
def write_to_log_file(title, query, complement, file):
    result = query_db(query)
    file.write("\n\n" + title + "\n\n")
    for text, num in result:
        file.write("{} -- {} {}\n".format(text, num, complement))


def main():
    f = open("news_log.txt", "w+")

    f.write("NEWS LOG\n")

    write_to_log_file("The most popular three articles of all time",
                      query_pop_articles, "views", f)
    write_to_log_file("The most popular authors of all time",
                      query_pop_authors, "views", f)
    write_to_log_file("Days with more than 1% of errors in requests",
                      query_days_high_error, "error", f)

    f.close()


if __name__ == "__main__":
    main()
