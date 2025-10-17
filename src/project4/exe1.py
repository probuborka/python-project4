import random
import string

def generate_string(n):
    """Генерация строки"""
    return ''.join([random.choice(string.ascii_letters + string.digits) for i in range(n)])


def apply_action(word, action):
    """Применяем действия"""
    actions_map = {
        'upper':      lambda w: w.upper(),
        'reverse':    lambda w: w[::-1],
        'double':     lambda w: w + w,
        'del_digits': lambda w: ''.join(c for c in w if not c.isdigit()),
        'del_even':   lambda w: ''.join(w[i] for i in range(len(w)) if i % 2 == 0),
        'replace':    lambda w: ''.join('Python' if c.isdigit() else c for c in w),
    }

    return actions_map[action](word)

def modify_text(text,n_word,actions):
    """Модификация строки"""
    words = []  
    len_text = len(text)
    i_word = 0
    begin_word = 0
    while i_word < n_word:
        for action in actions:
            len_word = random.randint(3, 10)
            if i_word >= n_word or begin_word + len_word > len_text:
                i_word = n_word
                break 
            words.append((apply_action(text[begin_word:begin_word + len_word],action)))
            begin_word += len_word
            i_word += 1

    return " ".join(words)

text = generate_string(100)

actions = ('upper', 'reverse', 'double', 'del_digits', 'del_even', 'replace')
text = modify_text(text,10,actions)

print(text)
