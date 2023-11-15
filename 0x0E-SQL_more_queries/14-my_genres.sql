-- UsING the database called hbtn_0d_tvshows  to lists the all genres in the show Dexter
-- Using a databse to actuALLY lists all THE rows in the table that's corresponding to all the rows in another
SELECT name
FROM tv_genres
LEFT JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
LEFT JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
WHERE tv_shows.title = 'Dexter'
GROUP BY name
ORDER BY name ASC;
