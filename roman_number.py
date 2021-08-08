roman_dict={ 1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 40: 'XL',50: 'L', 90: 'XC', 100: 'C', 400: 'XD', 500: 'D', 900: 'CM', 1000: 'M'}
num=int(input("enter a int num:"))
int_num=[1000,900,500,400,100,90,50,40,10,9,5,4,1]
for i in int_num:
    if num!=0:
        quo=num//i
        if quo!=0:
            for j in range(quo):
                print(roman_dict[i],end="")
        num%=i