-- List shows and genres
SELECT ts.title, r.name FROM tv_shows AS ts LEFT OUTER JOIN (SELECT * FROM tv_genres AS tg INNER JOIN tv_show_genres AS tsg ON tg.id = tsg.genre_id) AS r ON ts.id = r.show_id ORDER BY ts.title, r.name ASC;
