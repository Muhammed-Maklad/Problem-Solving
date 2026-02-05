Delete P1
From Person P1
join Person P2
  ON p1.email = p2.email
 AND p1.id > p2.id;