ROWS=3
COLS=3

MAX_LINE=3
MAX_BET=100
MIN_BET=1
#--------------------------------------------------------------------------------------->
symbolCount={
    "A":2,
    'B':4,
    'C':6,
    'D':8
}
symbolValue={
    "A":5,
    'B':4,
    'C':3,
    'D':2
}

def checkWin(columns,value,lines,bet):
    winnings=0
    winnings_Line=[]
    for line in range(lines):
        symbol=columns[0][line]
        for col in columns:
            symbol_Check= col[line]
            if symbol != symbol_Check:
                break
    else:
        winnings+=value[symbol]* bet
        winnings_Line.append(line +1)
    return winnings,winnings_Line





import random
def getSlotSpin(rows,cols,symbols):
    allSymbols=[]
    for symbol,symbolCount in symbols.items():
        for _ in range(symbolCount):
            allSymbols.append(symbol)
            
    columns=[]
    for _ in range(cols):
        column=[]
        currentSymbols = allSymbols[:]
        for _ in range (rows):
            value=random.choice(currentSymbols)
            currentSymbols.remove(value)
            column.append(value)
            
        columns.append(column)
        
    return columns

def getSlotPrint(columns):#transpose is happening with randows columns list 
    for row in range(len(columns[0])):
        for i,column in enumerate(columns):
            if i!= len(columns)-1:
                print(column[row],end=" | ")
            else:
                print(column[row],end="")
        print()
    
            
        
    

def deposit():
    while True:
        amt=input("Enter the Deposite Amount : Rs.")
        if amt.isdigit():
            amt=int(amt)
            if amt > 0:
                break
            else:
                print("Enter the Amount Greater than 0 || ")
        else:
            print("Please Enter the Valid Amount ||")
    return amt


def getNoOfLine():
    while True:
        lines=input("Enter the No. of Lines bet on (1-"+str(MAX_LINE)+") ? : ")
        if lines.isdigit():
            lines=int(lines)
            if 1 <= lines <= MAX_LINE:
                break
            else:
                print("Please Enter the No. of Line between 1 to 3")
        else:
            print("Please Enter the Valid Number ||")
    return lines
    

def getBet():
    while True:
        amt=input("Enter the Bet Amount for each line : Rs.")
        if amt.isdigit():
            amt=int(amt)
            if MIN_BET<= amt <=MAX_BET:
                break
            else:
                print(f"Enter the Amount Between Rs.{MIN_BET} to Rs.{MAX_BET} ")
        else:
            print("Please Enter the Valid Number ||")
    return amt
    
def spin(balance):
  lines= getNoOfLine()
  while True:
   bet=getBet()
   total_Bet=bet * lines
   if total_Bet > balance:
       print(f"You not having Enough Money to Bet, Your Bet Amount Rs.{total_Bet},Your Current Balance is Rs.{balance}. ")
   else:
       break
  print(f"Your Bet Amount is Rs.{bet} on {lines} lines, Total Bet Amount is Rs.{total_Bet}")
  slot=getSlotSpin(ROWS,COLS,symbolCount)
  getSlotPrint(slot)
  winnings, winnings_Line= checkWin(slot,symbolValue,lines,bet)
  print(f"you won Rs.{winnings}.")
  print(f"You Won on the line",*winnings_Line)
  return winnings - total_Bet
    
    
#---------------------------------------------------------------------------------------> 
def main():
  balance=deposit()
  while True:
      print(f"Current balance is Rs.{balance}")
      attempt=input("Press ENTER to Spin,Press Quit (Q to QUIT)")
      if attempt == "q":
          break
      balance +=spin(balance)
      
  print(f"You left with on Rs.{balance}")
    
          
  
  
#-------------------------------------------main-------------------------------------------->
main()
            