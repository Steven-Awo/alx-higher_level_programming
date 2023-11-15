-- Lists all the shows thats contained in the hbtn_0d_tvshows database
-- Lists all the rows of the tables in the specified database
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows LEFT JOIN tv_show_genres
ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
