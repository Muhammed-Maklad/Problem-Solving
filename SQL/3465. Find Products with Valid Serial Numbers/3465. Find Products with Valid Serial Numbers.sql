SELECT *
FROM products
WHERE CONCAT(' ',description,' ')
      LIKE '%[^A-Za-z0-9]SN[0-9][0-9][0-9][0-9]-[0-9][0-9][0-9][0-9][^A-Za-z0-9]%'  
      COLLATE Latin1_General_100_BIN2
ORDER BY product_id;