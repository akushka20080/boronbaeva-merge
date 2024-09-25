def ChessGame(Move1 , Move2):
    Let_x , Lety = Move1
    Set_x , Sety = Move2
    if Let_x  == Set_x or Lety == Sety or abs(Let_x - Set_x) == abs(Let_x - Set_x):
        return True
    else:
        False
Move1 = 6,5
Move2 = 4, 4
print(ChessGame )
jkdshiudefsed