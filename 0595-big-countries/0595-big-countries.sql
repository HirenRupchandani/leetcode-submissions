# Write your MySQL query statement below

SELECT name, population, World.area 
from World 
where World.area >= 3000000 
OR population >= 25000000;