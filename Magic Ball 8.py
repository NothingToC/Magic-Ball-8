import random

def en_magic_ball():
    answers = ["Undoubtedly", "It's a foregone conclusion", "No doubt about it", "Definitely yes", "You can be sure of that", "Very doubtful", "The prospects are not very good", "According to my data, no", "My answer is no", "Don't even think about it", "Concentrate and ask again", "It is impossible to predict now", "It's better not to tell", "Ask me later", "It's not clear yet, try again", "Yes", "The signs say yes", "Good prospects", "Most likely", "I think so"]

    print("Hello my friend, I am a magic ball, and I know the answer to any of your questions.")
    name = str(input("What's your name?: "))
    print(f"The magic ball is glad to welcome you {name}!")

    question = str(input("Do you want to know about any event?: ")).lower()

    if question == "yes":
        while True:
            print("The magic ball wants to know what interests you?")
            request = str(input())

            print(f"My answer: {random.choice(answers)}")

            next_step = str(input("Do you have any more questions?: ")).lower()

            if next_step == 'yes':
                continue

            elif next_step == 'no':
                print("Come back when you have any questions.! :)")
                break

            else:
                print("The magic ball couldn't recognize your answer, so it stopped working")
                break

    elif question == 'no':
        print("Come back when you have any questions.! :)")

    else:
        print("The magic ball couldn't recognize your answer, so it stopped working")

def ru_magic_ball():
    answers = ["Бесспорно", "Предрешено", "Никаких сомнений", "Определённо да", "Можешь быть уверен в этом", "Весьма сомнительно", "Перспективы не очень хорошие", "По моим данным - нет", "Мой ответ - нет", "Даже не думай", "Сконцентрируйся и спроси опять", "Сейчас нельзя предсказать", "Лучше не рассказывать", "Спроси позже", "Пока неясно, попробуй снова", "Да", "Знаки говорят - да", "Хорошие перспективы", "Вероятнее всего", "Мне кажется - да"]
    
    print("Привет мой друг, я магический шар, и я знаю ответ на любой твой вопрос.")
    name = str(input("Как тебя зовут?: "))
    print(f"Магический шар рад тебя приветствовать {name}!")

    question = str(input("Ты хочешь узнать о каком-либо событии?: ")).lower()

    if question == "да":
        while True:
            print("Магический шар хочет знать, что тебя интересует?")
            request = str(input())

            print(f"Мой ответ: {random.choice(answers)}")

            next_step = str(input("У тебя еще есть вопросы?: ")).lower()

            if next_step == 'да':
                continue

            elif next_step == 'нет':
                print("Возвращайся, когда у тебя появятся вопросы! :)")
                break

            else:
                print("Магический шар не смог распознать ваш ответ, поэтому он прекратил свою работу")
                break

    elif question == 'нет':
        print("Возвращайся, когда у тебя появятся вопросы! :)")

    else:
        print("Магический шар не смог распознать ваш ответ, поэтому он прекратил свою работу")
        

language = str(input("What language will the program work in?(На каком языке будет работать программа?): ")).lower()

if language == "русский" or language == "russian":
    ru_magic_ball()

elif language == "английский" or language == "english":
    en_magic_ball()

else:
    print("Язык не определен")