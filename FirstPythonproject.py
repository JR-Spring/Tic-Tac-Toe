#Codecademy lesson practices

right = "what is happening 50"

print(right)



def odd_indices(lst):
  new_lst = []
  for index in range(1, len(lst), 2):
    new_lst.append(lst[index])
  return new_lst

#Uncomment the line below when your function is done
print(odd_indices([4, 3, 7, 10, 11, -2]))

def odd_indices1(lst1):
  new_lst = []
  for index in range(0, len(lst1), 2):
    new_lst.append(lst1[index])
  return new_lst

#Uncomment the line below when your function is done
print(odd_indices1([4, 3, 7, 9, 11, 24, 56]))

#Overall I Determined which list returned the greater sum,To get ther I nested two loops and summed the number of each list using += and stored them in the sum variables,
# I then determined which list had the greatest sum and returned the answer.  
#where i have hashes are my steps

def larger_sum(lst1, lst2):
  sum1 = 0
  sum2 = 0
 # for number in lst1:
   # sum1 += number
 # for number in lst2:
   # sum2 += number
  if sum1 >= sum2:
    return lst1
  else: 
    return lst2

    #Uncomment the line below when your function is done
print(larger_sum([1, 9, 5, 10], [2, 3, 7, 30]))
    
#I created this on my own    
def smaller_sum(list3, list4):
  sum3 = 0 
  sum4 = 0
  for number in list3:
    sum3 += number 
    for number in list4:
      sum4 += number
 
    if sum3 <= sum4:
      return list3
    return list4
print(smaller_sum([2, 3, 7, 9, 11], [7, 3, 9, 9, 12, 45]))

#Code I created in Codecademy--code I finally answered right lol
def over_nine_thousand(lst):
  sum = 0
  for number in lst:
    sum += number
    if sum > 9000:
      break 
  return sum

print(over_nine_thousand([8000, 900, 120, 5000]))



# ****General outline of Tic Tac Toe code plan
# board--list
# display board--function
# play game--alternating turns from x to o etc# 
# handle turn
# check win function
    # check row, column, diagnol for win
# check tie function
# flip player

