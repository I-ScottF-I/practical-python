# bounce.py
#
# Exercise 1.5

#ball hits the ground from height of 100m and every time 
#it bounces its apex is 3/5ths of its original bounce

#show height of first 10 bounces

height = 100
bounces = 0

while bounces < 10:
    height = height * 0.6
    bounces = bounces + 1
    print (bounces, height)
    
    