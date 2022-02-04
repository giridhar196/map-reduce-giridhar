# Giridhar
# This is an example mapper

import sys 

# iterate through each line provided via standard input
for line in sys.stdin:
  datalist = line.strip().split(",")
  if (len(datalist) == 10) : 
    car,price,body,mileage,engV,engType,registration,year,model,drive = datalist

    # print intermediate key-value pairs to standard output
    print(car,"\t",1)