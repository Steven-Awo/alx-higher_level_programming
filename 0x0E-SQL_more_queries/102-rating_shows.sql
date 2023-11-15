-- listing all the shows that are from hbtn_0d_tvshows_rate and by their ratings
-- listing all the rows of the table by the total sum of a linked row
SELECT title, SUM(tv_show_ratings.rate) 'rating'
FROM tv_shows
LEFT JOIN tv_show_ratings ON tv_show_ratings.show_id = tv_shows.id
GROUP BY title
ORDER BY rating DESC;
