SELECT CONCAT(Name, "(", SUBSTRING(Occupation,1,1), ")") FROM OCCUPATIONS ORDER BY Name;

SELECT CONCAT("There are a total of ", COUNT(*), " ", LOWER(Occupation), "s.") FROM OCCUPATIONS GROUP BY Occupation ORDER BY COUNT(*),Occupation;
