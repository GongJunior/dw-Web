-- SQLite
SELECT DISTINCT
    n.name,
    count(w.id)
from name n
inner join word w on w.listname_id = n.id
GROUP BY n.name;