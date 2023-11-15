-- lists all the Comedy shows that are in the hbtn_0d_tvshows's database
-- lists all the rows of a database that'scorresponding to the column's value
SELECT title
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
LEFT JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
WHERE tv_genres.name = 'Comedy'
GROUP BY title
ORDER BY title ASC;
