import random
def pickagame(listofgames):
  temp2 = "yes"
  print(listofgames[random.randint(0,len(listofgames)-1)])
  temp2 = input("so you like the game i picked? if no enter NO, enter yes to end script.")
  if temp2 == "NO":
    pickagame(listofgames)
  else:
    print("your welcome")



listofgames = []
point = 0

while point != "1":
  print("please enter a game that is on a list that you would like to play.")
  temp = input("or text STOP to stop ")
  if temp == "STOP":
    if len(listofgames) < 1:
      print("no game entered, so no game was picked")
      point = "1"
      ifor = "1"
    else:
      point = "1"
      ifor = "0"
  else:
    listofgames.append(temp)
if ifor != "1":
  pickagame(listofgames)

  
  