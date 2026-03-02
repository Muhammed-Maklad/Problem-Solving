SELECT *,
       dna_sequence LIKE 'ATG%' AS has_start,
       RIGHT(dna_sequence, 3) IN ('TAA', 'TAG', 'TGA') AS has_stop,
       dna_sequence LIKE '%ATAT%' AS has_atat,
       dna_sequence LIKE '%GGG%' AS has_ggg
FROM Samples;


