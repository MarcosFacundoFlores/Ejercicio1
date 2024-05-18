import random
import re
from functools import reduce

def pause():
    input("Press Enter to return to the menu...")

def exercise_1():
    def calcular_cuadrado(numero):
        return numero ** 2

    numeros_aleatorios = [random.randint(1, 20) for _ in range(20)]
    resultado = list(map(calcular_cuadrado, numeros_aleatorios))

    print("Números aleatorios:", numeros_aleatorios)
    print("Cuadrados de los números aleatorios:", resultado)
    
    pause()  # Pause at the end of exercise 1

def exercise_2():
    def word_length(word):
        return len(word)

    text=open('juegos_en_red.txt','r',-1,'utf-8')
    words= re.sub(r'[ .,]+',' ',text.readline()).split(' ')
    words_length= list(map(word_length,words[0:30]))
    print(words_length)
    pause()  # Pause at the end of exercise 2

# Define more exercises in the same way
# Example:
def exercise_3():
    def capitalized_word(word):
        return word.capitalize()

    text=open('juegos_en_red.txt','r',-1,'utf-8')
    words= re.sub(r'[ .,]+',' ',text.readline().lower()).split(' ')
    capitalized_words=list(map(capitalized_word,words))
    print(capitalized_words)
    pause()  # Pause at the end of exercise 3

def exercise_4():
    numeros=[1,2,3,4,5,6,7,8,9,10]
    sumatoria=reduce(lambda x, y:x+y, numeros)
    print("Sumatoria(",numeros,")= ",sumatoria)
    pause()

def exercise_5():
    numeros=[1,2,3,4,5,6,7,8,9,10]
    producto=reduce(lambda ini, x: ini + [x*2], numeros,[]) #"ini" es el arreglo vacio que vamos a llenar
    print("2 *",numeros,"= ",producto)
    pause()

def exercise_6():
    def word_length(word):
        return len(word)

    text=open('juegos_en_red.txt','r',-1,'utf-8')
    words= re.sub(r'[ .,]+',' ',text.readline()).split(' ')
    promedio= reduce(lambda x, y:x+y, list(map(word_length,words)))/len(words)
    print("Promedio de longitudes: ",round(promedio))
    pause()

def exercise_7():
    pause()

def exercise_8():
    pause()

def exercise_9():
    pause()

def exercise_10():
    pause()

def main():
    exercises = {
        1: exercise_1,
        2: exercise_2,
        3: exercise_3,
        4: exercise_4,
        5: exercise_5,
        6: exercise_6,
        7: exercise_7,
        8: exercise_8,
        9: exercise_9,
        10: exercise_10
        # Add more exercises as needed
    }

    while True:
        print("Choose an exercise to execute:")
        for number, func in exercises.items():
            print(f"{number}. {func.__name__.replace('_', ' ')}")

        choice = input("Enter the exercise number (0 to exit): ")

        if choice == '0':
            print("Exiting...")
            break

        if choice.isdigit():
            exercise_number = int(choice)
            if exercise_number in exercises:
                exercises[exercise_number]()
            else:
                print("Invalid exercise number. Please try again.")
        else:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()
