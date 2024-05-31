try:
  # Rock,paper,scissor
  import random 
  def game(x,y):
      Choice= ['rock','paper','scissor']

      if x==y:
        res="Match Draw"
      #   print("Draw")
        return (res)

      elif x=="rock" and y=="scissor" or x=="scissor" and y=="paper" or x=="paper" and y=="rock":
        res="1"
      #   print("Win")
        return res

      else:
        res="0"  
      #   print("Loss")
        return res

  print("Welcome to the game")
  print("1.Human vs Human")
  print("2.Human vs Computer")
  a=int(input('Enter the choice :'))
  Choice= ['rock','paper','scissor']

  if a==1:
      Player1_choice = input("Rock,paper, or scissor:").lower()
      while Player1_choice not in Choice:
          Player1_choice = input("Invalid choice. Please enter rock, paper, or scissors: ").lower()
      Player2_choice = input("Rock,paper, or scissor:").lower()
      while Player2_choice not in Choice:
          Player2_choice = input("Invalid choice. Please enter rock, paper, or scissors: ").lower()
      r=game(Player1_choice, Player2_choice)
      print(f'Player1 chose : {Player1_choice} , Player2 chose : {Player2_choice}')
      if r=="0":
          print("Player 2 Win")
      elif r=="1":  
          print("Player 1 Win") 
      else:
          print(r)        
  else :
      human_choice = input("Rock,paper, or scissor:").lower()
      while human_choice not in Choice:
          human_choice = input("Invalid choice. Please enter rock, paper, or scissors: ").lower()
      b=random.choice(Choice)
      computer_choice = b
      print("Computer chose :",computer_choice)
      r=game(human_choice, computer_choice)
      print(f'Human chose : {human_choice} , Computer chose : {computer_choice}')
      if r=="0":
          print("Computer Win")
      elif r=="1":  
          print("Human Win")     
      else:    
         print(r)
                
except:
 print('Some error ')      