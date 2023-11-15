-- Uses the database called hbtn_0d_tvshows to list all the genres isn't linked to the show Dexter
-- Uses the database to list all THE rows that's not linked to one of the row
SELECT name
FROM tv_genres
WHERE name NOT IN
(SELECT name
	FROM tv_genres
	LEFT JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
	LEFT JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
	WHERE tv_shows.title = 'Dexter')
GROUP BY name
ORDER BY name ASC;
