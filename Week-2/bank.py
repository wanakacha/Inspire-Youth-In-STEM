#write a program that calculates 16% tax on income
#ranging between 100k-150k


#19% tax if income is between 150k-300k
#30%tax if income is above 300k
#5%if income is less 100k

#print gross income ,net income

income=input("enter your net income")
gross_income=input("")
income=int(input("enter your income: "))

if income<=100000:
    net_income=income*0.95
if income<300000:
    net_income=income*0.81
else:
    net_income=income*0.7
print("gross income:" + str(income)+"net income:"+str(net_income))





taxgroup_a=
taxgroup_b=
taxgroup_c=
taxgroup_d=

if gross_income<=100000:
    print("gross_income",gross_income)
    print("net_income",net_income-tax group_a)