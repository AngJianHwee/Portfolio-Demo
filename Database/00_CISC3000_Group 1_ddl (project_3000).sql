DROP DATABASE IF EXISTS project_3000;

CREATE DATABASE project_3000;

USE project_3000;

CREATE TABLE food
  (
     food_id     CHAR(5),
     food_name   VARCHAR(40) NOT NULL,
     food_cruise VARCHAR(10) DEFAULT 'General',
     PRIMARY KEY (food_id),
     CHECK (LENGTH(food_id) = 5)
  );

CREATE TABLE food_price
  (
     food_id    CHAR(5) REFERENCES food(food_id) ON UPDATE CASCADE ON DELETE CASCADE,
     size       INT DEFAULT 1,
     unit_price DECIMAL(5, 2) NOT NULL,
     PRIMARY KEY (food_id, size),
     FOREIGN KEY (food_id) REFERENCES food(food_id),
     CHECK (unit_price > 0),
     CHECK ((size = 1) OR (size = 2))
  );

CREATE TABLE member
  (
     member_id    CHAR(5),
     member_name  VARCHAR(20) NOT NULL,
     member_birth DATE DEFAULT NULL,
     member_tel   VARCHAR(20) DEFAULT NULL,
     member_email VARCHAR(30) DEFAULT NULL,
     PRIMARY KEY (member_id),
     CHECK (LENGTH(member_id) = 5)
  );

CREATE TABLE waiter
  (
     waiter_id        CHAR(5),
     waiter_name      VARCHAR(20) NOT NULL,
     waiter_join_date DATE NOT NULL,
     waiter_left_date DATE DEFAULT NULL,
     waiter_birth     DATE DEFAULT NULL,
     waiter_tel       VARCHAR(20) NOT NULL,
     PRIMARY KEY (waiter_id),
     CHECK (LENGTH(waiter_id) = 5)
  );

CREATE TABLE payment_method_info
  (
     method      INT,
     description VARCHAR(40) NOT NULL,
     PRIMARY KEY(method)
  );

CREATE TABLE order_list
  (
     order_id   CHAR(5),
     member_id  CHAR(5) ,
     waiter_id  CHAR(5) ,
     order_date DATETIME NOT NULL,
     takeaway   INT DEFAULT 0,
     PRIMARY KEY (order_id),
     FOREIGN KEY (member_id) REFERENCES member(member_id) ON DELETE SET NULL ON UPDATE CASCADE,
     FOREIGN KEY (waiter_id) REFERENCES waiter(waiter_id) ON DELETE SET NULL ON UPDATE CASCADE, 
     CHECK (LENGTH(order_id) = 5)
  );

CREATE TABLE order_info
  (
     order_id CHAR(20) ,
     food_id  CHAR(5) ,
     size     INT NOT NULL,
     quantity INT NOT NULL,
     FOREIGN KEY (order_id) REFERENCES order_list(order_id) ON UPDATE CASCADE ON DELETE CASCADE,
     FOREIGN KEY (food_id) REFERENCES food(food_id),
     CHECK (quantity > 0),
     CHECK ((size = 1) OR (size = 2))
  );

CREATE TABLE payment_method
  (
     order_id CHAR(10) ,
     method   INT DEFAULT 0 ,
     PRIMARY KEY (order_id, method),
     FOREIGN KEY(order_id) REFERENCES order_list(order_id) ON UPDATE CASCADE ON DELETE CASCADE,
     FOREIGN KEY(method) REFERENCES payment_method_info(method) ON UPDATE CASCADE ON DELETE SET DEFAULT 
  );

CREATE TABLE discount_rate
  (
     member_id_initial CHAR(1),
     discount_rate     DECIMAL(4, 2),
     PRIMARY KEY (member_id_initial),
     CHECK (discount_rate <= 1),
     CHECK (discount_rate >= 0)
  );

CREATE view view_subtotal_list
AS
  (SELECT order_id,
          food_id,
          size,
          quantity,
          unit_price,
          ( unit_price * quantity ) AS subtotal
   FROM   order_info
          JOIN food_price USING(food_id, size));

CREATE view view_normal_member
AS
  (SELECT member_id
   FROM   member
   WHERE  member_id LIKE "a%");

CREATE view view_total_list
AS
  (SELECT order_id,
          member_id,
          waiter_id,
          order_date,
          takeaway,
          discount_rate.discount_rate,
          FORMAT(Sum(subtotal) * discount_rate,2) AS total
   FROM   order_list
          JOIN view_subtotal_list USING(order_id)
          JOIN discount_rate
            ON ( LEFT(member_id, 1) = discount_rate.member_id_initial)
   GROUP  BY ( order_id )); 