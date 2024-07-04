# SQL Notes

## "MySQL in 25 Minutes"

This [video](https://www.youtube.com/watch?v=8kDs8QkFI2Y) gives a quick overview of how MySQL is related to database systems and design roles.

**Relational Databases:**

Goal: To organize large amounts of data that can be quickly retrieved.

- It's compact and well structured
- Name comes from "relational algebra"
- Relationships between tables are to minimize calls to unneeded tables if possible
- Allows a developer to stand away from low-level optimization of its storage and calls

**Tables:**

- Smallest units in the entire system that can carry integral logical meaning.

**Database:**

- A collection of these tables

**Relational Database Management System, RDBMS:**

- A combination of the tables and their relations
- SQL is made to manage RDBMS, by creating relations between tables in a database.

**Database Design:**

- Plotting a database system on a canvas with a visual tool

**Entity-Relationship (ER) Diagram:**

- An image of connections and their tables

**Relational Schema (Database Schema):**

- An existing idea of how the database must be organized and implemented.
- Looks like a table, with items and their types.
- Can be used as a blueprint / plan, before design, or to look at when writing queries.

```text
Sales
===================
purchase_number**
date_of_purchase
customer_id (FK)
item_code   (FK)

Customers
=========
customer_id**
complaints
full_name
```

**Database Management:**

- Combination of work of design, creation, and manipulation of a database.

**Database Administration:**

- Provides daily maintenance of the database.

**Primary Key:**

- A column, or set of columns, whose value exists and is unque for every record in a table.
- Can only have one per table
- the "unique identifier"
- cannot be a Null value
- not all tables will have a primary key

**Foreign Key:**

- Identifies the relationships between tables, not the tables themselves.
- Often, foreign keys are the primary keys of a related table
- Ok to have missing and duplicate values in table
- If with setup relation, submitting a value to a foreign key that doesn't exist as a primary in the related table's primary will throw an error.

**Unique Key:**

- Used to specify that there should not be duplicates, but will allow Null values
- Can have as many of these as you like
- Can be applied as multiple columns

**One-to-many relationship (directional):**

- One value from a table can be found many times in another table
- Drawn uniquely in a schema diagram
- Other varieties of relationships exist.

**Cardinal Constraints:**

- the symbols showing relationship limitations
- M N for infinite
- O for optional instances
- | for one
- \> for many

## "How I Use SQL as a Data Analyst"

This [video](https://www.youtube.com/watch?v=GEBzsz8ZSXs) goes into how this person used SQL in combination with Python and other tools in the workplace.

**Ad Hoc Analysis:**

- On any given day he may be given one-off questions to investigate. These can be done purely with SQL, or with some processing with a programming language.

**Data Sharing:**

- There's good value to having SQL knowledge to build dashboards for others to be able to quickly access particular data regularly.
- With some tools, can quickly port data to Excel spaces for others unfamiliar with SQL.

**SQL, Structured Query Language:**

- "Sequel. Or, S.Q.L." is a language.
- We also need an editor and a running database.
- "A database is a large, structured, collection of data."
- "When I send this query to the database, it'll then provide me with a list of the.."

**NoSQL Languages:**

- "Not Only SQL"
- [IBM](https://www.ibm.com/topics/nosql-databases#:~:text=for%20AI%20updates-,What%20is%20a%20NoSQL%20database%3F,structures%20found%20in%20relational%20databases.) writes that NoSQL was born from the need for faster returns, and working with disparate datasets, in the time of cloud servers. So it's made in a context for reliability, scalability, and multiple hosting locations.
- IBM throws the example of systems working with e-commerce.
- NoSQL, with its "sharding", allows for horizontal scaling for increased storage capacity and speed in queries.
- It's designed to be an alternative to relational databases. Companies will commonly use both relational and NoSQL databases in the same application.
- Examples: MongoDB, Redis, Firebase, DynamoDB

**Options for Hosting Database:**

- Locally on computer for development
- In sharing with others "on prem," on premises, setup with the network.
- Some cloud provider, Amazon, Google, Azure, Heroku.

**Example of a Project:**

- Creator was called to investigate information about the suppliers for their business. This was spread between many tables, and required cleaning. With a coworker, spent couple weeks writing 100+ lines of SQL to grab this data.
- Creator was then asked to deliver this dataset in a presentable form for their boss. Used Power-BI, allowing queries inside. Created an end-point dashboard to allow stakeholders to view.

**Integration with Programming:**

- Collect tables into Python
- Clean it up with tools/libraries: `Pandas`
- `MatPlotLib` to visualize
- `scikit-learn` to perform regression analysis

## "Learn Database Normalization - 1NF, 2NF, 3NF, 4NF, 5NF"

This [video](https://www.youtube.com/watch?v=GFQaEYEc8_8) goes into specifics of each layer of database normalization with some examples of why it's necessary.

**Data can be wrong:**

- Database design can protect against invalid data. How to handle failures of data integrity. Ex: A person can't have two birthdays, we can avoid this from being allowing to be insert.

**Normalization:**

- When a database is normalized, it is structured in such a way that it cannot express redundant information.
- Protects against contradictory data.
- Easier to enhance and extend
- Protected from insertion/update/deletion anomalies.
- 1NF, 2NF, 3NF etc. are described as safety checks, or levels of confidence in avoiding problematic design and its errors. 1NF being the simplest of confidence.

**First Normal Form:**

- Using row order to convey information violates 1NF.
- Mixed data types on a column violates 1NF
- Having a table without a primary key violates 1NF
- Storing a repeating group of data items on a single row violates 1NF

**Second Normal Form:**

- Considers how a tables non-key attributes/columns relate to the primary key.
- Each non-key attribute must depend on the entire primary key.

**Third Normal Form:**

- 3NF means to forbid non-keys items having dependencies on other non-key items.
- "Every non-key attribute in a table should depend on the key, the whole key and nothing but the key."
- Boyce-Codd Normal form, "EVERY attribute in a table..."

**Fourth Normal Form:**

- Multi-valued dependencies in a table must be multi-valued dependencies on the key.
- Ex: "For every birdhouse model, there's two available shapes and two distinct available colors." The shape attribute is dependent on the model, and the color is dependent on the model. The model is not the key. Therefore, not in 4NF.

**Fifth Normal Form:**

- The table, which must be in 4NF, cannot be described as the logical result of joining some other tables together.

**Notes from Edgar Codd**

From [Wikipedia](https://en.wikipedia.org/wiki/Database_normalization) :

- Normalization objectives were described by Codd in 1970:
  - To free the database from undesired dependencies and their related anomalies.
  - To reduce the need for restructuring the database as new types are added.
  - To make the model more informative to read.
  - To make the collection of relations neutral to the query statistics.
- We're trying to avoid 3 sorts of anomalies:
  - Insertion anomaly:
    - A situation where certain facts cannot be recorded.
  - Update anomaly:
    - If an update is only partially successful the tables may be left in an inconsistent state. This can happen when information is expressed on multiple rows.
  - Deletion anomaly:
    - Circumstance may drive a deletion of more information than necessary leading to a loss of information.

**Drawbacks of Normalization:**

[Leah Nguyen](https://medium.com/@ndleah/a-brief-guide-to-database-normalization-5ac59f093161) writes about the relationship of enjoying the benefits of normalization--consistency in data and management benefits--with its negatives of added table numbers and the possibility of slower queries. We can imagine that the tables are stored in different drives or locations and that join operations can becomes costly.

This leads to the introduction of [denormalization](https://en.wikipedia.org/wiki/Denormalization), in which a normalized database is then modified to have some redundancy or different grouping of data than before in effort of increasing performance in read-time (at the cost of writes).
