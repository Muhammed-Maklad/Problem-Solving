SELECT *
FROM products
WHERE PATINDEX(
    '%SN[0-9][0-9][0-9][0-9]-[0-9][0-9][0-9][0-9][^0-9]%',
    description + ' '
) > 0
ORDER BY product_id;