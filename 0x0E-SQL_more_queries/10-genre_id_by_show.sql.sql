-- Show Genre ID by Show
SELECT tv_shows.title, tv_shows_genres.genre_id FROM tv_shows INNER JOIN tv_show_genres ON tv_shows.id = tv_shows_genres.genre_id ORDER BY tv_shows.title, tv_shows_genres.genre_id
