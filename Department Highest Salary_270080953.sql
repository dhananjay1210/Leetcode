# Write your MySQL query statement below
select D.Name as Department , E.Name as Employee , E.Salary as Salary 
from 
    Employee E,
    Department D 
where E.DepartmentId = D.Id 
  and (DepartmentId,Salary) in 
  (select DepartmentId,max(Salary) from Employee group by DepartmentId)
