# Database

## What is a Database (DB)?

- Any collection of related information.
    - Phone book.
    - Shopping list.
    - Todo list.
- Databases can be stored in different ways:
    - On paper.
    - In your mind.
    - On a computer.
- Computers are great at keeping track of large amounts of information.

## Database Management Systems (DBMS)

- A special software program that helps users create and maintain a database.
    - Makes it easy to manage amounts of information.
    - Handles Security: only certain people with usernames and passwords can access the data.
    - Backups.
    - Importing/exporting data.
    - Concurrency.
    - Interacts with software applications.
        - Programming languages.
- CRUD (Create | Read/Retrieve | Update | Delete) are the core four operations the DBMS perform.

## Types of Databases

| Relational Databases (SQL) | Non-Relational Database (noSQL/not only SQL) |
|---|---|
| Organize data into one or more tables | Organize data in anything but a traditional table |
| - Each table has columns and rows | - Key-value stores |
| - A unique key identifies each row | - Documents (JSON, XML, etc) |
|| - Graphs |
|| - Flexible tables. |

## Relational Databases (SQL)

- **Relational Database Management Systems (RDBMS):**
    - Help users create and maintain a relational database.
        - MySQL, Oracle, PostgreSQL, MariaDB, etc.
- **Structured Query Language (SQL):**
    - Standardize language for interacting with RDBMS.
    - Used to perform CRUD operations, as well as other administrative tasks (user management, security, backup, etc).
    - Used to define tables and structures.
    - SQL code used on one RDBMS is not always portable to another without modification.

## Non-Relational Databases (noSQL / not only SQL)

- **Non-Relational Database Management Systems (NRDBMS):**
    - Help users create and maintain a non-relational database.
        - MongoDB, DynamoDB, Apache Cassandra, firebase, etc.
- **Implementation Specific:**
    - Any non-relational database falls under this category, so there's no set language standard.
    - Most NRDBMS will implement their own language for preforming CRUD and administrative operations on the database.

## Database Queries

- Queries are requests made to the DBMS for specific information.
- A google search is a query.

## Tables and Keys

- Tables consist of columns and rows:
    - a column represents a single _attribute_.
    - a row represents an entry/actual data.
- **Primary key:**
    - an attribute which uniquely defines the row in the DB.
    - Types:
        - Surrogate Key: 
            - an artificial, unique identifier added to the table for database management purposes.
            - it has no inherent meaning outside the database system.
            - Examples: auto incrementing integers or Global Unique Identifiers (GUIDs/UUIDs).
        - Natural Key:
            - a column (or combination of columns) that already exists in the real world, and serves as a unique identifier for a record.
            - Examples: Social Security Number (SSN) or International Standard Book Number (ISBN), etc.
- **Foreign Key:**
    - an attribute we can store on a database table that will link us to another database table.
    - stores the primary key of a row in another table.
- **Composite Key:**
    - a primary key that needs two or more attributes to uniquely identify each row.

## Structured Query Language (SQL)

- SQL is a language used for interaction with RDBMS.
    - You can use SQL to get the RDBMS to do things for you.
        - Create, retrieve, update, and delete data.
        - Create and manage databases.
        - Design and create database tables.
        - Perform administration tasks(security, user management, import/export, etc).
- SQL implementations vary between systems.
    - Not all RDBMS' follow the SQL standard to a 'T'.
    - The concepts are the same but the implementation may vary.
- SQL is a hybrid language, it's basically 4 types of languages in one.
    - **Data Query Language (DQL)**
        - Used to query the database for information.
        - Get information that is already stored there.
    - **Data Definition Language (DDL)**
        - Used for defining database schemas.
    - **Data Control Language (DCL)**
        - Used for controlling access to the data in the DB.
        - User and permissions management.
    - **Data Manipulation Language (DML)**
        - Used for inserting, updating, and deleting data from the DB.

## Basic Data Types

- INT: whole numbers.
- DECIMAL(M, N): decimal numbers, exact value.
- VARCHAR(L): string of text of length L. 
- BLOB: binary large object, stores large data.
- DATE: 'YYYY-MM-DD'
- TIMESTAMP: 'YYYY-MM-DD HH:MM::SS'
