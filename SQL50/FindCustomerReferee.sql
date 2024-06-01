-- Leetcode 584

-- Creates the example table
CREATE TABLE customer_leetcode (
    id int,
    name varchar(255),
    referee_id int
);

INSERT INTO customer_leetcode (id, name, referee_id)
VALUES (
    1,
    "Will",
    NULL
);

INSERT INTO customer_leetcode (id, name, referee_id)
VALUES (
    2,
    "Jane",
    NULL
);

INSERT INTO customer_leetcode (id, name, referee_id)
VALUES (
    3,
    "Alex",
    2
);

INSERT INTO customer_leetcode (id, name, referee_id)
VALUES (
    4,
    "Bill",
    NULL
);

INSERT INTO customer_leetcode (id, name, referee_id)
VALUES (
    5,
    "Zack",
    1
);

INSERT INTO customer_leetcode (id, name, referee_id)
VALUES (
    6,
    "Mark",
    2
);

-- Select the names of people that were not refered by Jane
SELECT name
FROM customer_leetcode
WHERE referee_id IS NULL OR referee_id != 2