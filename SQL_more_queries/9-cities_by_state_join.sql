-- Cities by States
-- script lists all cities in hbtn_0d_usa.


SELECT cities.id, cities.name, states.name
FROM cities
INNER JOIN states ON cities.state_id = states.id
-- Sorted by city ID
ORDER BY cities.id ASC;