-- Display max temperature of each state 
-- Ordered by statename
SELECT state, 
       MAX(value) AS max_temp
	FROM temperatures
GROUP BY state
ORDER BY state;
