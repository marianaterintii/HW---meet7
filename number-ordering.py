from os import system


system ("cls")

start_number_n = int ( input ("start_n: "))
end_number_n = int ( input ("end_n: "))


n = 5
while n <= 10:

    if start_number_n >= 5 and end_number_n <= 10 :
        print (n)
    n = n + 1

print ()

start_number_m = int ( input ("start_m: "))
end_number_m = int ( input ("end_m: "))

m = 10
while m >= 5:
    if start_number_m <=10 and start_number_n >=5 :
        print (m)
    m = m - 1