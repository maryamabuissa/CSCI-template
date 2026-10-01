# What does the following code print if I type "dAISY sunflOWER rOse"?


s1, s2, s3 = input().split()

s4 = s1.swapcase()
s4 = s4 + " " + s3[1].lower() + s3[0] + " " + s3.lower() + " " + s2.lower()[3:]

print(s1 + "...")
print(s4)
