### Ejercicios

'''
1. Declare an empty list
2. Declare a list with more than 5 items
3. Find the length of your list
4. Get the first item, the middle item and the last item of the list
5. Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
6. Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, manzana, IBM, Oracle and Amazon.
7. Print the list using _print()_
8. Print the number of companies in the list
9. Print the first, middle and last company
10. Print the list after modifying one of the companies
11. Add an IT company to it_companies
12. Insert an IT company in the middle of the companies list
13. Change one of the it_companies names to uppercase (IBM excluded!)
14. Join the it_companies with a string '#;&nbsp; '
15. Check if a certain company exists in the it_companies list.
16. Sort the list using sort() method
17. Reverse the list in descending order using reverse() method
18. Slice out the first 3 companies from the list
19. Slice out the last 3 companies from the list
20. Slice out the middle IT company or companies from the list
21. Remove the first IT company from the list
22. Remove the middle IT company or companies from the list
23. Remove the last IT company from the list
24. Remove all IT companies from the list
25. Destroy the IT companies list
26. Join the following lists:

    front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
    back_end = ['Node','Express', 'MongoDB']
'''
#Resolver 10 ejercicios 
#KEA

#Ejercicios resueltos
#1-1. Declare an empty list
print("##-- Ejercicio 1 --##")
listaVacia=[ ]
print(listaVacia)

#2-3. Find the length of your list
print("##-- Ejercicio 2 --##")
lista1=['Facebook', 'Google', 'Microsoft', 'manzana', 'IBM', 'Oracle', 'Amazon']
print(lista1)
tamaño1=len(lista1)
print("La lista contiene:", tamaño1, "elementos ")

#3-6. Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, manzana, IBM, Oracle and Amazon.
print("##-- Ejercicio 3 --##")
companies=['Facebook', 'Google', 'Microsoft', 'manzana', 'IBM', 'Oracle', 'Amazon']
print("La lista de compañias es la siguiente:\n", companies)

#4-9. Print the first, middle and last company
print("##-- Ejercicio 4 --##")
tam_companias=len(companies)
#print(tam_companias)
medio=int((tam_companias-1)/2) #nos da la el # del elemento medio de la lista
#print(medio)
print("1er Compañia: ",companies[0], ", 2da Compañia: ",companies[medio], ", 3er Compañia: ",companies[tam_companias-1])

#5-12. Insert an IT company in the middle of the companies list
print("##-- Ejercicio 5 --##")
companies[medio]='Intel'
print(companies)


#6-15. Check if a certain company exists in the it_companies list.
print("##-- Ejercicio 6 --##")
#a=input ()
#existe=a in companies
existe="Huawei" in companies
print(existe)
if existe==True:
    print("La compañia si existe en la lista")
else:
    print("La compañia no existe en la lista")

#7-18. Slice out the first 3 companies from the list
print("##-- Ejercicio 7 --##")
corte3=companies[3:]
print(corte3)

#8-21. Remove the first IT company from the list
print("##-- Ejercicio 8 --##")
companies.pop(0)
print(companies)


#9-24. Remove all IT companies from the list
print("##-- Ejercicio 9 --##")
del companies[:]
print (companies)


#10-26. Join the following lists:

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
print("##-- Ejercicio 10 --##")
listaunida=front_end+back_end
print("Las listas unidas es:\n", listaunida)