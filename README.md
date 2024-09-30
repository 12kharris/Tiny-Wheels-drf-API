
Problem with ORM being too restrictive with joins using filter and select_related
had to use raw SQL to overcome this and for some reason, using lk."IsLike" = 'true' stopped the qeuries from returning results. The query worked in pgadmin so not sure why this was. Therefore I had to move the filtering for liked/disliked into the react side of app