-- lists all the shows that are contained in hbtn_0d_tvshows and that have at least only one genre linked
-- lists all the rows of the database that has only one column that's common
SELECT tv_shows.title, tv_show_genres.genre_id FROM tv_shows INNER JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
