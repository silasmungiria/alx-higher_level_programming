# 0x0E. SQL - More queries

## Overview
This project contains a series of SQL queries that demonstrate various concepts and techniques related to MySQL databases. The project is part of the higher-level programming curriculum and focuses on working with databases, creating tables, querying data, and managing user privileges.

## Learning Objectives
By completing this project, you will be able to:

- Create a new MySQL user and grant privileges to a database or table.
- Understand the concepts of PRIMARY KEY and FOREIGN KEY.
- Use NOT NULL and UNIQUE constraints to enforce data integrity.
- Retrieve data from multiple tables using JOIN and UNION.
- Work with subqueries to perform complex queries.
- Design and manage relational database models.

## Requirements
- Allowed editors: vi, vim, emacs
- The project should be executed on Ubuntu 20.04 LTS using MySQL 8.0 (version 8.0.25).
- All SQL files should have a comment just before the query describing the task.
- All SQL keywords should be in uppercase (e.g., SELECT, WHERE).
- The project should have a README.md file at the root of the folder with the following instructions.

## How to Use
1. Install MySQL 8.0 on Ubuntu 20.04 LTS:
```bash
$ sudo apt update
$ sudo apt install mysql-server
$ mysql --version
```

2. Connect to your MySQL server:
```bash
$ sudo mysql
```

3. Import the database dump for the project (if applicable):
```bash
$ echo "CREATE DATABASE hbtn_0d_tvshows;" | mysql -uroot -p
Enter password:
$ curl "https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql" -s | mysql -uroot -p hbtn_0d_tvshows
Enter password:
```

4. Run the SQL queries provided in the project to complete the tasks.

## Tasks
1. [My privileges!](./0-privileges.sql)
2. [Root user](./1-create_user.sql)
3. [Read user](./2-create_read_user.sql)
4. [Always a name](./3-force_name.sql)
5. [ID can't be null](./4-never_empty.sql)
6. [Unique ID](./5-unique_id.sql)
7. [States table](./6-states.sql)
8. [Cities table](./7-cities.sql)
9. [Cities of California](./8-cities_of_california_subquery.sql)
10. [Genre ID by show](./10-genre_id_by_show.sql)
11. [Genre ID for all shows](./11-genre_id_all_shows.sql)
12. [No genre](./12-no_genre.sql)
13. [Number of shows by genre](./13-count_shows_by_genre.sql)
14. [My genres](./14-my_genres.sql)
15. [Only Comedy](./15-comedy_only.sql)
16. [List shows and genres](./16-shows_by_genre.sql)
17. [Not my genre](./100-not_my_genres.sql)
18. [No Comedy tonight!](./101-postgres_delete.sql)
19. [Rotten tomatoes](./101-postgres_delete.sql)
20. [Best genre](./101-postgres_delete.sql)

## Note
- Please ensure that you have the required privileges to execute these SQL queries on your MySQL server.
- Make sure to replace "localhost" with the appropriate host if your MySQL server is hosted on a different machine.
