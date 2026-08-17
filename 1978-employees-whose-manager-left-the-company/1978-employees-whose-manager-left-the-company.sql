# Write your MySQL query statement below
select employee_id 
from Employees
where salary < 30000
and manager_id is not null
and manager_id not in (select employee_id from Employees)
order by Employee_id asc