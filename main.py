f = open("three_digit_numbers.txt") 
sample = f.read()
cols = sample.split()
num_list = []
for col in cols:
    num = int(col)
    num_list.append(num)

#print(cols)
#print(num_list)
start = min(num_list)
for count in range(start, max(num_list)):
    # print(count)
    if count not in num_list:
        print(f"{count} is missing")