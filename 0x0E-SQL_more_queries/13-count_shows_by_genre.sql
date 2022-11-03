-- Shows number of shows by genre
SELECT name, 
COUNT(*) as number_of_shows 
FROM tv_genres AS t 
INNER JOIN
(SELECT * FROM tv_shows AS s1 INNER JOIN tv_show_genres AS g1
ON s1.id = g1.show_id) 
AS h 
ON t.id = h.genre_id 
GROUP BY name ORDER BY number_of_shows DESC;
