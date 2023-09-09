#leap year
#dont change the above syntax
if ('year%4==0 and year%100!=0 or year%400=0'):
  'return True'
else:
  'return False'
year = int(input("enter the year"))
print("{} is the leap year.".format(year))
  