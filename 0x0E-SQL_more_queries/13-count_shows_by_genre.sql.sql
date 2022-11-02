-- Shows number of shows by genre
SELECT g.name AS 'genre', COUNT(*) AS 'number_of_shows' FROM tv_shows AS s INNER JOIN tv_shows_genre AS g ON s.genre_id = g.id GROUP BY g.name ORDER BY 'number_of_shows' DESC;
