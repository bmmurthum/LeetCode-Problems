-- Leetcode 595

-- Creates the example table
CREATE TABLE world (
    name varchar(255),
    continent varchar(255),
    area int,
    population int,
    gdp bigint,
    PRIMARY KEY (name)
);

INSERT INTO world (name, continent, area, population, gdp)
VALUES (
    "Afghanistan",
    "Asia",
    652230,
    25500100,
    20343000000
);

INSERT INTO world (name, continent, area, population, gdp)
VALUES (
    "Albania",
    "Europe",
    28748,
    2831741,
    12960000000
);

INSERT INTO world (name, continent, area, population, gdp)
VALUES (
    "Algeria",
    "Africa",
    2381741,
    37100000,
    188681000000
);

INSERT INTO world (name, continent, area, population, gdp)
VALUES (
    "Andorra",
    "Europe",
    468,
    78115,
    3712000000
);

INSERT INTO world (name, continent, area, population, gdp)
VALUES (
    "Angola",
    "Africa",
    1246700,
    2069294,
    100990000000
);



-- Write a solution to fine the name, population and area of the "big" 
-- countries.
SELECT name, population, area
FROM World
WHERE area >= 3000000 OR population >= 25000000