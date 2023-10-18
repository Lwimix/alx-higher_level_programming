-- lists all genres from hbtn_0d_tvshows and displays
-- the number of shows linked to each
SELECT gen.name AS genre, COUNT(shgen.show_id) AS number_of_shows
FROM tv_genres gen
LEFT JOIN tv_show_genres shgen ON gen.id = shgen.genre_id
GROUP BY gen.id
HAVING COUNT(shgen.show_id) > 0
ORDER BY number_of_shows DESC;
