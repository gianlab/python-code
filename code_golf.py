def print_divisori():
    for i in range(1, 101):
        p = ''
        for z in range(1, 101):
            if z > i:
                break
            elif i % z == 0:
                p += str(z) + ' '
        print(p)


# print_divisori()

def evil_numbers():
    p = []
    for i in range(13, 1001):
        f = False
        for z in range(2, 1001):
            if z >= i:
                break
            elif i % z == 0:
                f = True
                break
        if not f:
            p.append(str(i))
    for s in p:
        k = s[::-1]
        if k in p and k != s:
            print(s)


# evil_numbers()


def print_cardinal_numbers():
    n = ('one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten')
    n1 = ('eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen')
    n2 = ('twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety')
    d = dict()
    d['0'] = 'zero'
    for i in range(1, 1000):
        t = str(i)
        t = tuple('0' * (3 - len(t)) + t)
        p = ''
        for j in range(2):
            k = int(t[j])
            if k > 0 and j == 0:
                p += n[k - 1] + ' hundred '
                if int(t[1]) > 0 or int(t[2]) > 0:
                    p += 'and '
            elif k > 1 and t[2] == '0':
                p += n2[k - 2]
            elif k > 1 and j == 1:
                p += n2[k - 2] + '-' + n[int(t[j + 1]) - 1]
            elif k == 1 and j == 1:
                if t[2] == '0':
                    p += 'ten'
                    break
                p += n1[int(t[j + 1]) - 1]
            elif k == 0 and j == 1:
                if t[2] == '0':
                    break
                p += n[int(t[2]) - 1]
        d[str(i)] = p
    d['1000'] = 'one thousand'
    inp = '8 7 200 958 17 1000 501 4 12 18 1 31 15 497 2 75 13 351 19 11 14 614 91 6 193 844 40 67 58 10 3 5 0 9 16 21 85 787'
    for z in inp.split(' '):
        print(d[z])


# print_cardinal_numbers()

def print_poker_card():
    s = '\'\\U0001f0'
    for c in ('a', 'b', 'c', 'd'):
        print(c, end='=')
        for i in range(1, 10):
            print(s + c + str(i) + '\'', end=',')
        for j in ('a', 'b', 'c', 'd'):
            print(s + c + str(j) + '\'', end=',')
        print(s + c + 'e\'')


# print_poker_card()

def print_cards():
    a = '\U0001f0a1', '\U0001f0a2', '\U0001f0a3', '\U0001f0a4', '\U0001f0a5', '\U0001f0a6', '\U0001f0a7', '\U0001f0a8', '\U0001f0a9', '\U0001f0aa', '\U0001f0ab', '\U0001f0ac', '\U0001f0ad', '\U0001f0ae'
    b = '\U0001f0b1', '\U0001f0b2', '\U0001f0b3', '\U0001f0b4', '\U0001f0b5', '\U0001f0b6', '\U0001f0b7', '\U0001f0b8', '\U0001f0b9', '\U0001f0ba', '\U0001f0bb', '\U0001f0bc', '\U0001f0bd', '\U0001f0be'
    c = '\U0001f0c1', '\U0001f0c2', '\U0001f0c3', '\U0001f0c4', '\U0001f0c5', '\U0001f0c6', '\U0001f0c7', '\U0001f0c8', '\U0001f0c9', '\U0001f0ca', '\U0001f0cb', '\U0001f0cc', '\U0001f0cd', '\U0001f0ce'
    d = '\U0001f0d1', '\U0001f0d2', '\U0001f0d3', '\U0001f0d4', '\U0001f0d5', '\U0001f0d6', '\U0001f0d7', '\U0001f0d8', '\U0001f0d9', '\U0001f0da', '\U0001f0db', '\U0001f0dc', '\U0001f0dd', '\U0001f0de'
    print('cards=', end='')
    for i in a:
        print('\'' + i + '\'', end=',')
    for i in b:
        print('\'' + i + '\'', end=',')
    for i in c:
        print('\'' + i + '\'', end=',')
    for i in d:
        print('\'' + i + '\'', end=',')


# print_cards()

from random import randint

def poker_hands():
    cards = '🂡', '🂢', '🂣', '🂤', '🂥', '🂦', '🂧', '🂨', '🂩', '🂪', '🂫', '🂭', '🂮', '🂱', '🂲', '🂳', '🂴', '🂵', '🂶', '🂷', '🂸', '🂹', '🂺', '🂻', '🂽', '🂾', '🃁', '🃂', '🃃', '🃄', '🃅', '🃆', '🃇', '🃈', '🃉', '🃊', '🃋', '🃍', '🃎', '🃑', '🃒', '🃓', '🃔', '🃕', '🃖', '🃗', '🃘', '🃙', '🃚', '🃛', '🃝', '🃞'
    print('🂡', '🂡'.encode('utf-8').hex()[-2:])
    for z in cards:
        print(z, z.encode('utf-8').hex()[-2:])
    ins = set()
    while len(ins) < 5:
        ins.add(randint(0, 55))
    hand = ''
    # for h in ins:
    #     hand += cards[h]
    # hand='🂢🂣🂤🂥🂦'
    hand='🃞🃎🃑🂮🃗'
    print(hand)
    en = []
    for h in hand:
        en += h.encode('utf-8').hex()[-2:]
    print(en)
    ins = set()
    for h in 1, 3, 5, 7, 9:
        ins.add(en[h])
    l = len(ins)
    if l == 5:
        ins2 = set()
        for h in 0, 2, 4, 6, 8:
            ins2.add(en[h])
        l = len(ins2)
        lis = list(ins)
        lis.sort()
        a = lis[0]
        s = ''.join(lis)
        s1 = '123456789abde'
        j = s1.find(a)
        if l > 1:
            if s == s1[j:j + 5] or s=='1abde':
                print('scala')
            else:
                print('niente')
        elif l == 1:
            if s == s1[j:j + 5] or s=='1abde':
                if s == '1abde':
                    print('scala massima')
                else:
                    print('scala reale')
            else:
                print('colore')

    elif l == 4:
        print('coppia')
    elif l == 3:
        print_options(en,3,'tris','doppia')
    elif l == 2:
        print_options(en, 4, 'poker', 'full')


import sys


def print_options(en, n, s1, s2):
    d = dict()
    for i in 1, 3, 5, 7, 9:
        if en[i] not in d:
            d[en[i]] = 1
        else:
            d[en[i]] += 1
    b = False
    for i in d.values():
        if i == n:
            b = True
            break
    if b:
        print(s1)
    else:
        print(s2)


for i in range(1, len(sys.argv)):
    en = []
    for h in sys.argv[i]:
        en += h.encode('utf-8').hex()[-2:]
    ins = set()
    for h in 1, 3, 5, 7, 9:
        ins.add(en[h])
    l = len(ins)
    if l == 5:
        ins2 = set()
        for h in 0, 2, 4, 6, 8:
            ins2.add(en[h])
        l = len(ins2)
        lis = list(ins)
        lis.sort()
        a = lis[0]
        s = ''.join(lis)
        s1 = '123456789abcde'
        j = s1.find(a)
        if l > 1:
            if s == s1[j:j + 5]:
                print('Straight')
            else:
                print('High Cards')
        elif l == 1:
            if s == s1[j:j + 5]:
                if s == 'abcde':
                    print('Royal Flush')
                else:
                    print('Straight Flush')
            else:
                print('Flush')

    elif l == 4:
        print('Pair')
    elif l == 3:
        print_options(en, 3, 'Three of a Kind', 'Two Pair')
    elif l == 2:
        print_options(en, 4, 'Four of a Kind', 'Full House')

poker_hands()
