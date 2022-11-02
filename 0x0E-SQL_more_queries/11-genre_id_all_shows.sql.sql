-- Shows Genre id for all shows
SELECT s.title, g.genre_id FROM tv_shows as s LEFT OUTER JOIN tv_shows_genres as g ORDER BY s.title, g.genre_id;
