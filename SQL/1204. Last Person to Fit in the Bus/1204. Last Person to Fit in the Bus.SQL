Select  person_name From
(
    Select person_name  , Turn,
    Sum(weight) over (Order by turn ) As Weight
    from Queue
) temp
Where Weight <= 1000
Order by turn DESC Limit 1 ;