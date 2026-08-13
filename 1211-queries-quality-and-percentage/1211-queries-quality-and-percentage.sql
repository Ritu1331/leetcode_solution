# Write your MySQL query statement below
select query_name , ifnull(round(avg(rating / position ) ,2),0) as quality , 
ifnull(round(sum(rating < 3) * 100 / count(*),2),0) as poor_query_percentage
from Queries
group by query_name  




