print("Hello ")
print()

cpt_python =  int(input(" quel est le score maximum de test en  python que vous pouvez obtenir ?"))
cpt_points = int(input("quel est le nombre de point que vous avez obtenus ?"))

number_competence = float(cpt_python/cpt_points)
number_compétence = round(number_competence,2)
cpt_pourcentage = round(float(cpt_python / cpt_points)*100, 2)

print("You got",cpt_pourcentage,"%")

if number_compétence >= .90:
  print("Your letter score is an A+")
elif number_compétence >= .80 and number_compétence <= .89:
  print("Your letter grade is an A-.")
elif number_compétence >= .70 and number_compétence <= .79:
  print("Your letter score is a B.")
elif number_compétence >= .60 and number_compétence <= .69:
  print("Your letter grade is a C.")
elif number_compétence >= .50 and number_compétence <= .59:
  print("Your letter grade is a D.")
elif number_compétence <= .49:
  print("Your letter grade is a U.")
else: 
  print("Try again!")



