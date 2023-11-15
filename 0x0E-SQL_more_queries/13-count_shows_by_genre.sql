-- lists all the genres from the hbtn_0d_tvshows and then displays the numb of shows that's linked to each
-- lists all the rows of the database that meets a condition
SELECT tv_genres.name AS 'genre', COUNT(tv_show_genres.genre_id) AS 'number_of_shows'
FROM tv_genres RIGHT JOIN tv_show_genres
ON tv_genres.id = tv_show_genres.genre_id
GROUP BY genre
ORDER BY number_of_shows DESC;
