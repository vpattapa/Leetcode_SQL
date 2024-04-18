# Write your MySQL query statement below


 select Department, Employee, Salary from    
(select e.name as Employee, e.salary as Salary, d.name as Department,  DENSE_RANK() OVER(partition by departmentId order by salary desc) as dr from Employee as e
left join
Department as d
on e.departmentId = d.id) as a
where a.dr = 1