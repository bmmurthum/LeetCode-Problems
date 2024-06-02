/*
Leetcode 1148 - Article Views I
https://leetcode.com/problems/article-views-i/description/

There is no primary key (column with unique values) for this table, the table may have duplicate rows.
Each row of this table indicates that some viewer viewed an article (written by some author) on some date. 
Note that equal author_id and viewer_id indicate the same person.

Write a solution to find all the authors that views at least one of their own articles.

Return the sult table sorted by id in ascending order.
*/

SELECT DISTINCT author_id AS id FROM Views 
WHERE author_id = viewer_id
ORDER BY author_id ASC


/*
Leetcode 1683 - Invalid Tweets
https://leetcode.com/problems/invalid-tweets/description/

Write a solution to find the IDs of the invalid tweets. The tweet is invalid if the number of characters used in the content of the tweet is strictly greater than 15.

Return the result table in any order.
*/

SELECT tweet_id FROM Tweets
WHERE CHAR_LENGTH(content) > 15


/*
Leetcode 1378 - Replace Employee ID With The Unique Identifier
https://leetcode.com/problems/replace-employee-id-with-the-unique-identifier/

Write a solution to show the unique ID of each user. If a user does not have a unique ID replace just show null.

Return the result table in any order.
*/

SELECT unique_id, name
FROM Employees
LEFT JOIN EmployeeUNI ON
EmployeeUNI.id = Employees.id


/*
Leetcode 1068 - Product Sales Analysis I
https://leetcode.com/problems/product-sales-analysis-i/description/

Write a solution to report the product_name, year, and price for each sale_id in the Sales table.

Return the resulting table in any order.
*/

SELECT Product.product_name, Sales.year, Sales.price 
FROM Sales
Left JOIN Product ON
Sales.product_id = Product.product_id


/*
Leetcode 1581 - Customer Who Visited But Did Not Make Any Transaction
https://leetcode.com/problems/customer-who-visited-but-did-not-make-any-transactions/

Write a solution to find the IDs of the users who visited without making any transactions and the number of times they made these types of visits. Return the result table in any order.

*/

-- SELECT v.customer_id, t.transaction_id,v.visit_id, t.visit_id, t.amount
SELECT v.customer_id, COUNT(v.visit_id) AS count_no_trans
From Visits v
LEFT JOIN Transactions t
ON v.visit_id = t.visit_id
WHERE t.visit_id IS NULL
GROUP BY v.customer_id


/*
Leetcode 197 - Rising Temperature
https://leetcode.com/problems/rising-temperature/

Write a solution to fine all dates' id with higher temperatures compared to its previous dates (yesterday). Return the result in any order.

*/

SELECT x.id
FROM Weather x, Weather y
WHERE DATEDIFF(x.recordDate,y.recordDate)=1 AND x.temperature>y.temperature