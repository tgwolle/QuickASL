# list= ['hello', 'world']
# output_list= []
# for word in list:
#   for n, letter in enumerate(word):
#     output_list[n]=  "images/"+ letter.upper() +".png"
# print (output_list) 
letters = {
  "A": "images/A.png",
  "B": "images/B.png",
  "C": "images/C.png",
  "D":"images/D.png",
  "E":"images/E.png",
  "F": "images/F.png",
  "G":"images/G.png",
  "H": "images/H.png",
  "I":"images/I.png",
  "J": "images/J.png",
  "K":"images/K.png",
  "L":"images/L.png",
  "M":"images/M.png",
  "N":"images/N.png",
  "O":"images/O.png",
  "P":"images/P.png",
  "Q":"images/Q.png",
  "R":"images/R.png",
  "S":"images/S.png",
  "T":"images/T.png",
  "U":"images/U.png",
  "V":"images/V.png",
  "W":"images/W.png",
  "X":"images/X.png",
  "Y":"images/Y.png",
  "Z":"images/Z.png",
  ".": "images/period.png",
  ",": "images/comma.png",
  "?": "images/qs.png",
  "!": "images/exc.png",
  "+":"images/empty.png"
  
 
}

input = ''
list = input.upper().replace(" ","+")

output_list=[]
for word in list:
      output_list.append(letters[word])
      
      
print(output_list)



