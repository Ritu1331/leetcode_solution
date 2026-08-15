SELECT employee_id, department_id
FROM Employee e
WHERE primary_flag = 'Y'
   OR (
       SELECT COUNT(*)
       FROM Employee e2
       WHERE e2.employee_id = e.employee_id
   ) = 1
ORDER BY employee_id;