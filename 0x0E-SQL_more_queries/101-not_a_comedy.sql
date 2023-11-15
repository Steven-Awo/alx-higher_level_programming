-- Listing all the shows exemting the genre called Comedy in the database called hbtn_0d_tvshows
-- Uses a database above to list all the rows that isn't linked to one of the row
SELECT title
FROM tv_shows
WHERE title NOT IN
(SELECT title
	FROM tv_shows
	LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
	LEFT JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
	WHERE tv_genres.name = 'Comedy')
GROUP BY title
ORDER BY title ASC;
