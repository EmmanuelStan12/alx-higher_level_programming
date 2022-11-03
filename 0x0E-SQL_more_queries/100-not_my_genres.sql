-- Not my genre in sql
SELECT name FROM tv_genres except SELECT name FROM tv_genres AS tg INNER JOIN (SELECT * FROM tv_shows AS ts INNER JOIN tv_show_genres AS
tsg ON ts.id = tsg.show_id WHERE ts.title = 'Dexter') AS h ON tg.id = h.genre_id;
