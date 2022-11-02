-- No Genre linked
SELECT s.title, g.genre_id FROM tv_shows AS s LEFT JOIN tv_shows_genre as g WHERE g.genre_id IS NULL ORDER BY s.title, g.genre_id;
