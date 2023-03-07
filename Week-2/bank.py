#write a program that calculates 16% tax on income
#ranging between 100k-150k


#19% tax if income is between 150k-300k
#30%tax if income is above 300k
#5%if income is less 100k

#p
print net income




tax_group_1=(gross_income*0.10)
tax_group_2=(gross_income*0.15)
tax_group_3=(gross_income*0.25)
tax_group_4=(gross_income*0.30)

if gross_income<=100000:
    print("gross_income=",gross_income)
    print("tax=",tax_group_1)
    print("net_income",(gross_income-tax group_1))
elif(gross_income>=100001)&(gross_income<=150000):
    print("gross_income=",gross_income)
    print("tax=",tax_group_2)
    print("net_income",(gross_income-tax group_2))
elif(gross_income>=150001)&(gross_income<=300000):
    print("gross_income=",gross_income)
    print("tax=",tax_group_3)
    print("net_income",(gross_income-tax group_3))
elif(gross_income>300000):
    print("gross_income=",gross_income)
    print("tax=",tax_group_4)
    print("net_income",(gross_income-tax group_4))

