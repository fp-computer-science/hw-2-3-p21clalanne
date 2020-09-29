print("PPPPP    "   "Y   Y    ""TTTTT   ""H   H    ""OOOOO    ""N   N")
print('P   P''     Y Y  ''     T   ''  HHHHH''    O   O''    NN  N')    
print('ppppp''      Y''        T''     H''  H''     O   O''    N N N')   
print('p''          Y''        T''     H''  H''     O   O''    N  NN') 
print('p''          Y''        T''     H''  H''     OOOOO''    N   N')



r = 4.6
a = 3.14*r**2
print(a) 
p = 2*3.14*r 
print(p)
print("the area of the circle with radius of 4.6 is 66.5")
print("the perimeter of the circle with the radius of 4.6 is 28.8")


l = 8.2
w = 13.9
t = 2*(l*w)
print(t)

l = 8.2
w = 13.9
e = w*l
print(e)

print("the area of the rectangle with length of 8.2 is 227.9") 
print("the perimeter of the rectangle with the length of 8.2 is 113.9") 


current_US_pop = 330337341
new_person_rate_second =16

"09-21-2020 to 09-22-2020 = 1day = Days*24hr*60min*60sec"
"one new person added every 16 seconds"
time_diff_second = 24*60*60


new_births = new_person_rate_second * time_diff_second/16

next_day_pop = current_US_pop + new_births

print(next_day_pop)
    