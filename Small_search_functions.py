##--Created By Michael Morten
###-- Date: 7/14/2019 @ 9:51am

from itertools import islice
R = [ [0, 0, 0, 1], [0, 1, 1, 0], [0, 0, 0, 1], [0, 0, 1, 0] ]

A2 = [[0, 1, 1,1]]
B2 = [[1, 1,0, 0]]

A = [ [0, 1], [1, 0] ]
B = [ [1, 0], [1,0]]

Am = [ [0, 1, 1], [1, 0, 1] ]
Bm = [ [1, 0], [0, 0], [0, 1] ]

BB2 = [[0, 0, 0, 1], [0, 1, 1, 0], [0, 0, 0, 1], [0, 0, 1, 0]]
BB3 = [[0, 1, 0, 0], [0, 0, 1, 1], [1, 0, 0, 0], [0, 1, 0, 0]]
#Methods
#-----------------------------------------------------
def matrix_print(A):
 while (len(A)>0):
     word=""
     set_to_print=A.pop(0)
     for i in set_to_print:
         word+=str(i)
     print(word)
def matrix_add_boolean(A,B):
 ending_matrix=[]
 lenToUse=(len(A[0]))
 for w in range (len(A)):
        for y in range(lenToUse):
            aTerm=A[w][y]
            bTerm=B[w][y]
            result=aTerm + bTerm
            if (aTerm + bTerm >= 1):
                ending_matrix.append(1)
            elif (aTerm + bTerm == 0):
                ending_matrix.append(0)
 rep = iter(ending_matrix)
 duece=[list(islice(rep, lenToUse)) for i in range(lenToUse)]
 return duece
def matrix_multiplication_boolean(A,B):
 counter=0
 results=0
 results2=0
 results_to_print=[]
 rep=[]
 while (counter < len(A)):
     for w in range(len(A)):
          for x in range(len(B)):
                aTerm=A[counter][x]
                bTerm=B[x][w]
                results=aTerm * bTerm
                results2=results+results2
          if (results2>=1):
             results_to_print.append(1)
             results2 = results2 * 0
          elif (results2<1):
             results_to_print.append(0)
     counter = counter +1
 rep = iter(results_to_print)
 duece=[list(islice(rep, len(B[0]))) for i in range(len(A))]
 return duece
def matrix_power(A,n):
 list_to_print=[]
 final_list=[]
 final_list2=[]
 counter=3
 final_list = matrix_multiplication_boolean(A, A)
 if (n==0):
     return[]
 if (n==1):
     return (A)
 if (n<=2):
     return matrix_multiplication_boolean(A, A)
 elif (n>2):
     while(counter<=n):
        final_list = matrix_multiplication_boolean(final_list, A)
        counter=counter+1
        return final_list
def matrix_transitive_closure(R):
 temp=[]
 addTem=[]
 n = 1
 for i in range(len(R[0])):
    while (n!=len(R[0])-1):
     temp = matrix_power(R, n)
     addTemp=matrix_add_boolean(temp, R)
     n=n+1
 print(addTemp)

#----------------------Testers/Calls--------------------
matrix_print(R)   #(TESTED!!)

# These method needed a return because they were used
# is being used in other methods
# the Addition function and multiplication function have returns
print((matrix_add_boolean(BB2, BB3))) #-- (TESTED!!)
print(matrix_multiplication_boolean(Am,Bm))
print(matrix_power(BB2, 3))

#This one has a print statement for it wasn't used in any other
# functions
matrix_transitive_closure(BB2)


