from dataclasses import dataclass
import random

kolory=['♣', '♦', '♡', '♠']
wartosci=['2','3','4','5','6','7','8','9','10','J','Q','K','A']
sila={w: i for i,w in enumerate(wartosci)}

@dataclass(order=True)
class Karta:
    sila: int
    color: str
    wartosc: str

    def __init__(self, color, wartosc):
        self.color = color
        self.wartosc = wartosc
        self.sila = sila[wartosc]

    def __repr__(self):
        return self.wartosc + self.color


@dataclass
class Reka:
    karty: list

    def __iter__(self):
        return iter(self.karty)


def return_lista_kart():
    return [Karta(k, w) for k in kolory for w in wartosci]


def gra(N=5):
    lista_kart = return_lista_kart()
    random.shuffle(lista_kart)

    gracz1 = Reka(lista_kart[:N])
    gracz2 = Reka(lista_kart[N:2*N])

    tura = random.choice([1, 2])

    while gracz1.karty and gracz2.karty:

        if tura == 1:
            karta1 = random.choice(gracz1.karty)
            gracz1.karty.remove(karta1)

            lepsze = [k for k in gracz2.karty if k.sila > karta1.sila]
            if lepsze:
                karta2 = min(lepsze, key=lambda k: k.sila)
            else:
                karta2 = min(gracz2.karty, key=lambda k: k.sila)
            gracz2.karty.remove(karta2)

        else:
            karta2 = random.choice(gracz2.karty)
            gracz2.karty.remove(karta2)

            lepsze = [k for k in gracz1.karty if k.sila > karta2.sila]
            if lepsze:
                karta1 = min(lepsze, key=lambda k: k.sila)
            else:
                karta1 = min(gracz1.karty, key=lambda k: k.sila)
            gracz1.karty.remove(karta1)

        if karta1.sila > karta2.sila:
            print("Wygrywa gracz 1")
            tura = 1
        elif karta1.sila < karta2.sila:
            print("Wygrywa gracz 2")
            tura = 2
        else:
            print("Remis — ignorujemy")

    print("Koniec gry!")
    print("Gracz1 ma: " + str(len(gracz1.karty)))
    print("Gracz2 ma: " + str(len(gracz2.karty)))

if __name__ == "__main__":
    gra(N=5)



from dataclasses import dataclass



@dataclass
class NumberToken:
    value: str

@dataclass
class OperatorToken:
    op: str


@dataclass
class Number:
    value: int

@dataclass
class Op:
    op: str


@dataclass
class NumNode:
    value: int

@dataclass
class OpNode:
    op: str
    left: any
    right: any



def lexer(expr: str):
    tokens = []
    for t in expr.split():
        match t:
            case '+' | '-' | '*' | '/':
                tokens.append(OperatorToken(t))
            case _:
                tokens.append(NumberToken(t))
    return tokens



def parser(tokens):
    out = []
    for tok in tokens:
        match tok:
            case NumberToken(v):
                out.append(Number(int(v)))
            case OperatorToken(op):
                out.append(Op(op))
    return out



def build_ast(parsed):
    stack = []
    for elem in parsed:
        match elem:
            case Number(v):
                stack.append(NumNode(v))
            case Op(op):
                right = stack.pop()
                left = stack.pop()
                stack.append(OpNode(op, left, right))
    return stack[0]



def eval_ast(node):
    match node:
        case NumNode(v):
            return v
        case OpNode(op, left, right):
            a = eval_ast(left)
            b = eval_ast(right)
            if op == '+':
                return a + b
            elif op == '-':
                return a - b
            elif op == '*':
                return a * b
            elif op == '/':
                return a / b

if __name__ == "__main__":
    expr = "2 3 + 5 *"  
    tokens = lexer(expr)
    print("Tokeny:", tokens)

    parsed = parser(tokens)
    print("Po parserze:", parsed)

    ast = build_ast(parsed)
    print("AST:", ast)

    wynik = eval_ast(ast)
    print("Wynik:", wynik)
