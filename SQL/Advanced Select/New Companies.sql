SELECT C.company_code, C.founder,
  (SELECT COUNT(DISTINCT lead_manager_code) FROM Lead_Manager LM WHERE LM.company_code=C.company_code),
  (SELECT COUNT(DISTINCT senior_manager_code) FROM Senior_Manager SM WHERE SM.company_code=C.company_code),
  (SELECT COUNT(DISTINCT manager_code) FROM Manager M WHERE M.company_code=C.company_code),
  (SELECT COUNT(DISTINCT employee_code) FROM Employee E WHERE E.company_code=C.company_code)
FROM Company C
ORDER BY C.company_code;
