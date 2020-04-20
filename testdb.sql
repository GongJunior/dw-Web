-- SQLite
SELECT DISTINCT
    n.name,
    count(w.id)
from names n
inner join words w on w.listname_id = n.id
GROUP BY n.name;