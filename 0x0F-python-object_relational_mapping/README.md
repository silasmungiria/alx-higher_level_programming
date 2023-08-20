# 0x0F. Python - Object-relational mapping

![Python](https://img.shields.io/badge/Python-3.8.5-blue)
![MySQL](https://img.shields.io/badge/MySQL-8.0-green)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-1.4.x-orange)

This repository contains a series of Python scripts and classes that demonstrate the use of Object-Relational Mapping (ORM) techniques with MySQL databases. The scripts use various modules, including MySQLdb and SQLAlchemy, to interact with the database.

## Table of Contents
- [Background Context](#background-context)
- [Installation](#installation)
- [Usage](#usage)
- [Tasks](#tasks)
- [Contributing](#contributing)
- [License](#license)

## Background Context
In this project, we explore the interaction between Python and databases. Two main techniques are used:

1. Using the `MySQLdb` module to connect to a MySQL database and execute SQL queries.
2. Utilizing the `SQLAlchemy` module, which is an Object-Relational Mapping (ORM) library, to abstract the interaction with the database.

## Installation
Before running the scripts in this repository, you need to install the required dependencies. Make sure you have Python 3.8.5, MySQL 8.0, MySQLdb 2.0.x, and SQLAlchemy 1.4.x installed. You can install the necessary modules using the following commands:

```bash
sudo apt-get install python3-dev
sudo apt-get install libmysqlclient-dev
sudo apt-get install zlib1g-dev
sudo pip3 install mysqlclient
sudo pip3 install SQLAlchemy
```

## Usage
1. Clone this repository to your local machine.
2. Navigate to the appropriate task directory.
3. Run the desired script using the following command:
```
./script_name.py mysql_username mysql_password database_name [additional_arguments]
```

## Tasks
The repository contains scripts and classes that fulfill various tasks. Each task demonstrates different aspects of object-relational mapping and database interaction. The tasks include:

- [**Task 0: Get all states**](./0-select_states.py)
- [**Task 1: Filter states**](./1-filter_states.py)
- [**Task 2: Filter states by user input**](./2-my_filter_states.py)
- [**Task 3: SQL Injection protection**](./3-my_safe_filter_states.py)
- [**Task 4: Cities by states**](./4-cities_by_state.py)
- [**Task 5: All cities by state**](./5-filter_cities.py)
- [**Task 6: First state model**](./6-model_state.py)
- [**Task 7: All states via SQLAlchemy**](./7-model_state_fetch_all.py)
- [**Task 8: First state**](./8-model_state_fetch_first.py)
- [**Task 9: Contains `a`**](./9-model_state_filter_a.py)
- [**Task 10: Get a state**](./10-model_state_my_get.py)
- [**Task 11: Add a new state**](./11-model_state_insert.py)
- [**Task 12: Update a state**](./12-model_state_update_id_2.py)
- [**Task 13: Delete states**](./13-model_state_delete_a.py)
- [**Task 14: Cities in state - 14-model_city_fetch_by_state.py**](./14-model_city_fetch_by_state.py)
- [**Task 14: Cities in state - model_city.py**](./model_city.py)
- [**Task 15: City Relationship - relationship_city.py**](./relationship_city.py)
- [**Task 15: City Relationship - relationship_state.py**](./relationship_state.py)
- [**Task 15: City Relationship - 100-relationship_states_cities.py**](./100-relationship_states_cities.py)
- [**Task 16: List Relationship**](./101-relationship_states_cities_list.py)
- [**Task 17: From City**](./102-relationship_cities_states_list.py)

Each task is contained in a separate script or class file. To understand the details of each task, refer to the individual scripts.

## Contributing
Contributions to this project are welcome! If you find any issues or want to improve the code, feel free to create a pull request.

## License
This project is licensed under the [MIT License](LICENSE).
