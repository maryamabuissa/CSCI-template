# What does the following code print if I type "banana pear cucumber"?


f1, f2, f3 = input().split()

new_string = f1[0] + f2[1:-1] + f3[-1]
print(new_string)

