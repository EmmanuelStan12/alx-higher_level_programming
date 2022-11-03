-- Get's shows with genre of comedy
SELECT title FROM tv_shows AS tg INNER JOIN (SELECT * FROM tv_genres AS ts INNER JOIN tv_show_genres AS tsg ON ts.id = tsg.genre_id WHERE ts.name = 'Comedy') AS r ON tg.id = r.show_id ORDER BY title ASC;
