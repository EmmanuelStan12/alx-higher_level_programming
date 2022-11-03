-- Show my genres
SELECT name FROM tv_genres AS tg INNER JOIN (SELECT * FROM tv_shows AS ts INNER JOIN tv_show_genres AS tsg ON ts.id = tsg.show_id WHERE ts.title = 'Dexter') AS r ON tg.id = r.genre_id ORDER BY name ASC;
