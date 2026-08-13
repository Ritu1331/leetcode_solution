# Write your MySQL query statement below
select round(avg(order_date = customer_pref_delivery_date) * 100 , 2) as immediate_percentage
from Delivery as d
where order_date = (
    select min(order_date)
    from Delivery
    where customer_id = d.customer_id
)