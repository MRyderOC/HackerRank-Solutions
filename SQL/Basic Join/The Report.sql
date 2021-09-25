SELECT 
  CASE
    WHEN S.Marks >= 70 THEN S.Name ELSE 'NULL'
  END,
  G.Grade,
  S.Marks
FROM Students S JOIN Grades G ON S.Marks BETWEEN G.Min_Mark AND G.Max_Mark
ORDER BY G.Grade DESC, S.Name;
