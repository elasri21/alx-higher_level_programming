--  lists all shows contained in hbtn_0d_tvshows
-- that have at least one genre linked.
SELECT ts.title, sg.genre_id FROM tv_shows AS ts INNER JOIN
tv_show_genres AS sg ON ts.id=sg.genre_id
ORDER BY ts.title, sg.genre_id;
