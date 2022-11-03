-- Show Genre ID by Show
SELECT s.title, g.genre_id 
FROM tv_shows AS s INNER JOIN tv_show_genres as g 
ON s.id = g.show_id ORDER BY s.title, g.genre_id ASC;
