USE project_3000;

-- Question 01
SELECT view_subtotal_list.food_id,
       food.food_name,
       Sum(view_subtotal_list.subtotal) AS "Total sales for each food",
       COUNT(view_subtotal_list.subtotal) AS "Total count ",
       CONCAT(FORMAT(100 * Sum(view_subtotal_list.subtotal) / (SELECT Sum(view_subtotal_list.subtotal) FROM view_subtotal_list),2),"%")  AS "Percentage of sales"
FROM   view_subtotal_list
       RIGHT OUTER JOIN food USING(food_id)
WHERE  ( LEFT(view_subtotal_list.food_id, 2) <> 'pk' )
GROUP  BY food.food_id
ORDER  BY Sum(view_subtotal_list.subtotal) DESC;

-- Question 02
SELECT Month(member_birth) AS "Members' birthday month",
       Count(Month(member_birth)) AS 'Count',
       Concat(Format(100 * Count(Month(member_birth)) / (SELECT Count(Month(member_birth)) FROM member 
                                   WHERE NOT Isnull(member_birth)), 2), "%") AS "Percentage"
FROM   member
WHERE  NOT Isnull(member_birth)
GROUP  BY Month(member_birth)
ORDER  BY Month(member_birth); 

-- Question 03
-- Without size
SELECT view_subtotal_list.food_id,
       food.food_name,
       Sum(view_subtotal_list.quantity) AS "total quantity for each food"
FROM   view_subtotal_list
       JOIN food USING(food_id)
WHERE  ( LEFT(view_subtotal_list.food_id, 2) <> 'pk' )
GROUP  BY view_subtotal_list.food_id
ORDER  BY view_subtotal_list.quantity DESC;

-- Question 04
SELECT view_total_list.waiter_id,
       waiter.waiter_name,
       FORMAT(Sum(view_total_list.total),2) AS "Total sales of each waiter",
       CONCAT(FORMAT(100 * Sum(total) / (SELECT Sum(total) FROM view_total_list),2),"%") AS 'Total Sales Percentage'
FROM   view_total_list
       RIGHT JOIN waiter USING (waiter_id)
GROUP  BY view_total_list.waiter_id
ORDER  BY Sum(view_total_list.total) DESC;

USE project_3000;

-- Question 01
SELECT view_subtotal_list.food_id,
       food.food_name,
       Sum(view_subtotal_list.subtotal) AS "Total sales for each food",
       COUNT(view_subtotal_list.subtotal) AS "Total count ",
       CONCAT(FORMAT(100 * Sum(view_subtotal_list.subtotal) / (SELECT Sum(view_subtotal_list.subtotal) FROM view_subtotal_list),2),"%")  AS "Percentage of sales"
FROM   view_subtotal_list
       RIGHT OUTER JOIN food USING(food_id)
WHERE  ( LEFT(view_subtotal_list.food_id, 2) <> 'pk' )
GROUP  BY food.food_id
ORDER  BY Sum(view_subtotal_list.subtotal) DESC;

-- Question 02
SELECT Month(member_birth) AS "Members' birthday month",
       Count(Month(member_birth)) AS 'Count',
       Concat(Format(100 * Count(Month(member_birth)) / (SELECT Count(Month(member_birth)) FROM member 
                                   WHERE NOT Isnull(member_birth)), 2), "%") AS "Percentage"
FROM   member
WHERE  NOT Isnull(member_birth)
GROUP  BY Month(member_birth)
ORDER  BY Month(member_birth); 

-- Question 03
-- Without size
SELECT view_subtotal_list.food_id,
       food.food_name,
       Sum(view_subtotal_list.quantity) AS "total quantity for each food"
FROM   view_subtotal_list
       JOIN food USING(food_id)
WHERE  ( LEFT(view_subtotal_list.food_id, 2) <> 'pk' )
GROUP  BY view_subtotal_list.food_id
ORDER  BY view_subtotal_list.quantity DESC;

-- Question 04
SELECT view_total_list.waiter_id,
       waiter.waiter_name,
       FORMAT(Sum(view_total_list.total),2) AS "Total sales of each waiter",
       CONCAT(FORMAT(100 * Sum(total) / (SELECT Sum(total) FROM view_total_list),2),"%") AS 'Total Sales Percentage'
FROM   view_total_list
       RIGHT JOIN waiter USING (waiter_id)
GROUP  BY view_total_list.waiter_id
ORDER  BY Sum(view_total_list.total) DESC;

-- Question 05
SELECT payment_method.method,
       payment_method_info.description,
       COUNT(total) AS "Total count",
       CONCAT(FORMAT(100 * COUNT(total) / (SELECT COUNT(total) FROM view_total_list),2),"%") AS 'Total Count Percentage'
FROM   view_total_list
       JOIN payment_method USING(order_id)
       RIGHT JOIN payment_method_info USING (method)
GROUP  BY payment_method.method
ORDER  BY Sum(total) DESC;

-- Question 06
SELECT        LEFT(view_total_list.member_id, 1) AS member_initial,
              IF(LEFT(view_total_list.member_id, 1) = 'A', 'member', member.member_name) AS 'member type',
              FORMAT(Sum(view_total_list.total),2) AS "Total spend",
              CONCAT(FORMAT(100 * Sum(total) / (SELECT Sum(total) FROM view_total_list),2),"%") AS 'Total Sales Percentage'
FROM   view_total_list
       JOIN member USING(member_id)
GROUP  BY LEFT(view_total_list.member_id, 1)
ORDER  BY view_total_list.member_id;

-- Question 07
SELECT LEFT(food_id, 2) AS 'Id Group',
       food.food_cruise,
       Sum(subtotal) AS 'Total Sales',
       Concat(Format(100 * Sum(subtotal) / (SELECT Sum(subtotal) FROM view_subtotal_list), 2), "%") AS 'Total Sales Percentage'
       FROM   view_subtotal_list
       JOIN food using(food_id)
GROUP  BY LEFT(food_id, 2)
ORDER  BY Sum(subtotal) DESC; 

-- Question 08
SELECT waiter_id,
       waiter_name,
       IF(Isnull(waiter_left_date), Datediff(Curdate(), waiter_join_date),
       Datediff(waiter_left_date, waiter_join_date)) AS 'Accumulated working days'
FROM   waiter
ORDER BY IF(Isnull(waiter_left_date), Datediff(Curdate(), waiter_join_date),
       Datediff(waiter_left_date, waiter_join_date)) DESC; 

-- Question 09
SELECT takeaway,
       FORMAT(Sum(total),2) AS "Total Sales",
       CONCAT(FORMAT(100 * Sum(total) / (SELECT Sum(total) FROM view_total_list),2),"%") AS 'Total Sales Percentage'
FROM   view_total_list
GROUP  BY takeaway
ORDER  BY SUM(total) DESC;

-- Question 10
SELECT takeaway,
       Count(total) AS 'Count',
       CONCAT(FORMAT(100 * Count(total) / (SELECT Count(total) FROM view_total_list),2),"%") AS 'Count Percentage',
       SUM(total) AS 'Total Amount',
       FORMAT(SUM(total)/COUNT(total),2) AS 'Average sales each'
FROM   view_total_list
GROUP  BY view_total_list.takeaway; 
-- Question 06
SELECT        LEFT(view_total_list.member_id, 1) AS member_initial,
              IF(LEFT(view_total_list.member_id, 1) = 'A', 'member', member.member_name) AS 'member type',
              FORMAT(Sum(view_total_list.total),2) AS "Total spend",
              CONCAT(FORMAT(100 * Sum(total) / (SELECT Sum(total) FROM view_total_list),2),"%") AS 'Total Sales Percentage'
FROM   view_total_list
       JOIN member USING(member_id)
GROUP  BY LEFT(view_total_list.member_id, 1)
ORDER  BY view_total_list.member_id;

-- Question 07
SELECT LEFT(food_id, 2) AS 'Id Group',
       food.food_cruise,
       Sum(subtotal) AS 'Total Sales',
       Concat(Format(100 * Sum(subtotal) / (SELECT Sum(subtotal) FROM view_subtotal_list), 2), "%") AS 'Total Sales Percentage'
       FROM   view_subtotal_list
       JOIN food using(food_id)
GROUP  BY LEFT(food_id, 2)
ORDER  BY Sum(subtotal) DESC; 

-- Question 08
SELECT waiter_id,
       waiter_name,
       IF(Isnull(waiter_left_date), Datediff(Curdate(), waiter_join_date),
       Datediff(waiter_left_date, waiter_join_date)) AS 'Accumulated working days'
FROM   waiter
ORDER BY IF(Isnull(waiter_left_date), Datediff(Curdate(), waiter_join_date),
       Datediff(waiter_left_date, waiter_join_date)) DESC; 

-- Question 09
SELECT takeaway,
       FORMAT(Sum(total),2) AS "Total Sales",
       CONCAT(FORMAT(100 * Sum(total) / (SELECT Sum(total) FROM view_total_list),2),"%") AS 'Total Sales Percentage'
FROM   view_total_list
GROUP  BY takeaway
ORDER  BY SUM(total) DESC;

-- Question 10
SELECT takeaway,
       Count(total) AS 'Count',
       CONCAT(FORMAT(100 * Count(total) / (SELECT Count(total) FROM view_total_list),2),"%") AS 'Count Percentage',
       SUM(total) AS 'Total Amount',
       FORMAT(SUM(total)/COUNT(total),2) AS 'Average sales each'
FROM   view_total_list
GROUP  BY view_total_list.takeaway; 