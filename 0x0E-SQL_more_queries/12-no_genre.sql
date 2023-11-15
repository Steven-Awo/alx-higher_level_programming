-- Lists all the shows thhat's contained in hbtn_0d_tvshows but without the genre linked
-- Lists all the rows of the specified database that doesn't have one column
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows LEFT JOIN tv_show_genres
ON tv_shows.id = tv_show_genres.show_id
WHERE tv_show_genres.genre_id IS NULL
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
