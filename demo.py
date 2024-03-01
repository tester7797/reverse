# ---------------------------------

print('--reverse the number--')

numb=12345    #1234  #123  #0
rev=0    #5  #54 #54321

while numb > 0:    # 1234 != 0
    d=numb%10    #d=5  #4  #3
    rev=rev*10+d  #0+5=5 #50+4=54  #540+3=543
    numb=numb//10    #1234   #123  #12

print('reverse numb',rev)

print('done')

a=20
print(a)

#-------------