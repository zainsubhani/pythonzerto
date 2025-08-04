# username =input("Please enter your username=")
# password = input("Please enter your password")

# print(f'the user name is {username} password length is {password} {len(password)}')

# amazon = ["zain","subhani"];
# amazon[0]="zainu"
# print(amazon)

# dictionry

# user = {
#     'zain':123,
#     'zain':444
# }
# print(user)
# is_old = True
# is_alive = False
# if is_old >= 2 and is_alive:
#     print('zain subhanni')
# elif is_old:
#  print('done')
 
 
 # trusthy and falsy
picture = [
  [0,0,0,1,0,0,0],
  [0,0,1,1,1,0,0],
  [0,1,1,1,1,1,0],
  [1,1,1,1,1,1,1],
  [0,0,0,1,0,0,0],
  [0,0,0,1,0,0,0]
]
 
for i in range(len(picture)):
    for j in range(len(picture[i])):
        if picture[i][j] == 0:
            print(' ', end='')
        else:
            print('*', end='')
    print()

for row in picture:
    for pixel in row:
        if pixel == 0:
            print(' ', end='')
        else:
            print('*', end='')
    print()
           

    
 