SELECT
CASE
    WHEN A = B AND B = C THEN "Equilateral"
    WHEN A + B <= C THEN "Not A Triangle"
    WHEN B + C <= A THEN "Not A Triangle"
    WHEN C + A <= B THEN "Not A Triangle"
    WHEN A = B AND A <> C then "Isosceles"
    WHEN A = C AND A <> B then "Isosceles"
    WHEN B = C AND A <> B then "Isosceles"
    ELSE "Scalene"
END
FROM TRIANGLES;
