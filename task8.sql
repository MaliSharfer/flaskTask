
--------------------------------------------task8------------------------------------------
------------------- Select query----------------;
1.
 select PRODUCT_ID,PRODUCT_NAME,LIST_PRICE from oe.product_information ORDER BY PRODUCT_NAME;

2.
select FIRST_NAME,LAST_NAME,PHONE_NUMBER,floor( months_between(CURRENT_DATE,HIRE_DATE)/12) AS yeares from hr.employees

3.
select FIRST_NAME,LAST_NAME,SALARY from hr.employees where EXTRACT(year from HIRE_DATE)>2005;

4.
select PRODUCT_NAME from oe.product_information;
where LIST_PRICE-MIN_PRICE >100
ORDER BY PRODUCT_NAME;
------------------------- Join query----------------:
1.
SELECT distinct oe.customers.CUSTOMER_ID, oe.orders.ORDER_ID 
FROM oe.customers 
INNER JOIN  oe.orders  
ON oe.customers.CUSTOMER_ID = oe.orders.CUSTOMER_ID
where (EXTRACT(year from oe.orders.ORDER_DATE)=2007) and (oe.customers.CREDIT_LIMIT>=200 and oe.customers.CREDIT_LIMIT<=700 )  
ORDER BY oe.orders.ORDER_ID;

2.
select oe.product_information.PRODUCT_NAME,oe.product_information.LIST_PRICE ,oe.categories_tab.CATEGORY_NAME from 
oe.product_information
inner join oe.categories_tab
ON oe.product_information.CATEGORY_ID = oe.categories_tab.CATEGORY_ID ;

3.
select oe.customers.CUST_FIRST_NAME ,oe.product_information.PRODUCT_NAME
from oe.customers
inner join oe.orders
on oe.customers.CUSTOMER_ID=oe.orders.CUSTOMER_ID
inner join oe.order_items
on oe.orders.ORDER_ID=oe.order_items.ORDER_ID
inner join oe.product_information
on oe.order_items.PRODUCT_ID=oe.product_information.PRODUCT_ID
where oe.order_items.UNIT_PRICE>10 and EXTRACT(year from oe.orders.ORDER_DATE)=2008 

4.
select oe.order_items.UNIT_PRICE*oe.order_items.QUANTITY as all_price ,oe.order_items.ORDER_ID ,oe.product_information.PRODUCT_NAME
from oe.product_information
inner join oe.order_items
on oe.order_items.PRODUCT_ID=oe.product_information.PRODUCT_ID
inner join oe.orders
on oe.orders.ORDER_ID=oe.order_items.ORDER_ID
where EXTRACT(year from oe.orders.ORDER_DATE)=2007

5.
select aa.FIRST_NAME ,aa.LAST_NAME, a.FIRST_NAME as manager_first_name ,aa.LAST_NAME manager_last_name
from hr.employees aa
inner join hr.employees a
on a.EMPLOYEE_ID=aa.MANAGER_ID ;

------------ Aggregation functions-------------:

1.
select  AVG(floor( months_between(CURRENT_DATE,HIRE_DATE)/12)) as  average_seniority from hr.employees

3.
select oe.product_information.SUPPLIER_ID , COUNT(oe.product_information.PRODUCT_NAME) count_of_product
from  oe.product_information   
group by oe.product_information.SUPPLIER_ID

4.
select PRODUCT_ID ,SUM(QUANTITY) QUANTITY
from oe.order_items
group by PRODUCT_ID 

5.
select  EXTRACT(year from ORDER_DATE) ,SUM(ORDER_TOTAL) total_sum , max(ORDER_DATE) last_order ,min(ORDER_DATE) first_order ,count(ORDER_DATE) amount_of_orders
from oe.orders
group by EXTRACT(year from ORDER_DATE)

6.
select  EXTRACT(day from ORDER_DATE) as day,SUM(ORDER_TOTAL) total_sum ,count(ORDER_DATE) amount_of_orders
from oe.orders
group by EXTRACT(day from ORDER_DATE)

7.
select SALES_REP_ID ,sum(ORDER_TOTAL)
from oe.orders
where EXTRACT(year from ORDER_DATE)=2007
group by SALES_REP_ID
having sum(ORDER_TOTAL)>20000

8.
select CUSTOMER_ID,sum(ORDER_TOTAL/1000)
from oe.orders
group by CUSTOMER_ID;

-------------------------- Sub query-------------------:
1.
select  PRODUCT_NAME , LIST_PRICE
from oe.product_information
where (select max(LIST_PRICE)from oe.product_information)=LIST_PRICE

2.
select PRODUCT_NAME ,LIST_PRICE
from oe.product_information
where (select max(LIST_PRICE)from oe.product_information)=LIST_PRICE and PRODUCT_ID in (select PRODUCT_ID from oe.order_items )

3.
select  PRODUCT_NAME , LIST_PRICE 
from oe.product_information
where LIST_PRICE=(select max(LIST_PRICE) from oe.product_information);

4.
select PRODUCT_ID from oe.order_items
where  ORDER_ID in (   
select ORDER_ID  from  oe.orders
where SALES_REP_ID=(
select EMPLOYEE_ID from hr.employees
where HIRE_DATE=(
select min(HIRE_DATE) from(
select EMPLOYEE_ID ,HIRE_DATE from hr.employees
where EMPLOYEE_ID in(select SALES_REP_ID from oe.orders)))))

5.
select distinct PRODUCT_ID from oe.order_items
where ORDER_ID in(
select ORDER_ID from oe.order_items
where PRODUCT_ID=    
(select PRODUCT_ID from oe.product_information
where LIST_PRICE=    
(select max(LIST_PRICE) from 
(select  PRODUCT_ID , LIST_PRICE from oe.product_information
where PRODUCT_ID in (  select PRODUCT_ID from oe.order_items)))));

----------------- analystic functions--------------------:
1.
with rws as (
  select o.PRODUCT_ID,o.CATEGORY_ID,o.LIST_PRICE, row_number () over (
           partition by CATEGORY_ID
           order by LIST_PRICE desc
         ) rn
  from   oe.product_information o
)
  select PRODUCT_ID,CATEGORY_ID,LIST_PRICE from rws
  where  rn <= 3

2.
SELECT EXTRACT(year from ORDER_DATE) as year,sum(ORDER_TOTAL) as sum ,
LAG(sum(ORDER_TOTAL)) OVER (order by EXTRACT(year from ORDER_DATE) asc ) - sum(ORDER_TOTAL)difference
FROM oe.orders
group  by EXTRACT(year from ORDER_DATE)  

3.
SELECT  sum(ORDER_TOTAL), EXTRACT(year from ORDER_DATE),EXTRACT(month from ORDER_DATE),SUM( sum(ORDER_TOTAL)) OVER (PARTITION BY EXTRACT(year from ORDER_DATE)) AS total_sal_by_dept
FROM oe.orders
group  by EXTRACT(year from ORDER_DATE) , EXTRACT(month from ORDER_DATE)
order by EXTRACT(year from ORDER_DATE)