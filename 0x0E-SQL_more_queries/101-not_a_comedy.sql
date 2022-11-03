-- Not a comedy sql
SELECT title FROM tv_shows EXCEPT SELECT title FROM tv_shows AS ts INNER JOIN (SELECT * FROM tv_genres AS tg INNER JOIN tv_show_genres AS tsg ON tg.id = tsg.genre_id WHERE tg.name = 'Comedy') AS h ON ts.id = h.show_id ORDER BY title;
