# Write  a  program that accepts  a  sequence  of comma-separated4-digit binary numbers as its input and
# then check whether they are divisible by 5 or not. The numbers  that  are  divisible  by
# 5  are  to  be  printed  in  a comma-separated sequence.

num = "0100,0011,1010,1001"
out = [str(x) for x in num.split(',') if int(x,2)%5==0]
",".join(out)