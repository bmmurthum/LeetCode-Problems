-- Leetcode 1757

-- Creates the example table
CREATE TABLE products (
    product_id int,
    low_fats enum('Y','N'),
    recyclable enum('Y','N')
);

INSERT INTO products (product_id, low_fats, recyclable)
VALUES (
    0,
    'Y',
    'N'
);

INSERT INTO products (product_id, low_fats, recyclable)
VALUES (
    1,
    'Y',
    'Y'
);

INSERT INTO products (product_id, low_fats, recyclable)
VALUES (
    2,
    'N',
    'Y'
);

INSERT INTO products (product_id, low_fats, recyclable)
VALUES (
    3,
    'Y',
    'Y'
);

INSERT INTO products (product_id, low_fats, recyclable)
VALUES (
    4,
    'N',
    'N'
  );

-- Select only the products that are both low-fat and recyclable
SELECT product_id
FROM products
WHERE low_fats = 'Y' AND recyclable = 'Y'