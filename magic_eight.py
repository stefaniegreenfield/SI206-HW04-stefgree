import random
lst = ['It is certain', 'It is decidely so', 'Without a doubt', 'Yes definitely', 'You may rely on it', 'As I see it, yes', 'Most likely', 'Outlook good', 'Yes', 'Signs point to yes', 'Reply hazy try again', 'Ask again later', 'Better not tell you now', 'Cannot predict now', 'Concentrate and ask again']

def question():
    while q!='quit':
        q=input('What is your question?')
        if q[-1]!='?':
            print('I’m sorry, I can only answer questions.')
