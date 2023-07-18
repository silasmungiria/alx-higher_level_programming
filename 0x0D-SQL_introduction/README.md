# 0x0D. SQL - Introduction

This repository contains solutions to the tasks of the "0x0D. SQL - Introduction" project, which is part of the ALX Higher Level Programming curriculum. The project focuses on SQL and MySQL concepts, covering various tasks related to creating databases, tables, executing queries, and performing data manipulation.

## Concepts

The project covers the following concepts:

- Databases
- Databases

## Resources

Before starting the project, it is recommended to review the following resources:

- [What is Database & SQL?](https://www.youtube.com/watch?v=FR4QIeZaPeM)
- [A Basic MySQL Tutorial](https://www.digitalocean.com/community/tutorials/a-basic-mysql-tutorial)
- [Basic SQL statements: DDL and DML](https://www.studytonight.com/dbms/basic-sql-statements-ddl-and-dml)
- [Basic queries: SQL and RA](https://www.studytonight.com/dbms/basic-queries-sql-and-ra)
- [SQL technique: functions](https://www.studytonight.com/dbms/sql-technique-functions)
- [SQL technique: subqueries](https://www.studytonight.com/dbms/sql-technique-subqueries)
- [What makes the big difference between a backtick and an apostrophe?](https://stackoverflow.com/questions/29402316/what-makes-the-big-difference-between-a-backtick-and-an-apostrophe)
- [MySQL Cheat Sheet](https://www.sqltutorial.org/sql-cheat-sheet/)
- [MySQL 8.0 SQL Statement Syntax](https://dev.mysql.com/doc/refman/8.0/en/sql-statements.html)
- [Installing MySQL in Ubuntu 20.04](https://www.digitalocean.com/community/tutorials/how-to-install-mysql-on-ubuntu-20-04)

## Learning Objectives

By the end of this project, you should be able to explain the following concepts to anyone, without the help of Google:

- General
  - What's a database?
  - What's a relational database?
  - What does SQL stand for?
  - What's MySQL?
  - How to create a database in MySQL?
  - What do DDL and DML stand for?
  - How to create or alter a table?
  - How to select data from a table?
  - How to insert, update, or delete data?
  - What are subqueries?
  - How to use MySQL functions?

## Requirements

- Allowed editors: vi, vim, emacs
- All your files will be executed on Ubuntu 20.04 LTS using MySQL 8.0 (version 8.0.25)
- All your files should end with a new line
- All your SQL queries should have a comment just before (i.e., syntax above)
- All your files should start with a comment describing the task
- All SQL keywords should be in uppercase (SELECT, WHERE...)
- A `README.md` file, at the root of the folder of the project, is mandatory
- The length of your files will be tested using `wc`

## Usage

To run the SQL scripts, follow these steps:

1. Install MySQL 8.0 on Ubuntu 20.04 LTS:
   ```
   $ sudo apt update
   $ sudo apt install mysql-server
   $ mysql --version
   ```

2. Connect to your MySQL server:
   ```
   $ sudo mysql
   ```

3. Execute the SQL scripts:
   ```
   mysql> source file.sql
   ```

Note: Replace `file.sql` with the name of the SQL script you want to execute.

## Tasks

### 0. List databases
- Script: [0-list_databases.sql](./0-list_databases.sql)

### 1. Create a database
- Script: [1-create_database_if_missing.sql](./1-create_database_if_missing.sql)

### 2. Delete a database
- Script: [2-remove_database.sql](./2-remove_database.sql)

### 3. List tables
- Script: [3-list_tables.sql](./3-list_tables.sql)

### 4. First table
- Script: [4-first_table.sql](./4-first_table.sql)

### 5. Full description
- Script: [5-full_table.sql](./5-full_table.sql)

### 6. List all in table
- Script: [6-list_values.sql](./6-list_values.sql)

### 7. First add
- Script: [7-insert_value.sql](./7-insert_value.sql)

### 8. Count 89
- Script: [8-count_89.sql](./8-count_89.sql)

### 9. Full creation
- Script: [9-full_creation.sql](./9-full_creation.sql)

### 10. List by best
- Script: [10-top_score.sql](./10-top_score.sql)

### 11. Select the best
- Script: [11-best_score.sql](./11-best_score.sql)

### 12. Cheating is bad
- Script: [12-no_cheating.sql](./12-no_cheating.sql)

### 13. Score too low
- Script: [13-change_class.sql](./13-change_class.sql)

### 14. Average
- Script: [14-average.sql](./14-average.sql)

### 15. Number by score
- Script: [15-groups.sql](./15-groups.sql)

### 16. Say my name
- Script: [16-no_link.sql](./16-no_link.sql)

### 17. Go to UTF8
- Script: [100-move_to_utf8.sql](./100-move_to_utf8.sql)

### 18. Temperatures #0
- Script: [101-avg_temperatures.sql](./101-avg_temperatures.sql)

### 19. Temperatures #1
- Script: [102-top_city.sql](./102-top_city.sql)

### 20. Temperatures #2
- Script: [103-max_state.sql](./103-max_state.sql)

**Note:** Each task has its corresponding SQL script file that should be executed to accomplish the task.

## Author

- Guillaume, Software Engineer at ALX

