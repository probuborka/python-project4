import random
import string

def generate_string(n):
    """Генерация строки"""
    return ''.join([random.choice(string.ascii_letters + string.digits) for i in range(n)])

def split_to_words(text, n_word):
    """Разбиваем строку на слова с случайной длиной"""
    words = []
    for i in range(n_word):
        word_len = random.randint(3, 10)
        words.append(text[i:i + word_len])
    return words

def apply_action(words, actions):
    """Применяем действие"""
    actions_map = {
        'upper':      lambda w: w.upper(),
        'reverse':    lambda w: w[::-1],
        'double':     lambda w: w + w,
        'del_digits': lambda w: ''.join(c for c in w if not c.isdigit()),
        'del_even':   lambda w: ''.join(w[i] for i in range(len(w)) if i % 2 == 0),
        'replace':    lambda w: ''.join('Python' if c.isdigit() else c for c in w),
    }

    i_word = -1
    while i_word < len(words)-1:
        for action in actions:
            i_word += 1
            if i_word >= len(words):
                break 
            words[i_word] = actions_map[action](words[i_word])

def join_word(words):
    """Склеиваем слова в строку через пробел"""
    return " ".join(words)

text    = generate_string(1000)
words   = split_to_words(text, 10)
actions = ('upper', 'reverse', 'double', 'del_digits', 'del_even', 'replace')
apply_action(words, actions)
print(join_word(words))
