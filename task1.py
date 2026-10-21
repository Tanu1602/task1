# import numpy as np
# marks = np.array([
#     [65, 70, 68, 72, 75],
#     [73, 75, 70, 72, 74],
#     [90, 95, 89, 91, 94],
#     [55, 60, 58, 62, 57],
#     [80, 82, 84, 86, 88],
#     [85, 78, 92, 88, 76],
#     [96, 94, 98, 97, 95],
#     [67, 69, 71, 73, 75],
#     [88, 90, 85, 87, 89],
#     [78, 80, 82, 84, 86]
# ])

# print(f"the marks are: {marks}")

# #1.total
# total=[]
# for i in marks:
#     total.append(int(sum(i)))
#     sub_count=len(i)
# print(total)

# #2.average
# for i in total:
#  average= i/sub_count
#  print(average)

# #highest student marks
# highest=max(total)
# print(f"the highest student mark are {highest}")

# #subject_wise highest marks




# #above average
# for i in total:
#    average=i/sub_count
#    if average >= 75:
#      print(f"above average  = {average}")





     #--------------------------------------------------------------------------------------------------------------------------------------------

 # practical 2
# import numpy as np
# sales = np.array([
#     [45000, 52000, 48000, 51000],
#     [38000, 40000, 42000, 39000],
#     [60000, 62000, 61000, 63000],
#     [55000, 54000, 56000, 57000],
#     [30000, 32000, 31000, 33000],
#     [47000, 49000, 51000, 50000],
#     [65000, 67000, 66000, 68000]
# ])
# print(f"the complete salary is : {sales}")

# weak1=0



#2 total sales
# total=[]
# for i in sales:
#     total.append(int(sum(i)))
#     sub_count=len(i)
# print(total)

# #3.highest sales
# highest=max(total)
# print(f"the highest total sales are : {highest}")

# #4.lowest sales
# lowest=min(total)
# print(f"the lowest total sales are : {lowest}")

# #4.greater than 50000
# for i in total:
#     if i > (50000):
#         print(f"the greater sales is {i}")

#---------------------------------------------------------------------------------------------------------------------------------------------------------

#peactical:3 employee salary analyzer

# import numpy as np

# salary = np.array([
#     25000,
#     32000,
#     28000,
#     45000,
#     38000,
#     50000,
#     42000,
#     35000,
#     27000,
#     60000,
#     48000,
#     31000,
#     55000,
#     40000,
#     37000
# ])

# print(salary)

# #2.average salary
# total=0
# for i in salary:
#     total+=i
#     average=total/len(salary)
# print(f"average salary is = {average}")

# #2.min_max salary
# maximum=max(salary)
# print(F"the maximum salary is = {maximum}")
# minimum=min(salary)
# print(f"the minimum salary is = {minimum}")

# #3.more than 50000
# for i in salary:
#     if i >= (50000):
#       print(f"the salary is = {i}")

# #below average
# count=0
# for i in salary:
#    if i >=average:
#       count+=1
# print(f"the below average is = ",count)      

# #5. highest to lowest
# sorted_salary=np.sort(salary)
# print("highest to lowest")

#---------------------------------------------------------------------------------------------------------------------------------------------
# #practical 4. TEMPERATURE MONITORING
# import numpy as np

# temperature = np.array([
#     30, 31, 29, 32, 33,
#     34, 35, 31, 30, 29,
#     28, 32, 33, 34, 36,
#     35, 34, 33, 32, 31,
#     30, 29, 28, 27, 31,
#     32, 33, 34, 35, 36
# ])
# print(temperature)

# #2. highest_lowest temperature
# highest=max(temperature)
# lowest=min(temperature)
# print(f"the highest temperature is = {highest}")
# print(f"the lowest temperature is = {lowest}")

# #3.average temp
# total=0
# for i in temperature:
#     average=total/len(temperature)
#     total+=1
# print(f"the average temperature is = {average}")

# #4 temp above 35
# for i in temperature:
#  if i >=35:
#     print(f"the temp above 35 is ={i}")

#5 temp below 25
# count=0
# for i in temperature:
#     if i < 25:
#      count+=1    
#     print(f"the temp below 25 is ={i}")

# #6 diff bet maximum and minimum
# difference = highest-lowest
# print(f"the difference bet maximum and minimum temperature is = {difference}")


#--------------------------------------------------------------------------------------------------------------------------------------------------------
#practical. 5 STUDENT ATTENDANCE SYSTEM


# import numpy as np

# attendance = np.array([
#     95, 82, 76, 68, 91,
#     88, 73, 79, 97, 65,
#     84, 90, 72, 86, 93,
#     70, 77, 81, 98, 74
# ])
# print(attendance)

# #2.average
# total=np.sum(attendance)
# average = total/len(attendance)
# print(f"the average attendance is = {average}")

# #3.attendance below 75
# for i in attendance:
#     if i<75:
#         print(f"the attendance below 75 is = {i}")


# #4. attendance above 90
# count=0
# for i in attendance:
#     if i>90:
#         count+=1
# print(f"the attendance above 90 is = {count}")

# #5. highest and lowest attendance
# highest=max(attendance)
# lowest=min(attendance)
# print(f"the highest attendance is = {highest}")
# print(f"the lowest attendance is = {lowest}")


# #6.Replace all attendance values below 75 with 0.

# new=attendance.copy()
# for i in range(len(new)):
#         if i < 75:
#          new[i] = 0
# print(f"the new attendance is = {new}")


#\----------------------------------------------------------------------------------------------------------------------------------------------------------------------
#practical 6 E-COMMERCE ORDER ANALYSIS


# import numpy as np

# orders = np.array([
#     1200, 4500, 800, 2500, 6700,
#     1500, 3200, 900, 4100, 2800,
#     5600, 1100, 3900, 7200, 1800,
#     2400, 5100, 950, 6300, 3000
# ])

# print(orders)
# print("======================================================================================================================================================")

# #1.total revenue
# total_revenue=np.sum(orders)
# print(f"the total revenuue is = {total_revenue}")
# print("======================================================================================================================================================")

# #2.average order value
# total=0
# for i in orders:
#      total+=i
#      average=total/len(orders)
# print(f"the average is = {average}")
# print("========================================================================================================================================================")

# #3.orders above 5000
# for i in orders:
#      if i > 5000:
#           print(f"the orders above 5000 are = {i}")
#           print("========================================================================================================================================================")

# #4.orders below 2000
# for i in orders:
#      if i < 2000:
#           print(f"the orders below 2000 are = {i}")
#           print("========================================================================================================================================================")

# #5.sort orders in assending order
# sorted_orders =np.sort(orders)                     #np.sort(orders) = Sorts all orders in ascending order.
# print(f"the sorted orders are = {sorted_orders}")
# print("========================================================================================================================================================")

# #6. top 5 orders value
# top_5= np.sort(orders)[-5:]
# print(f"the top 5 orders are = {top_5}")    #[-5:]= Takes the last 5 values which are the highest orders

 #-----------------------------------------------------------------------------------------------------------------------------------------------------------------

# practical 7.BANK TRANSACTION ANALYSIS

# import numpy as np

# transactions = np.array([
#     5500, -1800, 2700, 600, -3200,
#     1500, 4500, -2000, -1000, 500,
#     6000, -2500, 3500, -1000, 2000,
#     5000, -1200, 2500, -800, 3000,
#     -700, 4000, -3000, 1500, -900,
#      2200, 4800, -1300, 2100, -4000
# ])

# print(transactions)
# print("========================================================================================================================================================")

# #2.total balance  change
# total=np.sum(transactions)
# print(f"the total balance change is = {total}")
# print("========================================================================================================================================================")

# #find all deposites transactions 
# deposite=transactions[transactions>0]
# print(f"the deposite transactions are = {deposite}")
# print("========================================================================================================================================================")

# #find all withdrawals transactions
# withdrawal=transactions[transactions<0]
# print(f"the withdrawal transactions are = {withdrawal}")
# print("========================================================================================================================================================")

# #find total deposites
# total_deposite=np.sum(deposite)
# print(f"the total deposites are={total_deposite}")
# print("========================================================================================================================================================")

# #find total withdrawals
# total_withdrawal=np.sum(withdrawal)
# print(f"the total withdrawals are={total_withdrawal}")
# print("===========================================================================================================================================================)")

# #find largest withdrawal
# largest=np.max(withdrawal)
# print(f"the largest withdrawal is = {largest}")
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# practical8. HOSPITAL PATIENT DATA
# import numpy as np
# data= np.array([
#     10, 25, 36, 63, 46,
#     18, 70, 59, 30, 15,
#     67, 40, 22, 50, 80,
#     12, 28, 75, 38, 48,
#     17, 62, 33, 27, 98
# ])

# #avg age of patient
# total=0
# for i in data:
#     total+=i
#     average=total/len(data)
# print(f"the average age of patient is = {average}")
# print("========================================================================================================================================================")

# #find the youngest and oldest patient
# youngest=np.min(data)
# print(f" the youngest patient is = {youngest}")

# oldest=np.max(data)
# print(f"the oldest patient is = {oldest}")
# print("================================================================================================================================================================")

# #find the patient above 60 years
# for i in data:
#     if i > 60:
#         print(f"the patient is above 60 years is = {i}")
# print("=======================================================================================================================================================")

# #find the patient below 18 years
# for i in data:
#     if i < 18:
#         print(f"the paient is below 18 years is = {i} ")
# print("======================================================================================================================================================")        


# # sort patient age
# sorted_data=np.sort(data)
# print(f"the sorted age is = {sorted_data}")

#find median

# -------------------------------------------------------------------------------------------------------------------------------------------------------------

# practical.9  EXAM RESULT ANALYSIS
import numpy as np

marks = np.array([
    [80, 75, 90, 85, 70, 88],
    [60, 55, 65, 70, 58, 62],
    [90, 92, 95, 89, 91, 94],
    [40, 45, 50, 42, 38, 44],
    [78, 82, 80, 76, 79, 81],
    [55, 60, 58, 62, 57, 59],
    [85, 88, 40, 87, 89, 35],
    [70, 72, 68, 74, 71, 69],
    [95, 96, 94, 97, 98, 99],
    [35, 40, 38, 42, 36, 39],
    [82, 80, 78, 84, 81, 79],
    [65, 67, 69, 64, 66, 68],
    [38, 90, 85, 87, 89, 91],
    [50, 52, 48, 55, 53, 51],
    [76, 74, 78, 80, 77, 79],
    [91, 93, 92, 94, 90, 95],
    [58, 60, 62, 59, 61, 63],
    [84, 86, 88, 85, 87, 89],
    [72, 70, 68, 74, 73, 71],
    [98, 97, 99, 96, 95, 80]
])
# total marks of each student
total=[]
for i in marks:
     total.append(int(sum(i)))

print(f"the total marks of each students are = {total}")
# print("====================================================================================================================================================")

# # . Calculate each students percentage
percentage=[] 
for i in total:
    per=(i/600)*100
    percentage.append(per)
print(f"the per of each student is = {percentage}")
print("=====================================================================================================================================")

#  Find the student with the highest percentage
highest=np.max(percentage)
print(f"the student with highest percentage is {highest}")

# Find students who scored below 40 in any subject. 





# 6. Count students whose percentage is above 80.
for i in percentage:
     if i > 90:
          print(f"the percentage above 90 is =s")