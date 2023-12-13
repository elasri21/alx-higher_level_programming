--  lists all shows, all genres linked to that show, from hbtn_0d_tvshows.
SELECT t.title, g.name
  FROM tv_shows AS t
    LEFT JOIN tv_shows_genres AS s
    ON t.id=s.show_id
    LEFT JOIN tv_genres AS g
    ON s.genre_id=g.id
  ORDER BY t.title, g.name;
