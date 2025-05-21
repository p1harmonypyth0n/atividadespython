palavra = input("Digite uma palavra: ")

vogais = ("aeiouAEIOU")

contador=0

for vogal in palavra :
    
    if vogal in vogais :
        
        contador = contador + 1
   
   
    print(f"a palavra contem quantas vogais", contador)

