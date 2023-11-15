-- listing all the shows and also all the genres linked to the show all from the database called hbtn_0d_tvshows
-- listing all the rows of a table that's linked to the other table
SELECT title, name
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
LEFT JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
ORDER BY title ASC, name ASC;
