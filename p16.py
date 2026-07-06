basic=float(input("Enter the basic salary:"))
hra=basic*10/100
da=basic*55/100
pf=basic*12/100
grosssalary=basic+hra+da+pf
print(f"HRA is {hra}")
print(f"DA is {da}")
print(f"PF is {pf}")
print(f"Gross Salary is {grosssalary}")