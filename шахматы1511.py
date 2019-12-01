def king_attack_q(pos1,pos2): # является ли ситуация странной: черный король под атакой белого (или клетка под атакой короля )
    return abs(int(pos1[1]) - int(pos2[1])) <= 1 and abs(ord(pos1[0])-ord(pos2[0])) <= 1

def get_neighbors(pos,positions): #соседи
    letter = ord(pos[0])
    num = int(pos[1])
    neighbors = []
    for el in positions:
        if abs(letter-ord(el[0])) <= 1 and abs(int(num) - int(el[1])) <= 1 and pos != el:
            neighbors.append(el)
    return neighbors

def rook_attac_q(kpos, lpos): # находится ли король под атакой ладьи
    return bool(kpos[0] == lpos[0]) ^ bool(kpos[1] == lpos[1])

#может ли фигура сделать ход ?
def can_move_q(lpos, kwpos, neighbors):
    for n in neighbors:
        if not rook_attac_q(n, lpos) and not king_attack_q(n, kwpos):
            return True
    return False

class Error(Exception):
    pass

def situation_type(string): # string: бк, бл, чк
    mas = string.upper().split(" ")
    letters = set([el[0] for el in mas])
    nums = set([el[1] for el in mas])

    positions = set()
    allowed_letters = {"A","B","C","D","E","F","G","H"}
    allowed_nums = set([str(i) for i in range(1,9)])

    for letter in allowed_letters:
        for num in allowed_nums:
            positions.add(letter+num)

    try:
        if len(mas) != len(set(mas)):
            raise Error("фигуры не могут стоять на одной клетке")
        elif not letters.issubset(allowed_letters) or not nums.issubset(allowed_nums):
            raise Error("неправильно заданы позиции фигур")
        else:
            if king_attack_q(mas[0],mas[2]): #черный король под атакой белого
                return "странная"

            neighbors = get_neighbors(mas[2], positions)
            cmq = can_move_q(mas[1], mas[0], neighbors) # может сделать ход ?
            raq = rook_attac_q(mas[2], mas[1]) # под атакой ладьи ?

            if not raq and cmq:
                return "обычная"
            elif raq and cmq:
                return "шах"
            elif not raq and not cmq:
                return "пат"
            else:
                return "мат"
    except Error as error:
        return error
