# Q-1 Find the Odd & Even Numbers in the List
def odd_even(list_1):
    odd = []
    even = []
    for i in list_1:
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
    print("odd numbers in given list: ",odd)
    print("even numbers in given list: ", even)

s1 = [10,501,22,37,100,999,87,351]
odd_even(s1)


#Q-2 find the Prime numbers in the List and find the count of it
def prime_num(list_2):
    pr_num = []
    for i in list_2:
        if i > 1:
            prime = True
            for j in range(2, i):
                if i % j == 0:
                    prime = False
                    break  # Exit the loop as soon as a divisor is found
            if prime:
                pr_num.append(i)
                    
    return pr_num

s2 = [10, 501, 22, 37, 100, 999, 87, 351]
print("List of Prime Numbers:", prime_num(s2))
print("No of Prime Number: ",len(prime_num(s2)))



# Q-3 find Happy Numbers in the list
def happy(n):
    se = set()
    while n != 1 and n not in se:
        se.add(n)
        n = sum(int(digit)**2 for digit in str(n))
    return n == 1

def happy_number(nums):
    hp_num = []
    for num in nums:
        if happy(num):
            hp_num.append(num)
    return hp_num

s3 = [10, 501, 22, 37, 100, 999, 87, 351]
happy_numbers = happy_number(s3)
print("Happy Numbers:", happy_numbers)



# Q-4 sum of first and last digit in integer
def sum(num):
    num = str(num)
    sum_digits = int(num[0]) + int(num[-1])
    return sum_digits

s4 = int(input("Enter the Number: "))
if s4 >= 10 :
    print("sum of first & last digit:", sum(s4))
else:
    print("Enter valid number")


# Q-5 Calculate the Distribution of Mangoes to No of Persons

def share ():
    N = list(map(int, input("Enter the Mangoes in the bag: ").split()))
    M = int(input("No of person: "))
    s = sorted(N)
    g_m = []
    if M <= len(s):
        for i in range(len(s)):
            g_m.append(s[i])
            if i == M -1:
                break
    print("Given Mangoes: ", g_m)
share()





#Q-6 Find Duplicates in the given List

def dup_list(li_1,li_2,li_3):
    se1 = set(li_1)
    se2 = set(li_2)
    se3 = set(li_3)
    dupli_se = se1.intersection(se2,se3)
    if dupli_se:
        return dupli_se
    else:
        return "No Duplicates in the list"

s6_1 = list(map(int, input("Enter the li_1: ").split()))
s6_2 = list(map(int, input("Enter the li_2: ").split()))
s6_3 = list(map(int, input("Enter the li_3: ").split()))
print("Duplicates in the list: ",dup_list(s6_1,s6_2,s6_3)) 
  


# Q-7 first Non-repating element
def non_repeat(list_7):
    for i in list_7:
        if list_7.count(i) == 1:
            return i
s7 = list(map(str,input("Enter the list_7: ").split()))
print("Non-repeating element: ", non_repeat(s7))