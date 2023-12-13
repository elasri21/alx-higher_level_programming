-- lists all genres from hbtn_0d_tvshows and displays the number of show.
SELECT name, SUM(`rate`) AS rating FROM tv_genres AS g
    INNER JOIN tv_show_genres AS r
    ON s.genre_id=s.show_id
GROUP BY name order BY rating DESC;
