# nokte man sefid haro paiin dar nazar gereftam
# siah haro bala  chon sarbaz (paw) farg dare koja bashe va che rangi
import os
from tkinter import *
from tkinter import messagebox


def clear():
    os.system('cls')


# create piece ID
piece_id_counter = 0
piece_id_list = []
square_list = []
black_piece_attack = []
white_piece_attack = []
black_king_kisher = []
white_king_kisher = []

block_list = []


def piece_id(name, tasir, satr, soton):
    global piece_id_counter
    piece_id_counter += 1
    globals()[f"piece_{piece_id_counter}"] = piece(name, tasir, satr, soton)
    piece_id_list.append(f"piece_{piece_id_counter}")


# square class
class square:
    def __init__(self, satr, soton, piece, asar):
        self.soton = soton
        self.satr = satr
        self.piece = piece
        self.asar = asar
        self.asarha = []

    def square_status(self):
        return self.piece


# pieces class
class piece:
    def __init__(self, name, tasir, satr, soton):
        self.tasir = tasir
        self.name = name
        self.satr = satr
        self.soton = soton

    def check_piece(self, id):
        print("\ntamami piece ha =", piece_id_list)
        print("\n" + str(id) + " =" + self.name + "\ntasirat =", self.tasir, "\nshomare square = ", str(self.satr),
              str(self.soton))


def asargozari(piece_id):  # >>>>>>>>>>>>>>>> b&w
    global block_list

    j = globals()[piece_id].satr
    i = globals()[piece_id].soton
    temp_tasir = globals()[piece_id].tasir
    # ^^^^^^^^^^^^^^^
    try:
        globals()[f"square_{str(int(j))}{str(int(i))}"].asarha = globals()[piece_id].tasir
    except:
        print("! no problem !")
    # ^^^^^^^^^^^^^^^
    removing_tasir = []
    for t in temp_tasir:
        jj = t[0]
        ii = t[1]
        if (int(j) + int(jj) <= 8) and (int(j) + int(jj) > 0) and (int(i) + int(ii) <= 8) and (
                int(i) + int(ii) > 0):
            if globals()[f"square_{str(int(j) + int(jj))}{str(int(i) + int(ii))}"].piece[0] != ".":
                block_j = int(j) + int(jj)
                block_i = int(i) + int(ii)
                if block_j == int(j) and block_i < int(i):
                    ib = 1
                    while ib <= 8:
                        try:
                            removing_tasir.append([int(j) + int(jj) + 0, int(i) + int(ii) - ib])
                            ib += 1
                        except:
                            ib += 1

                elif block_j == int(j) and block_i > int(i):
                    ib = 1
                    while ib <= 8:
                        try:
                            removing_tasir.append([int(j) + int(jj) + 0, int(i) + int(ii) + ib])
                            ib += 1
                        except:
                            ib += 1
                elif block_j < int(j) and block_i == int(i):
                    jb = 1
                    while jb <= 8:
                        try:
                            removing_tasir.append([int(j) + int(jj) - jb, int(i) + int(ii) + 0])
                            jb += 1
                        except:
                            jb += 1

                elif block_j > int(j) and block_i == int(i):
                    jb = 1
                    while jb <= 8:
                        try:
                            removing_tasir.append([int(j) + int(jj) + jb, int(i) + int(ii) + 0])
                            jb += 1
                        except:
                            jb += 1

                elif block_j < int(j) and block_i < int(i):
                    jb = 1
                    ib = 1
                    while jb <= 8:
                        try:
                            removing_tasir.append([int(j) + int(jj) - jb, int(i) + int(ii) - ib])
                            jb += 1
                            ib += 1
                        except:
                            jb += 1
                            ib += 1

                elif block_j > int(j) and block_i < int(i):
                    jb = 1
                    ib = 1
                    while jb <= 8:
                        try:
                            removing_tasir.append([int(j) + int(jj) + jb, int(i) + int(ii) - ib])
                            jb += 1
                            ib += 1
                        except:
                            jb += 1
                            ib += 1
                elif block_j > int(j) and block_i > int(i):
                    jb = 1
                    ib = 1
                    while jb <= 8:
                        try:
                            removing_tasir.append([int(j) + int(jj) + jb, int(i) + int(ii) + ib])
                            jb += 1
                            ib += 1
                        except:
                            jb += 1
                            ib += 1
                elif block_j < int(j) and block_i > int(i):
                    jb = 1
                    ib = 1
                    while jb <= 8:
                        try:
                            removing_tasir.append([int(j) + int(jj) - jb, int(i) + int(ii) + ib])
                            jb += 1
                            ib += 1
                        except:
                            jb += 1
                            ib += 1
    # ^^^^^^^^^^^^^^^^^^^

    temp_asarha = globals()[f"square_{str(int(j))}{str(int(i))}"].asarha
    temp_list_asarha = []
    for asar in temp_asarha:
        asar_j = asar[0]
        asar_i = asar[1]
        natije_j = int(asar_j) + int(j)
        natije_i = int(asar_i) + int(i)
        if (natije_j <= 8) and (natije_j > 0) and (natije_i <= 8) and (natije_i > 0):
            temp_list_asarha.append([natije_j, natije_i])
    globals()[f"square_{str(int(j))}{str(int(i))}"].asarha = temp_list_asarha

    for remove in removing_tasir:
        try:
            globals()[f"square_{str(int(j))}{str(int(i))}"].asarha.remove(remove)
        except:
            print("no problem !")

    # ^^^^^^^^^^^^^^^^^^^
    for t in temp_tasir:
        jjj = t[0]
        iii = t[1]
        temp_name = globals()[piece_id].name
        if (int(j) + int(jjj) <= 8) and (int(j) + int(jjj) > 0) and (int(i) + int(iii) <= 8) and (
                int(i) + int(iii) > 0):
            if temp_name == "p" or temp_name == "r" or temp_name == "h" or temp_name == "k" or temp_name == "b" or temp_name == "q":
                globals()[f"square_{str(int(j) + int(jjj))}{str(int(i) + int(iii))}"].piece += ")"
            elif temp_name == "P" or temp_name == "R" or temp_name == "H" or temp_name == "K" or temp_name == "B" or temp_name == "Q":
                globals()[f"square_{str(int(j) + int(jjj))}{str(int(i) + int(iii))}"].piece += "}"
    for t in removing_tasir:
        removing_j = t[0]
        removing_i = t[1]
        temp_name = globals()[piece_id].name
        try:
            if temp_name == "p" or temp_name == "r" or temp_name == "h" or temp_name == "k" or temp_name == "b" or temp_name == "q":
                globals()[f"square_{str(removing_j)}{str(removing_i)}"].piece = globals()[
                    f"square_{str(removing_j)}{str(removing_i)}"].piece.replace(")", "", 1)
            elif temp_name == "P" or temp_name == "R" or temp_name == "H" or temp_name == "K" or temp_name == "B" or temp_name == "Q":
                globals()[f"square_{str(removing_j)}{str(removing_i)}"].piece = globals()[
                    f"square_{str(removing_j)}{str(removing_i)}"].piece.replace("}", "", 1)
        except Exception as err:
            print("!", err)


def undo_asargozari():  # >>>>>>>>>>>>>>>> b&w

    for sq in square_list:
        piece_name = globals()[sq].piece[0]
        globals()[sq].piece = piece_name
        if piece_name != ".":
            print("\n asar gozari ", sq, " pak shod")


def kisher_block_finder():  # >>>>>>>>>>>>>>>> b&w
    for sq in square_list:
        sq_j = globals()[sq].satr
        sq_i = globals()[sq].soton
        piece_name = globals()[sq].piece
        piece_asarha = globals()[sq].asarha

        for asar in piece_asarha:
            asar_j = asar[0]
            asar_i = asar[1]
            temp_piece = globals()[f"square_{str(asar_j)}{str(asar_i)}"].piece
            ##### block list #####
            if piece_name[0] == "P" or piece_name[0] == "Q" or piece_name[0] == "H" or piece_name[0] == "R" or \
                    piece_name[0] == "B" or piece_name[0] == "K":
                if temp_piece[0] == "p" or temp_piece[0] == "q" or temp_piece[0] == "h" or temp_piece[0] == "r" or \
                        temp_piece[0] == "b":
                    block_list.append([asar_j, asar_i, sq_j, sq_i])
            elif piece_name[0] == "p" or piece_name[0] == "q" or piece_name[0] == "h" or piece_name[0] == "r" or \
                    piece_name[0] == "b" or piece_name[0] == "k":
                if temp_piece[0] == "P" or temp_piece[0] == "Q" or temp_piece[0] == "H" or temp_piece[0] == "R" or \
                        temp_piece[0] == "B":
                    block_list.append([asar_j, asar_i, sq_j, sq_i])
            ##### white and black kisher #####
            if piece_name[0] == "P" or piece_name[0] == "Q" or piece_name[0] == "H" or piece_name[0] == "R" or \
                    piece_name[0] == "B" or piece_name[0] == "K":
                if temp_piece[0] == "k":
                    white_king_kisher.append([sq_j, sq_i])
            elif piece_name[0] == "p" or piece_name[0] == "q" or piece_name[0] == "h" or piece_name[0] == "r" or \
                    piece_name[0] == "b" or piece_name[0] == "k":
                if temp_piece[0] == "K":
                    black_king_kisher.append([sq_j, sq_i])


def tasirat(name):  # >>>>>>>>>>>>>>>> b&w
    if name == "p":
        return [[-1, -1], [-1, +1]]
    elif name == "P":
        return [[+1, -1], [+1, +1]]
    elif name == "r":
        return [[+ 0, + 1], [+ 0, + 2], [+ 0, + 3], [+ 0, + 4], [+ 0, + 5],
                [+ 0, + 6], [+ 0, + 7], [+ 0, - 1], [+ 0, - 2], [+ 0, - 3],
                [+ 0, - 4], [+ 0, - 5], [+ 0, - 6], [+ 0, - 7], [- 1, 0], [- 2, 0],
                [- 3, 0], [- 4, 0], [- 5, 0], [- 6, 0], [- 7, 0], [+ 1, 0], [+ 2, 0],
                [+ 3, 0], [+ 4, 0], [+ 5, 0], [+ 6, 0], [+ 7, 0]]
    elif name == "R":
        return [[+ 0, + 1], [+ 0, + 2], [+ 0, + 3], [+ 0, + 4], [+ 0, + 5],
                [+ 0, + 6], [+ 0, + 7], [+ 0, - 1], [+ 0, - 2], [+ 0, - 3],
                [+ 0, - 4], [+ 0, - 5], [+ 0, - 6], [+ 0, - 7], [- 1, 0], [- 2, 0],
                [- 3, 0], [- 4, 0], [- 5, 0], [- 6, 0], [- 7, 0], [+ 1, 0], [+ 2, 0],
                [+ 3, 0], [+ 4, 0], [+ 5, 0], [+ 6, 0], [+ 7, 0]]

    elif name == "h":
        return [[- 2, + 1], [- 1, + 2], [+ 1, + 2], [+ 2, + 1], [+ 2, - 1],
                [+ 1, - 2], [- 1, - 2], [- 2, - 1]]
    elif name == "H":
        return [[- 2, + 1], [- 1, + 2], [+ 1, + 2], [+ 2, + 1], [+ 2, - 1],
                [+ 1, - 2], [- 1, - 2], [- 2, - 1]]
    elif name == "b":
        return [[- 1, + 1], [- 2, + 2], [- 3, + 3], [- 4, + 4], [- 5, + 5],
                [- 6, + 6], [- 7, + 7], [+ 1, + 1], [+ 2, + 2], [+ 3, + 3],
                [+ 4, + 4], [+ 5, + 5], [+ 6, + 6], [+ 7, + 7], [- 1, - 1],
                [- 2, - 2], [- 3, - 3], [- 4, - 4], [- 5, - 5], [- 6, - 6],
                [- 7, - 7], [+ 1, - 1], [+ 2, - 2], [+ 3, - 3], [+ 4, - 4],
                [+ 5, - 5], [+ 6, - 6], [+ 7, - 7]]
    elif name == "B":
        return [[- 1, + 1], [- 2, + 2], [- 3, + 3], [- 4, + 4], [- 5, + 5],
                [- 6, + 6], [- 7, + 7], [+ 1, + 1], [+ 2, + 2], [+ 3, + 3],
                [+ 4, + 4], [+ 5, + 5], [+ 6, + 6], [+ 7, + 7], [- 1, - 1],
                [- 2, - 2], [- 3, - 3], [- 4, - 4], [- 5, - 5], [- 6, - 6],
                [- 7, - 7], [+ 1, - 1], [+ 2, - 2], [+ 3, - 3], [+ 4, - 4],
                [+ 5, - 5], [+ 6, - 6], [+ 7, - 7]]
    elif name == "q":
        return [[- 1, + 1], [- 2, + 2], [- 3, + 3], [- 4, + 4], [- 5, + 5],
                [- 6, + 6], [- 7, + 7], [+ 1, + 1], [+ 2, + 2], [+ 3, + 3],
                [+ 4, + 4], [+ 5, + 5], [+ 6, + 6], [+ 7, + 7], [- 1, - 1],
                [- 2, - 2], [- 3, - 3], [- 4, - 4], [- 5, - 5], [- 6, - 6],
                [- 7, - 7], [+ 1, - 1], [+ 2, - 2], [+ 3, - 3], [+ 4, - 4],
                [+ 5, - 5], [+ 6, - 6], [+ 7, - 7], [+ 0, + 1], [+ 0, + 2],
                [+ 0, + 3], [+ 0, + 4], [+ 0, + 5], [+ 0, + 6], [+ 0, + 7],
                [+ 0, - 1], [+ 0, - 2], [+ 0, - 3], [+ 0, - 4], [+ 0, - 5],
                [+ 0, - 6], [+ 0, - 7], [- 1, 0], [- 2, 0], [- 3, 0], [- 4, 0],
                [- 5, 0], [- 6, 0], [- 7, 0], [+ 1, 0], [+ 2, 0], [+ 3, 0], [+ 4, 0],
                [+ 5, 0], [+ 6, 0], [+ 7, 0]]
    elif name == "Q":
        return [[- 1, + 1], [- 2, + 2], [- 3, + 3], [- 4, + 4], [- 5, + 5],
                [- 6, + 6], [- 7, + 7], [+ 1, + 1], [+ 2, + 2], [+ 3, + 3],
                [+ 4, + 4], [+ 5, + 5], [+ 6, + 6], [+ 7, + 7], [- 1, - 1],
                [- 2, - 2], [- 3, - 3], [- 4, - 4], [- 5, - 5], [- 6, - 6],
                [- 7, - 7], [+ 1, - 1], [+ 2, - 2], [+ 3, - 3], [+ 4, - 4],
                [+ 5, - 5], [+ 6, - 6], [+ 7, - 7], [+ 0, + 1], [+ 0, + 2],
                [+ 0, + 3], [+ 0, + 4], [+ 0, + 5], [+ 0, + 6], [+ 0, + 7],
                [+ 0, - 1], [+ 0, - 2], [+ 0, - 3], [+ 0, - 4], [+ 0, - 5],
                [+ 0, - 6], [+ 0, - 7], [- 1, 0], [- 2, 0], [- 3, 0], [- 4, 0],
                [- 5, 0], [- 6, 0], [- 7, 0], [+ 1, 0], [+ 2, 0], [+ 3, 0], [+ 4, 0],
                [+ 5, 0], [+ 6, 0], [+ 7, 0]]
    elif name == "k":
        return [[- 1, - 1], [- 1, 0], [- 1, + 1], [+ 0, - 1], [+ 0, + 1], [+ 1, - 1],
                [+ 1, 0], [+ 1, + 1]]
    elif name == "K":
        return [[- 1, - 1], [- 1, 0], [- 1, + 1], [+ 0, - 1], [+ 0, + 1], [+ 1, - 1],
                [+ 1, 0], [+ 1, + 1]]


# chess functions
"""def check_status(j,i):
    square_dis=10-len(globals()[f"square_{j}{i}"].piece)
    distance=""
    while square_dis>0:
        distance+=" "
        square_dis-=1
    if i > 1:
        print(str(globals()[f"square_{j}{i}"].square_status()) + distance, end=" ")
    else:
        print("\n\n\n")
        print(str(globals()[f"square_{j}{i}"].square_status()) + distance, end=" ")

def check_piece_status():
    for item in piece_id_list:
        globals()[item].check_piece(item)"""
"""def change_piece():
    counter = 0
    try:
        while(counter==0):
            print("\n 1-add piece to square \n 2-remove piece \n 0-Finish changing piece")
            choose_piece_menu=int(input("\n your choose ? ="))
            if choose_piece_menu == 1:
                add_piece()
            elif choose_piece_menu ==2:
                remove_piece()
            elif choose_piece_menu ==0:
                counter=1
    except Exception as err:
        print("!",err)"""


def add_piece(vorodi):
    clear()
    j = vorodi[0]
    i = vorodi[1]
    piece_name = vorodi[2]
    print("\n menu -> Change piece -> add_piece")

    try:
        choosen_square_j = j
        choosen_square_i = i
        choosen_piece = piece_name
        if (int(choosen_square_i) > 0) and (int(choosen_square_j) > 0) and (int(choosen_square_i) < 9) and (
                int(choosen_square_j) < 9):
            if choosen_piece == "p" or choosen_piece == "P" or choosen_piece == "k" or choosen_piece == "K" or choosen_piece == "b" or choosen_piece == "B" or choosen_piece == "h" or choosen_piece == "H" or choosen_piece == "Q" or choosen_piece == "q" or choosen_piece == "r" or choosen_piece == "R":
                piece_id(choosen_piece, tasirat(choosen_piece), choosen_square_j, choosen_square_i)
                globals()[f"square_{choosen_square_j}{choosen_square_i}"].piece = choosen_piece
                globals()[f"square_{choosen_square_j}{choosen_square_i}"].asar = tasirat(choosen_piece)
    except Exception as err:
        print("\n### Error ! ### =  satr va soton bayad beyn 1 ta 8 bashad !", err)

    else:
        print("\n baraye add kardan piece jadid undo asargozari ra ejra konid !")


"""def remove_piece():
    clear()
    print("\n menu -> Change piece -> Remove piece")

        try:
            id_num=input("shomare id mored nazar ra vared konid =")
            choosen_square_j=globals()[f"piece_{id_num}"].satr
            choosen_square_i=globals()[f"piece_{id_num}"].soton
            globals()[f"square_{choosen_square_j}{choosen_square_i}"].piece ='.'
            globals()[f"square_{choosen_square_j}{choosen_square_i}"].asar = []
            piece_id_list.remove(f"piece_{id_num}")
            del globals()[f"piece_{id_num}"]
        except Exception as err:
            print("\n### Error ! ### =  satr va soton ID bayad beyn 1 ta 8 bashad !",err)

    else:
        print("\n baraye remove kardan piece bayad undo asargozari ra ejra konid !")"""
# check and mate

white_kish = 0
black_kish = 0
white_mate = 0
black_mate = 0

black_king_move_list = []
white_king_move_list = []
black_king_kish_list = []
white_king_kish_list = []

black_king_position = []
white_king_position = []
wehave_white_king = False
wehave_black_king = False


def kish_check():  # >>>>>>>>>>>>>>>> b&w
    global white_kish
    global black_kish
    global wehave_white_king
    global wehave_black_king
    for s in square_list:
        if globals()[s].piece[0] == "k":
            wehave_white_king = True
            piece_len = len(globals()[s].piece)
            try:
                while piece_len > 0:
                    if globals()[s].piece[piece_len - 1] == "}":
                        white_kish = 1
                        print("white kish shod")
                    piece_len -= 1
            except Exception as err:
                print("!", err)
        elif globals()[s].piece[0] == "K":
            wehave_black_king = True
            piece_len = len(globals()[s].piece)
            try:
                while piece_len > 0:
                    if globals()[s].piece[piece_len - 1] == ")":
                        black_kish = 1
                        print("black kish shod")
                    piece_len -= 1
            except Exception as err:
                print("!", err)


def check_check():  # >>>>>>>>>>>>>>>> b&w
    global white_kish
    global black_kish
    global white_mate
    global black_mate
    global king_moves
    global white_king_move_list
    global black_king_move_list
    if white_kish == 1 or black_kish == 1:
        try:
            for sq in square_list:
                temp_king_moves = [[-1, -1], [-1, +0], [-1, +1], [+0, -1], [+0, +1], [+1, -1], [+1, +0], [+1, +1]]
                king_moves = [[-1, -1], [-1, +0], [-1, +1], [+0, -1], [+0, +1], [+1, -1], [+1, +0], [+1, +1]]
                if globals()[f"{sq}"].piece[0] == "k" or globals()[f"{sq}"].piece[0] == "K":
                    king_j = globals()[f"{sq}"].satr
                    king_i = globals()[f"{sq}"].soton
                    for move in king_moves:
                        move_j = move[0]
                        move_i = move[1]
                        hadaf_j = king_j + move_j
                        hadaf_i = king_i + move_i
                        if hadaf_j > 0 and hadaf_i > 0 and hadaf_j < 9 and hadaf_i < 9:
                            temp_piece = globals()[f"square_{hadaf_j}{hadaf_i}"].piece

                            try:
                                if globals()[f"{sq}"].piece[0] == "k":
                                    for st in temp_piece:
                                        if st == "}" or st == "p" or st == "h" or st == "q" or st == "b" or st == "r":
                                            try:
                                                temp_king_moves.remove(move)
                                            except Exception as err:
                                                print("err toye check_check ", err)

                                elif globals()[f"{sq}"].piece[0] == "K":
                                    for st in temp_piece:
                                        if st == ")" or st == "P" or st == "H" or st == "Q" or st == "B" or st == "R":

                                            try:
                                                temp_king_moves.remove(move)
                                            except Exception as err:
                                                print("err toye check_check ", err)
                            except Exception as err:
                                print("!", err)

                        else:
                            try:
                                temp_king_moves.remove(move)
                            except Exception as err:
                                print("err toye check_check ", err)
                if globals()[f"{sq}"].piece[0] == "k":
                    white_king_move_list = temp_king_moves
                elif globals()[f"{sq}"].piece[0] == "K":
                    black_king_move_list = temp_king_moves
        except Exception as err:
            print("err toye check check ", err)


def uncheck_king_byking():  # >>>>>>>>>>>>>>>> b&w
    global white_king_move_list
    global black_king_move_list
    print(">>>>>>>>>>>>>>>>>>>> 1", black_king_move_list)
    for sq in square_list:

        if globals()[f"{sq}"].piece[0] == "k":
            king_j = globals()[f"{sq}"].satr
            king_i = globals()[f"{sq}"].soton
            white_king_position.append(globals()[f"{sq}"].satr)
            white_king_position.append(globals()[f"{sq}"].soton)
            for move in white_king_move_list:

                move_j = move[0]
                move_i = move[1]
                hadaf_j = king_j + move_j
                hadaf_i = king_i + move_i
                if hadaf_j > 0 and hadaf_i > 0 and hadaf_j < 9 and hadaf_i < 9:

                    temp_piece = globals()[f"square_{hadaf_j}{hadaf_i}"].piece
                    king_can_attack = True
                    if temp_piece[0] != ".":
                        if temp_piece[0] == "P" or temp_piece[0] == "R" or temp_piece[0] == "B" or temp_piece[
                            0] == "Q" or temp_piece[0] == "H":

                            for st in temp_piece:
                                if st == "}":
                                    king_can_attack = False
                        else:
                            king_can_attack = False
                    else:
                        king_can_attack = True
                    if king_can_attack == False:
                        try:
                            white_king_move_list.remove(move)
                        except Exception as err:
                            print("err toye unckeck by king ", err)
        elif globals()[f"{sq}"].piece[0] == "K":

            king_j = globals()[f"{sq}"].satr
            king_i = globals()[f"{sq}"].soton
            black_king_position.append(globals()[f"{sq}"].satr)
            black_king_position.append(globals()[f"{sq}"].soton)
            for move in black_king_move_list:

                move_j = move[0]
                move_i = move[1]
                hadaf_j = king_j + move_j
                hadaf_i = king_i + move_i
                if hadaf_j > 0 and hadaf_i > 0 and hadaf_j < 9 and hadaf_i < 9:

                    temp_piece = globals()[f"square_{hadaf_j}{hadaf_i}"].piece
                    king_can_attack = True
                    if temp_piece[0] != ".":
                        if temp_piece[0] == "p" or temp_piece[0] == "r" or temp_piece[0] == "b" or temp_piece[
                            0] == "q" or temp_piece[0] == "h":
                            for st in temp_piece:
                                if st == ")":
                                    king_can_attack = False
                        else:
                            king_can_attack = False
                    else:
                        king_can_attack = True
                    if king_can_attack == False:
                        try:
                            black_king_move_list.remove(move)
                        except Exception as err:
                            print("err toye unckeck by king ", err)
        print(">>>>>> 2", black_king_move_list)

        if globals()[f"{sq}"].piece[0] == "k":
            king_cant_move = []
            king2_j = globals()[f"{sq}"].satr
            king2_i = globals()[f"{sq}"].soton
            temp_white_move = white_king_move_list
            for move2 in temp_white_move:
                move2_j = int(move2[0])
                move2_i = int(move2[1])
                ############################
                if move2_j == 1 and move2_i == 1:
                    king_cant_move = []
                    position_check_jmanfi_imanfi = [[- 1, - 1], [- 2, - 2], [- 3, - 3], [- 4, - 4], [- 5, - 5],
                                                    [- 6, - 6], [- 7, - 7]]

                    for check in position_check_jmanfi_imanfi:
                        hadaf2_j = king2_j + check[0]
                        hadaf2_i = king2_i + check[1]
                        try:
                            temp_piece = globals()[f"square_{hadaf2_j}{hadaf2_i}"].piece[0]
                            if temp_piece == "B" or temp_piece == "Q":
                                king_cant_move.append(True)
                            else:
                                king_cant_move.append(False)
                        except Exception as err:
                            print("!", err)
                    for cant in king_cant_move:
                        if cant == True:
                            try:
                                white_king_move_list.remove(move2)
                            except Exception as err:
                                print("err toye unckeck by king ", err)
                        ###############1##ok############
                if move2_j == 1 and move2_i == -1:
                    king_cant_move = []
                    position_check_jmanfi_imosbat = [[- 1, + 1], [- 2, + 2], [- 3, + 3], [- 4, + 4], [- 5, + 5],
                                                     [- 6, + 6], [- 7, + 7]]

                    for check in position_check_jmanfi_imosbat:
                        hadaf2_j = king2_j + check[0]
                        hadaf2_i = king2_i + check[1]
                        try:
                            temp_piece = globals()[f"square_{hadaf2_j}{hadaf2_i}"].piece[0]
                            if temp_piece == "B" or temp_piece == "Q":
                                king_cant_move.append(True)
                            else:
                                king_cant_move.append(False)
                        except Exception as err:
                            print("!", err)
                    for cant in king_cant_move:
                        if cant == True:
                            try:
                                white_king_move_list.remove(move2)
                            except Exception as err:
                                print("err toye unckeck by king ", err)
                ###############2##ok############
                if move2_j == -1 and move2_i == -1:
                    king_cant_move = []
                    position_check_jmosbat_imosbat = [[+ 1, + 1], [+ 2, + 2], [+ 3, + 3], [+ 4, + 4], [+ 5, + 5],
                                                      [+ 6, + 6], [+ 7, + 7]]
                    for check in position_check_jmosbat_imosbat:
                        hadaf2_j = king2_j + check[0]
                        hadaf2_i = king2_i + check[1]
                        try:
                            temp_piece = globals()[f"square_{hadaf2_j}{hadaf2_i}"].piece[0]
                            if temp_piece == "B" or temp_piece == "Q":
                                king_cant_move.append(True)
                            else:
                                king_cant_move.append(False)
                        except Exception as err:
                            print("!", err)
                    for cant in king_cant_move:
                        if cant == True:
                            try:
                                white_king_move_list.remove(move2)
                            except Exception as err:
                                print("err toye unckeck by king ", err)
                ###############3##ok############
                if move2_j == -1 and move2_i == 1:
                    king_cant_move = []
                    position_check_jmosbat_imanfi = [[+ 1, - 1], [+ 2, - 2], [+ 3, - 3], [+ 4, - 4], [+ 5, - 5],
                                                     [+ 6, - 6], [+ 7, - 7]]
                    for check in position_check_jmosbat_imanfi:
                        hadaf2_j = king2_j + check[0]
                        hadaf2_i = king2_i + check[1]
                        try:
                            temp_piece = globals()[f"square_{hadaf2_j}{hadaf2_i}"].piece[0]
                            if temp_piece == "B" or temp_piece == "Q":
                                king_cant_move.append(True)
                            else:
                                king_cant_move.append(False)
                        except Exception as err:
                            print("!", err)
                    for cant in king_cant_move:
                        if cant == True:
                            try:
                                white_king_move_list.remove(move2)
                            except Exception as err:
                                print("err toye unckeck by king ", err)
                ###############4##ok############
                if move2_j == 0 and move2_i == 1:
                    king_cant_move = []
                    position_check_jsabet_imanfi = [[+ 0, - 1], [+ 0, - 2], [+ 0, - 3], [+ 0, - 4], [+ 0, - 5],
                                                    [+ 0, - 6], [+ 0, - 7]]

                    for check in position_check_jsabet_imanfi:
                        hadaf2_j = king2_j + check[0]
                        hadaf2_i = king2_i + check[1]
                        try:
                            temp_piece = globals()[f"square_{hadaf2_j}{hadaf2_i}"].piece[0]
                            if temp_piece == "R" or temp_piece == "Q":
                                king_cant_move.append(True)
                            else:
                                king_cant_move.append(False)
                        except Exception as err:
                            print("!", err)
                    for cant in king_cant_move:
                        if cant == True:
                            try:
                                white_king_move_list.remove(move2)
                            except Exception as err:
                                print("err toye unckeck by king ", err)
                ###############5##ok############
                if move2_j == 0 and move2_i == -1:
                    king_cant_move = []
                    position_check_jsabet_imosbat = [[+ 0, + 1], [+ 0, + 2], [+ 0, + 3], [+ 0, + 4], [+ 0, + 5],
                                                     [+ 0, + 6], [+ 0, + 7]]
                    for check in position_check_jsabet_imosbat:
                        hadaf2_j = king2_j + check[0]
                        hadaf2_i = king2_i + check[1]
                        try:
                            temp_piece = globals()[f"square_{hadaf2_j}{hadaf2_i}"].piece[0]
                            if temp_piece == "R" or temp_piece == "Q":
                                king_cant_move.append(True)
                            else:
                                king_cant_move.append(False)
                        except Exception as err:
                            print("!", err)
                    for cant in king_cant_move:
                        if cant == True:
                            try:
                                white_king_move_list.remove(move2)
                            except Exception as err:
                                print("err toye unckeck by king ", err)
                ###############6##ok############
                if move2_j == -1 and move2_i == 0:
                    king_cant_move = []
                    position_check_jmosbat_isabet = [[+ 1, 0], [+ 2, 0], [+ 3, 0], [+ 4, 0], [+ 5, 0], [+ 6, 0],
                                                     [+ 7, 0]]

                    for check in position_check_jmosbat_isabet:
                        hadaf2_j = king2_j + check[0]
                        hadaf2_i = king2_i + check[1]
                        try:
                            temp_piece = globals()[f"square_{hadaf2_j}{hadaf2_i}"].piece[0]
                            if temp_piece == "R" or temp_piece == "Q":
                                king_cant_move.append(True)
                            else:
                                king_cant_move.append(False)
                        except Exception as err:
                            print("!", err)
                    for cant in king_cant_move:
                        if cant == True:
                            try:
                                white_king_move_list.remove(move2)
                            except Exception as err:
                                print("err toye unckeck by king ", err)
                ###############7##ok############
                if move2_j == 1 and move2_i == 0:
                    king_cant_move = []
                    position_check_jmanfi_isabet = [[- 1, 0], [- 2, 0], [- 3, 0], [- 4, 0], [- 5, 0], [- 6, 0],
                                                    [- 7, 0]]
                    for check in position_check_jmanfi_isabet:
                        hadaf2_j = king2_j + check[0]
                        hadaf2_i = king2_i + check[1]
                        try:
                            temp_piece = globals()[f"square_{hadaf2_j}{hadaf2_i}"].piece[0]
                            if temp_piece == "R" or temp_piece == "Q":
                                king_cant_move.append(True)
                            else:
                                king_cant_move.append(False)
                        except Exception as err:
                            print("!", err)
                    for cant in king_cant_move:
                        if cant == True:
                            try:
                                white_king_move_list.remove(move2)
                            except Exception as err:
                                print("err toye unckeck by king ", err)
                ##############8##ok#############
        elif globals()[f"{sq}"].piece[0] == "K":
            king_cant_move = []
            king2_j = globals()[f"{sq}"].satr
            king2_i = globals()[f"{sq}"].soton
            temp_black_move = black_king_move_list
            for move2 in temp_black_move:
                move2_j = int(move2[0])
                move2_i = int(move2[1])
                ############################
                if move2_j == 1 and move2_i == 1:
                    king_cant_move = []
                    position_check_jmanfi_imanfi = [[- 1, - 1], [- 2, - 2], [- 3, - 3], [- 4, - 4], [- 5, - 5],
                                                    [- 6, - 6], [- 7, - 7]]

                    for check in position_check_jmanfi_imanfi:
                        hadaf2_j = king2_j + check[0]
                        hadaf2_i = king2_i + check[1]
                        try:
                            temp_piece = globals()[f"square_{hadaf2_j}{hadaf2_i}"].piece[0]
                            if temp_piece == "b" or temp_piece == "q":
                                king_cant_move.append(True)
                            else:
                                king_cant_move.append(False)
                        except Exception as err:
                            print("!", err)
                    for cant in king_cant_move:
                        if cant == True:
                            try:
                                black_king_move_list.remove(move2)
                            except Exception as err:
                                print("err toye unckeck by king ", err)
                        ###############1##ok############
                if move2_j == 1 and move2_i == -1:
                    king_cant_move = []
                    position_check_jmanfi_imosbat = [[- 1, + 1], [- 2, + 2], [- 3, + 3], [- 4, + 4], [- 5, + 5],
                                                     [- 6, + 6], [- 7, + 7]]

                    for check in position_check_jmanfi_imosbat:
                        hadaf2_j = king2_j + check[0]
                        hadaf2_i = king2_i + check[1]
                        try:
                            temp_piece = globals()[f"square_{hadaf2_j}{hadaf2_i}"].piece[0]
                            if temp_piece == "b" or temp_piece == "q":
                                king_cant_move.append(True)
                            else:
                                king_cant_move.append(False)
                        except Exception as err:
                            print("!", err)
                    for cant in king_cant_move:
                        if cant == True:
                            try:
                                black_king_move_list.remove(move2)
                            except Exception as err:
                                print("err toye unckeck by king ", err)
                ###############2##ok############
                if move2_j == -1 and move2_i == -1:
                    king_cant_move = []
                    position_check_jmosbat_imosbat = [[+ 1, + 1], [+ 2, + 2], [+ 3, + 3], [+ 4, + 4], [+ 5, + 5],
                                                      [+ 6, + 6], [+ 7, + 7]]
                    for check in position_check_jmosbat_imosbat:
                        hadaf2_j = king2_j + check[0]
                        hadaf2_i = king2_i + check[1]
                        try:
                            temp_piece = globals()[f"square_{hadaf2_j}{hadaf2_i}"].piece[0]
                            if temp_piece == "b" or temp_piece == "q":
                                king_cant_move.append(True)
                            else:
                                king_cant_move.append(False)
                        except Exception as err:
                            print("!", err)
                    for cant in king_cant_move:
                        if cant == True:
                            try:
                                black_king_move_list.remove(move2)
                            except Exception as err:
                                print("err toye unckeck by king ", err)
                ###############3##ok############
                if move2_j == -1 and move2_i == 1:
                    king_cant_move = []
                    position_check_jmosbat_imanfi = [[+ 1, - 1], [+ 2, - 2], [+ 3, - 3], [+ 4, - 4], [+ 5, - 5],
                                                     [+ 6, - 6], [+ 7, - 7]]
                    for check in position_check_jmosbat_imanfi:
                        hadaf2_j = king2_j + check[0]
                        hadaf2_i = king2_i + check[1]
                        try:
                            temp_piece = globals()[f"square_{hadaf2_j}{hadaf2_i}"].piece[0]
                            if temp_piece == "b" or temp_piece == "q":
                                king_cant_move.append(True)
                            else:
                                king_cant_move.append(False)
                        except Exception as err:
                            print("!", err)
                    for cant in king_cant_move:
                        if cant == True:
                            try:
                                black_king_move_list.remove(move2)
                            except Exception as err:
                                print("err toye unckeck by king ", err)
                ###############4##ok############
                if move2_j == 0 and move2_i == 1:
                    king_cant_move = []
                    position_check_jsabet_imanfi = [[+ 0, - 1], [+ 0, - 2], [+ 0, - 3], [+ 0, - 4], [+ 0, - 5],
                                                    [+ 0, - 6], [+ 0, - 7]]

                    for check in position_check_jsabet_imanfi:
                        hadaf2_j = king2_j + check[0]
                        hadaf2_i = king2_i + check[1]
                        try:
                            temp_piece = globals()[f"square_{hadaf2_j}{hadaf2_i}"].piece[0]
                            if temp_piece == "r" or temp_piece == "q":
                                king_cant_move.append(True)
                            else:
                                king_cant_move.append(False)
                        except Exception as err:
                            print("!", err)
                    for cant in king_cant_move:
                        if cant == True:
                            try:
                                black_king_move_list.remove(move2)
                            except Exception as err:
                                print("err toye unckeck by king ", err)
                ###############5##ok############
                if move2_j == 0 and move2_i == -1:
                    king_cant_move = []
                    position_check_jsabet_imosbat = [[+ 0, + 1], [+ 0, + 2], [+ 0, + 3], [+ 0, + 4], [+ 0, + 5],
                                                     [+ 0, + 6], [+ 0, + 7]]
                    for check in position_check_jsabet_imosbat:
                        hadaf2_j = king2_j + check[0]
                        hadaf2_i = king2_i + check[1]
                        try:
                            temp_piece = globals()[f"square_{hadaf2_j}{hadaf2_i}"].piece[0]
                            if temp_piece == "r" or temp_piece == "q":
                                king_cant_move.append(True)
                            else:
                                king_cant_move.append(False)
                        except Exception as err:
                            print("!", err)
                    for cant in king_cant_move:
                        if cant == True:
                            try:
                                black_king_move_list.remove(move2)
                            except Exception as err:
                                print("err toye unckeck by king ", err)
                ###############6##ok############
                if move2_j == -1 and move2_i == 0:
                    king_cant_move = []
                    position_check_jmosbat_isabet = [[+ 1, 0], [+ 2, 0], [+ 3, 0], [+ 4, 0], [+ 5, 0], [+ 6, 0],
                                                     [+ 7, 0]]

                    for check in position_check_jmosbat_isabet:
                        hadaf2_j = king2_j + check[0]
                        hadaf2_i = king2_i + check[1]
                        try:
                            temp_piece = globals()[f"square_{hadaf2_j}{hadaf2_i}"].piece[0]
                            if temp_piece == "r" or temp_piece == "q":
                                king_cant_move.append(True)
                            else:
                                king_cant_move.append(False)
                        except Exception as err:
                            print("!", err)
                    for cant in king_cant_move:
                        if cant == True:
                            try:
                                black_king_move_list.remove(move2)
                            except Exception as err:
                                print("err toye unckeck by king ", err)
                ###############7##ok############
                if move2_j == 1 and move2_i == 0:
                    king_cant_move = []
                    position_check_jmanfi_isabet = [[- 1, 0], [- 2, 0], [- 3, 0], [- 4, 0], [- 5, 0], [- 6, 0],
                                                    [- 7, 0]]
                    for check in position_check_jmanfi_isabet:
                        hadaf2_j = king2_j + check[0]
                        hadaf2_i = king2_i + check[1]
                        try:
                            temp_piece = globals()[f"square_{hadaf2_j}{hadaf2_i}"].piece[0]
                            if temp_piece == "r" or temp_piece == "q":
                                king_cant_move.append(True)
                            else:
                                king_cant_move.append(False)
                        except Exception as err:
                            print("!", err)
                    for cant in king_cant_move:
                        if cant == True:
                            try:
                                black_king_move_list.remove(move2)
                            except Exception as err:
                                print("err toye unckeck by king ", err)
                ##############8##ok#############
    print(">>>>>>>>>>>>>>>>>>>> 3", black_king_move_list)


black_friendly = []
white_friendly = []
black_piece_uncheck = []
white_piece_uncheck = []
apiece_can_uncheck_black = False
apiece_can_uncheck_white = False


def uncheck_king_bypiece():  # >>>>>>>>>>>>>>>> b&w

    global white_mate
    global black_mate
    global white_king_move_list
    global black_king_move_list
    global white_king_position
    global black_king_position
    global black_king_kisher
    global white_king_kisher
    global black_friendly
    global white_friendly
    global white_piece_uncheck
    global black_piece_uncheck
    global apiece_can_uncheck_black
    global apiece_can_uncheck_white
    counter = 0
    temp_move_list_b = black_king_move_list
    temp_len_move_list_b = len(temp_move_list_b)
    temp_list = []
    if temp_len_move_list_b == 0:

        for kisher in black_king_kisher:
            kisher_j = kisher[0]
            kisher_i = kisher[1]

            for blocker in block_list:
                if blocker[0] == kisher_j and blocker[1] == kisher_i:

                    ####################

                    try:
                        position_check_jsabet_imosbat = [[+ 0, + 1], [+ 0, + 2], [+ 0, + 3], [+ 0, + 4], [+ 0, + 5],
                                                         [+ 0, + 6], [+ 0, + 7]]

                        for move in position_check_jsabet_imosbat:
                            move_j = move[0]
                            move_i = move[1]
                            king_j = black_king_position[0]
                            king_i = black_king_position[1]
                            hadaf_j = move_j + king_j
                            hadaf_i = move_i + king_i

                            if hadaf_j > 0 and hadaf_i > 0 and hadaf_j < 9 and hadaf_i < 9:
                                temp_piece = globals()[f"square_{hadaf_j}{hadaf_i}"].piece
                                if blocker[2] == hadaf_j and blocker[3] == hadaf_i and temp_piece[0] != "k" and \
                                        temp_piece[0] != "b" and temp_piece[0] != "h" and temp_piece[0] != "p" and \
                                        temp_piece[0] != "q" and temp_piece[0] != "r":
                                    piece_checked = 0
                                    for move2 in position_check_jsabet_imosbat:
                                        move2_j = move2[0]
                                        move2_i = move2[1]
                                        check_j = move2_j + hadaf_j
                                        check_i = move2_i + hadaf_i
                                        temp_piece2 = globals()[f"square_{check_j}{check_i}"].piece
                                        if temp_piece2[0] == "r" or temp_piece2[0] == "q":
                                            temp_list.append([hadaf_j, hadaf_i, False])
                                            piece_checked = 1
                                        elif temp_piece2[0] == "p" or temp_piece2[0] == "b" or [0] == "k" or \
                                                temp_piece2[0] == "h":
                                            temp_list.append([hadaf_j, hadaf_i, True])
                                            piece_checked = 1
                                        elif temp_piece2[0] == "Q" or temp_piece2[0] == "P" or temp_piece2[0] == "R" or \
                                                temp_piece2[0] == "K" or temp_piece2[0] == "H" or temp_piece2[0] == "B":
                                            temp_list.append([hadaf_j, hadaf_i, True])
                                            piece_checked = 1
                                    if piece_checked == 0:
                                        temp_list.append([hadaf_j, hadaf_i, True])

                        position_check_jsabet_imanfi = [[+ 0, - 1], [+ 0, - 2], [+ 0, - 3], [+ 0, - 4], [+ 0, - 5],
                                                        [+ 0, - 6], [+ 0, - 7]]
                        for move in position_check_jsabet_imanfi:
                            move_j = move[0]
                            move_i = move[1]
                            king_j = black_king_position[0]
                            king_i = black_king_position[1]
                            hadaf_j = move_j + king_j
                            hadaf_i = move_i + king_i

                            if hadaf_j > 0 and hadaf_i > 0 and hadaf_j < 9 and hadaf_i < 9:
                                temp_piece = globals()[f"square_{hadaf_j}{hadaf_i}"].piece
                                if blocker[2] == hadaf_j and blocker[3] == hadaf_i and temp_piece[0] != "k" and \
                                        temp_piece[0] != "b" and temp_piece[0] != "h" and temp_piece[0] != "p" and \
                                        temp_piece[0] != "q" and temp_piece[0] != "r":
                                    piece_checked = 0
                                    for move2 in position_check_jsabet_imanfi:
                                        move2_j = move2[0]
                                        move2_i = move2[1]
                                        check_j = move2_j + hadaf_j
                                        check_i = move2_i + hadaf_i
                                        temp_piece2 = globals()[f"square_{check_j}{check_i}"].piece
                                        if temp_piece2[0] == "r" or temp_piece2[0] == "q":
                                            temp_list.append([hadaf_j, hadaf_i, False])
                                            piece_checked = 1
                                        elif temp_piece2[0] == "p" or temp_piece2[0] == "b" or [0] == "k" or \
                                                temp_piece2[
                                                    0] == "h":
                                            temp_list.append([hadaf_j, hadaf_i, True])
                                            piece_checked = 1
                                        elif temp_piece2[0] == "Q" or temp_piece2[0] == "P" or temp_piece2[0] == "R" or \
                                                temp_piece2[0] == "K" or temp_piece2[0] == "H" or temp_piece2[0] == "B":
                                            temp_list.append([hadaf_j, hadaf_i, True])
                                            piece_checked = 1
                                    if piece_checked == 0:
                                        temp_list.append([hadaf_j, hadaf_i, True])

                        position_check_jmosbat_isabet = [[+ 1, 0], [+ 2, 0], [+ 3, 0], [+ 4, 0], [+ 5, 0], [+ 6, 0],
                                                         [+ 7, 0]]
                        for move in position_check_jmosbat_isabet:
                            move_j = move[0]
                            move_i = move[1]
                            king_j = black_king_position[0]
                            king_i = black_king_position[1]
                            hadaf_j = move_j + king_j
                            hadaf_i = move_i + king_i

                            if hadaf_j > 0 and hadaf_i > 0 and hadaf_j < 9 and hadaf_i < 9:
                                temp_piece = globals()[f"square_{hadaf_j}{hadaf_i}"].piece
                                if blocker[2] == hadaf_j and blocker[3] == hadaf_i and temp_piece[0] != "k" and \
                                        temp_piece[0] != "b" and temp_piece[0] != "h" and temp_piece[0] != "p" and \
                                        temp_piece[0] != "q" and temp_piece[0] != "r":
                                    piece_checked = 0
                                    for move2 in position_check_jmosbat_isabet:
                                        move2_j = move2[0]
                                        move2_i = move2[1]
                                        check_j = move2_j + hadaf_j
                                        check_i = move2_i + hadaf_i
                                        temp_piece2 = globals()[f"square_{check_j}{check_i}"].piece
                                        if temp_piece2[0] == "r" or temp_piece2[0] == "q":
                                            temp_list.append([hadaf_j, hadaf_i, False])
                                            piece_checked = 1
                                        elif temp_piece2[0] == "p" or temp_piece2[0] == "b" or [0] == "k" or \
                                                temp_piece2[
                                                    0] == "h":
                                            temp_list.append([hadaf_j, hadaf_i, True])
                                            piece_checked = 1
                                        elif temp_piece2[0] == "Q" or temp_piece2[0] == "P" or temp_piece2[0] == "R" or \
                                                temp_piece2[0] == "K" or temp_piece2[0] == "H" or temp_piece2[0] == "B":
                                            temp_list.append([hadaf_j, hadaf_i, True])
                                            piece_checked = 1
                                    if piece_checked == 0:
                                        temp_list.append([hadaf_j, hadaf_i, True])

                        position_check_jmanfi_isabet = [[- 1, 0], [- 2, 0], [- 3, 0], [- 4, 0], [- 5, 0], [- 6, 0],
                                                        [- 7, 0]]
                        for move in position_check_jmanfi_isabet:
                            move_j = move[0]
                            move_i = move[1]
                            king_j = black_king_position[0]
                            king_i = black_king_position[1]
                            hadaf_j = move_j + king_j
                            hadaf_i = move_i + king_i

                            if hadaf_j > 0 and hadaf_i > 0 and hadaf_j < 9 and hadaf_i < 9:
                                temp_piece = globals()[f"square_{hadaf_j}{hadaf_i}"].piece
                                if blocker[2] == hadaf_j and blocker[3] == hadaf_i and temp_piece[0] != "k" and \
                                        temp_piece[0] != "b" and temp_piece[0] != "h" and temp_piece[0] != "p" and \
                                        temp_piece[0] != "q" and temp_piece[0] != "r":
                                    piece_checked = 0
                                    for move2 in position_check_jmanfi_isabet:
                                        move2_j = move2[0]
                                        move2_i = move2[1]
                                        check_j = move2_j + hadaf_j
                                        check_i = move2_i + hadaf_i
                                        temp_piece2 = globals()[f"square_{check_j}{check_i}"].piece
                                        if temp_piece2[0] == "r" or temp_piece2[0] == "q":
                                            temp_list.append([hadaf_j, hadaf_i, False])
                                            piece_checked = 1
                                        elif temp_piece2[0] == "p" or temp_piece2[0] == "b" or [0] == "k" or \
                                                temp_piece2[
                                                    0] == "h":
                                            temp_list.append([hadaf_j, hadaf_i, True])
                                            piece_checked = 1
                                        elif temp_piece2[0] == "Q" or temp_piece2[0] == "P" or temp_piece2[0] == "R" or \
                                                temp_piece2[0] == "K" or temp_piece2[0] == "H" or temp_piece2[0] == "B":
                                            temp_list.append([hadaf_j, hadaf_i, True])
                                            piece_checked = 1
                                    if piece_checked == 0:
                                        temp_list.append([hadaf_j, hadaf_i, True])

                        position_check_jmanfi_imosbat = [[- 1, + 1], [- 2, + 2], [- 3, + 3], [- 4, + 4], [- 5, + 5],
                                                         [- 6, + 6], [- 7, + 7]]
                        for move in position_check_jmanfi_imosbat:
                            move_j = move[0]
                            move_i = move[1]
                            king_j = black_king_position[0]
                            king_i = black_king_position[1]
                            hadaf_j = move_j + king_j
                            hadaf_i = move_i + king_i

                            if hadaf_j > 0 and hadaf_i > 0 and hadaf_j < 9 and hadaf_i < 9:
                                temp_piece = globals()[f"square_{hadaf_j}{hadaf_i}"].piece
                                if blocker[2] == hadaf_j and blocker[3] == hadaf_i and temp_piece[0] != "k" and \
                                        temp_piece[0] != "b" and temp_piece[0] != "h" and temp_piece[0] != "p" and \
                                        temp_piece[0] != "q" and temp_piece[0] != "r":
                                    piece_checked = 0
                                    for move2 in position_check_jmanfi_imosbat:
                                        move2_j = move2[0]
                                        move2_i = move2[1]
                                        check_j = move2_j + hadaf_j
                                        check_i = move2_i + hadaf_i
                                        temp_piece2 = globals()[f"square_{check_j}{check_i}"].piece
                                        if temp_piece2[0] == "b" or temp_piece2[0] == "q":
                                            temp_list.append([hadaf_j, hadaf_i, False])
                                            piece_checked = 1
                                        elif temp_piece2[0] == "p" or temp_piece2[0] == "r" or [0] == "k" or \
                                                temp_piece2[
                                                    0] == "h":
                                            temp_list.append([hadaf_j, hadaf_i, True])
                                            piece_checked = 1
                                        elif temp_piece2[0] == "Q" or temp_piece2[0] == "P" or temp_piece2[0] == "R" or \
                                                temp_piece2[0] == "K" or temp_piece2[0] == "H" or temp_piece2[0] == "B":
                                            temp_list.append([hadaf_j, hadaf_i, True])
                                            piece_checked = 1
                                    if piece_checked == 0:
                                        temp_list.append([hadaf_j, hadaf_i, True])

                        position_check_jmosbat_imosbat = [[+ 1, + 1], [+ 2, + 2], [+ 3, + 3], [+ 4, + 4], [+ 5, + 5],
                                                          [+ 6, + 6], [+ 7, + 7]]
                        for move in position_check_jmosbat_imosbat:
                            move_j = move[0]
                            move_i = move[1]
                            king_j = black_king_position[0]
                            king_i = black_king_position[1]
                            hadaf_j = move_j + king_j
                            hadaf_i = move_i + king_i

                            if hadaf_j > 0 and hadaf_i > 0 and hadaf_j < 9 and hadaf_i < 9:
                                temp_piece = globals()[f"square_{hadaf_j}{hadaf_i}"].piece
                                if blocker[2] == hadaf_j and blocker[3] == hadaf_i and temp_piece[0] != "k" and \
                                        temp_piece[0] != "b" and temp_piece[0] != "h" and temp_piece[0] != "p" and \
                                        temp_piece[0] != "q" and temp_piece[0] != "r":
                                    piece_checked = 0
                                    for move2 in position_check_jmosbat_imosbat:
                                        move2_j = move2[0]
                                        move2_i = move2[1]
                                        check_j = move2_j + hadaf_j
                                        check_i = move2_i + hadaf_i
                                        temp_piece2 = globals()[f"square_{check_j}{check_i}"].piece
                                        if temp_piece2[0] == "b" or temp_piece2[0] == "q":
                                            temp_list.append([hadaf_j, hadaf_i, False])
                                            piece_checked = 1
                                        elif temp_piece2[0] == "p" or temp_piece2[0] == "r" or [0] == "k" or \
                                                temp_piece2[
                                                    0] == "h":
                                            temp_list.append([hadaf_j, hadaf_i, True])
                                            piece_checked = 1
                                        elif temp_piece2[0] == "Q" or temp_piece2[0] == "P" or temp_piece2[0] == "R" or \
                                                temp_piece2[0] == "K" or temp_piece2[0] == "H" or temp_piece2[0] == "B":
                                            temp_list.append([hadaf_j, hadaf_i, True])
                                            piece_checked = 1
                                    if piece_checked == 0:
                                        temp_list.append([hadaf_j, hadaf_i, True])

                        position_check_jmanfi_imanfi = [[- 1, - 1], [- 2, - 2], [- 3, - 3], [- 4, - 4], [- 5, - 5],
                                                        [- 6, - 6], [- 7, - 7]]
                        for move in position_check_jmanfi_imanfi:
                            move_j = move[0]
                            move_i = move[1]
                            king_j = black_king_position[0]
                            king_i = black_king_position[1]
                            hadaf_j = move_j + king_j
                            hadaf_i = move_i + king_i

                            if hadaf_j > 0 and hadaf_i > 0 and hadaf_j < 9 and hadaf_i < 9:
                                temp_piece = globals()[f"square_{hadaf_j}{hadaf_i}"].piece
                                if blocker[2] == hadaf_j and blocker[3] == hadaf_i and temp_piece[0] != "k" and \
                                        temp_piece[0] != "b" and temp_piece[0] != "h" and temp_piece[0] != "p" and \
                                        temp_piece[0] != "q" and temp_piece[0] != "r":
                                    piece_checked = 0
                                    for move2 in position_check_jmanfi_imanfi:
                                        move2_j = move2[0]
                                        move2_i = move2[1]
                                        check_j = move2_j + hadaf_j
                                        check_i = move2_i + hadaf_i
                                        temp_piece2 = globals()[f"square_{check_j}{check_i}"].piece
                                        if temp_piece2[0] == "b" or temp_piece2[0] == "q":
                                            temp_list.append([hadaf_j, hadaf_i, False])
                                            piece_checked = 1
                                        elif temp_piece2[0] == "p" or temp_piece2[0] == "r" or [0] == "k" or \
                                                temp_piece2[
                                                    0] == "h":
                                            temp_list.append([hadaf_j, hadaf_i, True])
                                            piece_checked = 1
                                        elif temp_piece2[0] == "Q" or temp_piece2[0] == "P" or temp_piece2[0] == "R" or \
                                                temp_piece2[0] == "K" or temp_piece2[0] == "H" or temp_piece2[0] == "B":
                                            temp_list.append([hadaf_j, hadaf_i, True])
                                            piece_checked = 1
                                    if piece_checked == 0:
                                        temp_list.append([hadaf_j, hadaf_i, True])

                        position_check_jmosbat_imanfi = [[+ 1, - 1], [+ 2, - 2], [+ 3, - 3], [+ 4, - 4], [+ 5, - 5],
                                                         [+ 6, - 6], [+ 7, - 7]]
                        for move in position_check_jmosbat_imanfi:
                            move_j = move[0]
                            move_i = move[1]
                            king_j = black_king_position[0]
                            king_i = black_king_position[1]
                            hadaf_j = move_j + king_j
                            hadaf_i = move_i + king_i

                            if hadaf_j > 0 and hadaf_i > 0 and hadaf_j < 9 and hadaf_i < 9:
                                temp_piece = globals()[f"square_{hadaf_j}{hadaf_i}"].piece
                                if blocker[2] == hadaf_j and blocker[3] == hadaf_i and temp_piece[0] != "k" and \
                                        temp_piece[0] != "b" and temp_piece[0] != "h" and temp_piece[0] != "p" and \
                                        temp_piece[0] != "q" and temp_piece[0] != "r":
                                    piece_checked = 0
                                    for move2 in position_check_jmosbat_imanfi:
                                        move2_j = move2[0]
                                        move2_i = move2[1]
                                        check_j = move2_j + hadaf_j
                                        check_i = move2_i + hadaf_i
                                        temp_piece2 = globals()[f"square_{check_j}{check_i}"].piece
                                        if temp_piece2[0] == "b" or temp_piece2[0] == "q":
                                            temp_list.append([hadaf_j, hadaf_i, False])
                                            piece_checked = 1
                                        elif temp_piece2[0] == "p" or temp_piece2[0] == "r" or [0] == "k" or \
                                                temp_piece2[
                                                    0] == "h":
                                            temp_list.append([hadaf_j, hadaf_i, True])
                                            piece_checked = 1
                                        elif temp_piece2[0] == "Q" or temp_piece2[0] == "P" or temp_piece2[0] == "R" or \
                                                temp_piece2[0] == "K" or temp_piece2[0] == "H" or temp_piece2[0] == "B":
                                            temp_list.append([hadaf_j, hadaf_i, True])
                                            piece_checked = 1
                                    if piece_checked == 0:
                                        temp_list.append([hadaf_j, hadaf_i, True])
                    except Exception as err:
                        print("problem in 1 ", err)

        #################################
        try:
            temp_block_list = block_list

            for checked in temp_list:
                for block in block_list:

                    try:
                        if checked[0] == block[2] and checked[1] == block[3] and checked[2] == True:
                            temp_block_list.remove(block)
                            black_friendly.append(checked)
                        elif checked[0] == block[2] and checked[1] == block[3] and checked[2] == False:
                            temp_block_list.remove(block)
                    except Exception as err:
                        print("error toye  remove temp block")

            # in paiinia baraye onaiie ke fagat unchek mikonan ba kingeshon kolan asib nemizanan
            for unchecker in temp_block_list:
                unchecker_j = unchecker[2]
                unchecker_i = unchecker[3]
                checker_j = unchecker[0]
                checker_i = unchecker[1]
                for kishkonande in black_king_kisher:
                    kishkonande_j = kishkonande[0]
                    kishkonande_i = kishkonande[1]
                    if kishkonande_j == checker_j and kishkonande_i == checker_i:
                        unchecker_name = globals()[f"square_{unchecker_j}{unchecker_i}"].piece
                        checker_name = globals()[f"square_{checker_j}{checker_i}"].piece
                        if unchecker_name[0] == "Q" or unchecker_name[0] == "P" or unchecker_name[0] == "R" or \
                                unchecker_name[0] == "H" or \
                                unchecker_name[0] == "B":
                            if checker_name[0] == "q" or checker_name[0] == "p" or checker_name[0] == "r" or \
                                    checker_name[0] == "h" or \
                                    checker_name[0] == "b":
                                black_friendly.append([unchecker_j, unchecker_i, True])


        except Exception as err:
            print("problem in 2 ", err)
            # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

    #### hala white #####

    temp_move_list_w = white_king_move_list
    temp_len_move_list_w = len(temp_move_list_w)
    temp_list = []
    if temp_len_move_list_w == 0:

        for kisher in white_king_kisher:
            kisher_j = kisher[0]
            kisher_i = kisher[1]
            for blocker in block_list:
                if blocker[0] == kisher_j and blocker[1] == kisher_i:

                    ####################

                    try:
                        position_check_jsabet_imosbat = [[+ 0, + 1], [+ 0, + 2], [+ 0, + 3], [+ 0, + 4], [+ 0, + 5],
                                                         [+ 0, + 6], [+ 0, + 7]]

                        for move in position_check_jsabet_imosbat:
                            move_j = move[0]
                            move_i = move[1]
                            king_j = white_king_position[0]
                            king_i = white_king_position[1]
                            hadaf_j = move_j + king_j
                            hadaf_i = move_i + king_i

                            if hadaf_j > 0 and hadaf_i > 0 and hadaf_j < 9 and hadaf_i < 9:
                                temp_piece = globals()[f"square_{hadaf_j}{hadaf_i}"].piece
                                if blocker[2] == hadaf_j and blocker[3] == hadaf_i and temp_piece[0] != "K" and \
                                        temp_piece[0] != "B" and temp_piece[0] != "H" and temp_piece[0] != "P" and \
                                        temp_piece[0] != "Q" and temp_piece[0] != "R":
                                    piece_checked = 0
                                    for move2 in position_check_jsabet_imosbat:
                                        move2_j = move2[0]
                                        move2_i = move2[1]
                                        check_j = move2_j + hadaf_j
                                        check_i = move2_i + hadaf_i
                                        temp_piece2 = globals()[f"square_{check_j}{check_i}"].piece
                                        if temp_piece2[0] == "R" or temp_piece2[0] == "Q":
                                            temp_list.append([hadaf_j, hadaf_i, False])
                                            piece_checked = 1
                                        elif temp_piece2[0] == "P" or temp_piece2[0] == "B" or [0] == "K" or \
                                                temp_piece2[0] == "H":
                                            temp_list.append([hadaf_j, hadaf_i, True])
                                            piece_checked = 1
                                        elif temp_piece2[0] == "q" or temp_piece2[0] == "p" or temp_piece2[
                                            0] == "r" or temp_piece2[0] == "k" or temp_piece2[0] == "h" or \
                                                temp_piece2[0] == "b":
                                            temp_list.append([hadaf_j, hadaf_i, True])
                                            piece_checked = 1
                                    if piece_checked == 0:
                                        temp_list.append([hadaf_j, hadaf_i, True])

                        position_check_jsabet_imanfi = [[+ 0, - 1], [+ 0, - 2], [+ 0, - 3], [+ 0, - 4], [+ 0, - 5],
                                                        [+ 0, - 6], [+ 0, - 7]]
                        for move in position_check_jsabet_imanfi:
                            move_j = move[0]
                            move_i = move[1]
                            king_j = white_king_position[0]
                            king_i = white_king_position[1]
                            hadaf_j = move_j + king_j
                            hadaf_i = move_i + king_i

                            if hadaf_j > 0 and hadaf_i > 0 and hadaf_j < 9 and hadaf_i < 9:
                                temp_piece = globals()[f"square_{hadaf_j}{hadaf_i}"].piece
                                if blocker[2] == hadaf_j and blocker[3] == hadaf_i and temp_piece[0] != "K" and \
                                        temp_piece[0] != "B" and temp_piece[0] != "H" and temp_piece[0] != "P" and \
                                        temp_piece[0] != "Q" and temp_piece[0] != "R":
                                    piece_checked = 0
                                    for move2 in position_check_jsabet_imanfi:
                                        move2_j = move2[0]
                                        move2_i = move2[1]
                                        check_j = move2_j + hadaf_j
                                        check_i = move2_i + hadaf_i
                                        temp_piece2 = globals()[f"square_{check_j}{check_i}"].piece
                                        if temp_piece2[0] == "R" or temp_piece2[0] == "Q":
                                            temp_list.append([hadaf_j, hadaf_i, False])
                                            piece_checked = 1
                                        elif temp_piece2[0] == "P" or temp_piece2[0] == "B" or [0] == "K" or \
                                                temp_piece2[
                                                    0] == "H":
                                            temp_list.append([hadaf_j, hadaf_i, True])
                                            piece_checked = 1
                                        elif temp_piece2[0] == "q" or temp_piece2[0] == "p" or temp_piece2[
                                            0] == "r" or \
                                                temp_piece2[0] == "k" or temp_piece2[0] == "h" or temp_piece2[
                                            0] == "b":
                                            temp_list.append([hadaf_j, hadaf_i, True])
                                            piece_checked = 1
                                    if piece_checked == 0:
                                        temp_list.append([hadaf_j, hadaf_i, True])

                        position_check_jmosbat_isabet = [[+ 1, 0], [+ 2, 0], [+ 3, 0], [+ 4, 0], [+ 5, 0], [+ 6, 0],
                                                         [+ 7, 0]]
                        for move in position_check_jmosbat_isabet:
                            move_j = move[0]
                            move_i = move[1]
                            king_j = white_king_position[0]
                            king_i = white_king_position[1]
                            hadaf_j = move_j + king_j
                            hadaf_i = move_i + king_i

                            if hadaf_j > 0 and hadaf_i > 0 and hadaf_j < 9 and hadaf_i < 9:
                                temp_piece = globals()[f"square_{hadaf_j}{hadaf_i}"].piece
                                if blocker[2] == hadaf_j and blocker[3] == hadaf_i and temp_piece[0] != "K" and \
                                        temp_piece[0] != "B" and temp_piece[0] != "H" and temp_piece[0] != "P" and \
                                        temp_piece[0] != "Q" and temp_piece[0] != "R":
                                    piece_checked = 0
                                    for move2 in position_check_jmosbat_isabet:
                                        move2_j = move2[0]
                                        move2_i = move2[1]
                                        check_j = move2_j + hadaf_j
                                        check_i = move2_i + hadaf_i
                                        temp_piece2 = globals()[f"square_{check_j}{check_i}"].piece
                                        if temp_piece2[0] == "R" or temp_piece2[0] == "Q":
                                            temp_list.append([hadaf_j, hadaf_i, False])
                                            piece_checked = 1
                                        elif temp_piece2[0] == "P" or temp_piece2[0] == "B" or [0] == "K" or \
                                                temp_piece2[
                                                    0] == "H":
                                            temp_list.append([hadaf_j, hadaf_i, True])
                                            piece_checked = 1
                                        elif temp_piece2[0] == "q" or temp_piece2[0] == "p" or temp_piece2[
                                            0] == "r" or \
                                                temp_piece2[0] == "k" or temp_piece2[0] == "h" or temp_piece2[
                                            0] == "b":
                                            temp_list.append([hadaf_j, hadaf_i, True])
                                            piece_checked = 1
                                    if piece_checked == 0:
                                        temp_list.append([hadaf_j, hadaf_i, True])

                        position_check_jmanfi_isabet = [[- 1, 0], [- 2, 0], [- 3, 0], [- 4, 0], [- 5, 0], [- 6, 0],
                                                        [- 7, 0]]
                        for move in position_check_jmanfi_isabet:
                            move_j = move[0]
                            move_i = move[1]
                            king_j = white_king_position[0]
                            king_i = white_king_position[1]
                            hadaf_j = move_j + king_j
                            hadaf_i = move_i + king_i

                            if hadaf_j > 0 and hadaf_i > 0 and hadaf_j < 9 and hadaf_i < 9:
                                temp_piece = globals()[f"square_{hadaf_j}{hadaf_i}"].piece
                                if blocker[2] == hadaf_j and blocker[3] == hadaf_i and temp_piece[0] != "K" and \
                                        temp_piece[0] != "B" and temp_piece[0] != "H" and temp_piece[0] != "P" and \
                                        temp_piece[0] != "Q" and temp_piece[0] != "R":
                                    piece_checked = 0
                                    for move2 in position_check_jmanfi_isabet:
                                        move2_j = move2[0]
                                        move2_i = move2[1]
                                        check_j = move2_j + hadaf_j
                                        check_i = move2_i + hadaf_i
                                        temp_piece2 = globals()[f"square_{check_j}{check_i}"].piece
                                        if temp_piece2[0] == "R" or temp_piece2[0] == "Q":
                                            temp_list.append([hadaf_j, hadaf_i, False])
                                            piece_checked = 1
                                        elif temp_piece2[0] == "P" or temp_piece2[0] == "B" or [0] == "K" or \
                                                temp_piece2[
                                                    0] == "H":
                                            temp_list.append([hadaf_j, hadaf_i, True])
                                            piece_checked = 1
                                        elif temp_piece2[0] == "q" or temp_piece2[0] == "p" or temp_piece2[
                                            0] == "r" or \
                                                temp_piece2[0] == "k" or temp_piece2[0] == "h" or temp_piece2[
                                            0] == "b":
                                            temp_list.append([hadaf_j, hadaf_i, True])
                                            piece_checked = 1
                                    if piece_checked == 0:
                                        temp_list.append([hadaf_j, hadaf_i, True])

                        position_check_jmanfi_imosbat = [[- 1, + 1], [- 2, + 2], [- 3, + 3], [- 4, + 4], [- 5, + 5],
                                                         [- 6, + 6], [- 7, + 7]]
                        for move in position_check_jmanfi_imosbat:
                            move_j = move[0]
                            move_i = move[1]
                            king_j = white_king_position[0]
                            king_i = white_king_position[1]
                            hadaf_j = move_j + king_j
                            hadaf_i = move_i + king_i

                            if hadaf_j > 0 and hadaf_i > 0 and hadaf_j < 9 and hadaf_i < 9:
                                temp_piece = globals()[f"square_{hadaf_j}{hadaf_i}"].piece
                                if blocker[2] == hadaf_j and blocker[3] == hadaf_i and temp_piece[0] != "K" and \
                                        temp_piece[0] != "B" and temp_piece[0] != "H" and temp_piece[0] != "P" and \
                                        temp_piece[0] != "Q" and temp_piece[0] != "R":
                                    piece_checked = 0
                                    for move2 in position_check_jmanfi_imosbat:
                                        move2_j = move2[0]
                                        move2_i = move2[1]
                                        check_j = move2_j + hadaf_j
                                        check_i = move2_i + hadaf_i
                                        temp_piece2 = globals()[f"square_{check_j}{check_i}"].piece
                                        if temp_piece2[0] == "B" or temp_piece2[0] == "Q":
                                            temp_list.append([hadaf_j, hadaf_i, False])
                                            piece_checked = 1
                                        elif temp_piece2[0] == "P" or temp_piece2[0] == "R" or [0] == "K" or \
                                                temp_piece2[
                                                    0] == "H":
                                            temp_list.append([hadaf_j, hadaf_i, True])
                                            piece_checked = 1
                                        elif temp_piece2[0] == "q" or temp_piece2[0] == "p" or temp_piece2[
                                            0] == "r" or \
                                                temp_piece2[0] == "k" or temp_piece2[0] == "h" or temp_piece2[
                                            0] == "b":
                                            temp_list.append([hadaf_j, hadaf_i, True])
                                            piece_checked = 1
                                    if piece_checked == 0:
                                        temp_list.append([hadaf_j, hadaf_i, True])

                        position_check_jmosbat_imosbat = [[+ 1, + 1], [+ 2, + 2], [+ 3, + 3], [+ 4, + 4],
                                                          [+ 5, + 5], [+ 6, + 6], [+ 7, + 7]]
                        for move in position_check_jmosbat_imosbat:
                            move_j = move[0]
                            move_i = move[1]
                            king_j = white_king_position[0]
                            king_i = white_king_position[1]
                            hadaf_j = move_j + king_j
                            hadaf_i = move_i + king_i

                            if hadaf_j > 0 and hadaf_i > 0 and hadaf_j < 9 and hadaf_i < 9:
                                temp_piece = globals()[f"square_{hadaf_j}{hadaf_i}"].piece
                                if blocker[2] == hadaf_j and blocker[3] == hadaf_i and temp_piece[0] != "K" and \
                                        temp_piece[0] != "B" and temp_piece[0] != "H" and temp_piece[0] != "P" and \
                                        temp_piece[0] != "Q" and temp_piece[0] != "R":
                                    piece_checked = 0
                                    for move2 in position_check_jmosbat_imosbat:
                                        move2_j = move2[0]
                                        move2_i = move2[1]
                                        check_j = move2_j + hadaf_j
                                        check_i = move2_i + hadaf_i
                                        temp_piece2 = globals()[f"square_{check_j}{check_i}"].piece
                                        if temp_piece2[0] == "B" or temp_piece2[0] == "Q":
                                            temp_list.append([hadaf_j, hadaf_i, False])
                                            piece_checked = 1
                                        elif temp_piece2[0] == "P" or temp_piece2[0] == "R" or [0] == "K" or \
                                                temp_piece2[
                                                    0] == "H":
                                            temp_list.append([hadaf_j, hadaf_i, True])
                                            piece_checked = 1
                                        elif temp_piece2[0] == "q" or temp_piece2[0] == "p" or temp_piece2[
                                            0] == "r" or \
                                                temp_piece2[0] == "k" or temp_piece2[0] == "h" or temp_piece2[
                                            0] == "b":
                                            temp_list.append([hadaf_j, hadaf_i, True])
                                            piece_checked = 1
                                    if piece_checked == 0:
                                        temp_list.append([hadaf_j, hadaf_i, True])

                        position_check_jmanfi_imanfi = [[- 1, - 1], [- 2, - 2], [- 3, - 3], [- 4, - 4], [- 5, - 5],
                                                        [- 6, - 6], [- 7, - 7]]
                        for move in position_check_jmanfi_imanfi:
                            move_j = move[0]
                            move_i = move[1]
                            king_j = white_king_position[0]
                            king_i = white_king_position[1]
                            hadaf_j = move_j + king_j
                            hadaf_i = move_i + king_i

                            if hadaf_j > 0 and hadaf_i > 0 and hadaf_j < 9 and hadaf_i < 9:
                                temp_piece = globals()[f"square_{hadaf_j}{hadaf_i}"].piece
                                if blocker[2] == hadaf_j and blocker[3] == hadaf_i and temp_piece[0] != "K" and \
                                        temp_piece[0] != "B" and temp_piece[0] != "H" and temp_piece[0] != "P" and \
                                        temp_piece[0] != "Q" and temp_piece[0] != "R":
                                    piece_checked = 0
                                    for move2 in position_check_jmanfi_imanfi:
                                        move2_j = move2[0]
                                        move2_i = move2[1]
                                        check_j = move2_j + hadaf_j
                                        check_i = move2_i + hadaf_i
                                        temp_piece2 = globals()[f"square_{check_j}{check_i}"].piece
                                        if temp_piece2[0] == "B" or temp_piece2[0] == "Q":
                                            temp_list.append([hadaf_j, hadaf_i, False])
                                            piece_checked = 1
                                        elif temp_piece2[0] == "P" or temp_piece2[0] == "R" or [0] == "K" or \
                                                temp_piece2[
                                                    0] == "H":
                                            temp_list.append([hadaf_j, hadaf_i, True])
                                            piece_checked = 1
                                        elif temp_piece2[0] == "q" or temp_piece2[0] == "p" or temp_piece2[
                                            0] == "r" or \
                                                temp_piece2[0] == "k" or temp_piece2[0] == "h" or temp_piece2[
                                            0] == "b":
                                            temp_list.append([hadaf_j, hadaf_i, True])
                                            piece_checked = 1
                                    if piece_checked == 0:
                                        temp_list.append([hadaf_j, hadaf_i, True])

                        position_check_jmosbat_imanfi = [[+ 1, - 1], [+ 2, - 2], [+ 3, - 3], [+ 4, - 4], [+ 5, - 5],
                                                         [+ 6, - 6], [+ 7, - 7]]
                        for move in position_check_jmosbat_imanfi:
                            move_j = move[0]
                            move_i = move[1]
                            king_j = white_king_position[0]
                            king_i = white_king_position[1]
                            hadaf_j = move_j + king_j
                            hadaf_i = move_i + king_i

                            if hadaf_j > 0 and hadaf_i > 0 and hadaf_j < 9 and hadaf_i < 9:
                                temp_piece = globals()[f"square_{hadaf_j}{hadaf_i}"].piece
                                if blocker[2] == hadaf_j and blocker[3] == hadaf_i and temp_piece[0] != "K" and \
                                        temp_piece[0] != "B" and temp_piece[0] != "H" and temp_piece[0] != "P" and \
                                        temp_piece[0] != "Q" and temp_piece[0] != "R":
                                    piece_checked = 0
                                    for move2 in position_check_jmosbat_imanfi:
                                        move2_j = move2[0]
                                        move2_i = move2[1]
                                        check_j = move2_j + hadaf_j
                                        check_i = move2_i + hadaf_i
                                        temp_piece2 = globals()[f"square_{check_j}{check_i}"].piece
                                        if temp_piece2[0] == "B" or temp_piece2[0] == "Q":
                                            temp_list.append([hadaf_j, hadaf_i, False])
                                            piece_checked = 1
                                        elif temp_piece2[0] == "P" or temp_piece2[0] == "R" or [0] == "K" or \
                                                temp_piece2[
                                                    0] == "H":
                                            temp_list.append([hadaf_j, hadaf_i, True])
                                            piece_checked = 1
                                        elif temp_piece2[0] == "q" or temp_piece2[0] == "p" or temp_piece2[
                                            0] == "r" or \
                                                temp_piece2[0] == "k" or temp_piece2[0] == "h" or temp_piece2[
                                            0] == "b":
                                            temp_list.append([hadaf_j, hadaf_i, True])
                                            piece_checked = 1
                                    if piece_checked == 0:
                                        temp_list.append([hadaf_j, hadaf_i, True])
                    except Exception as err:
                        print("problem in 1 ", err)

        #################################
        try:
            temp_block_list = block_list

            for checked in temp_list:
                for block in temp_block_list:
                    try:
                        if checked[0] == block[2] and checked[1] == block[3] and checked[2] == True:
                            temp_block_list.remove(block)
                            white_friendly.append(checked)
                        elif checked[0] == block[2] and checked[1] == block[3] and checked[2] == False:
                            temp_block_list.remove(block)
                    except Exception as err:
                        print("toye  white err darim", err)
            # in paiinia baraye onaiie ke fagat unchek mikonan ba kingeshon kolan asib nemizanan
            for unchecker in temp_block_list:
                unchecker_j = unchecker[2]
                unchecker_i = unchecker[3]
                checker_j = unchecker[0]
                checker_i = unchecker[1]
                for kishkonande in white_king_kisher:
                    kishkonande_j = kishkonande[0]
                    kishkonande_i = kishkonande[1]
                    if kishkonande_j == checker_j and kishkonande_i == checker_i:
                        unchecker_name = globals()[f"square_{unchecker_j}{unchecker_i}"].piece
                        checker_name = globals()[f"square_{checker_j}{checker_i}"].piece
                        if unchecker_name[0] == "q" or unchecker_name[0] == "p" or unchecker_name[0] == "r" or \
                                unchecker_name[0] == "h" or \
                                unchecker_name[0] == "b":
                            if checker_name[0] == "Q" or checker_name[0] == "P" or checker_name[0] == "R" or \
                                    checker_name[
                                        0] == "H" or \
                                    checker_name[0] == "B":
                                white_friendly.append([unchecker_j, unchecker_i, True])
        except Exception as err:
            print("problem in 2 ", err)


black_friendly_list = []
last_black_friendly_can_move = []
white_friendly_list = []
last_white_friendly_can_move = []


def uncheck_by_piece_move():  # >>>>>>>>>>>>>>>> b&w
    # har mohre shatranj
    black_picemove_to_uncheck = []
    for sq in square_list:
        black_picemove_to_uncheck = []
        temp_main_piece = globals()[f"{sq}"].piece
        main_j = globals()[f"{sq}"].satr
        main_i = globals()[f"{sq}"].soton
        # ke dar team siah bod (- kodeh black king)
        if temp_main_piece[0] == "H" or temp_main_piece[0] == "P" or temp_main_piece[0] == "Q" or temp_main_piece[
            0] == "R" or temp_main_piece[0] == "B":
            main_asar_koli = globals()[f"{sq}"].asarha  # asarasho begir
            if temp_main_piece[0] == "P":
                main_asar_koli = [[main_j + 1, main_i]]
            for main_asar in main_asar_koli:
                main_asar_j = main_asar[0]
                main_asar_i = main_asar[1]
                for kisher in black_king_kisher:  # j i ksi ke kish karde
                    kisher_j = kisher[0]
                    kisher_i = kisher[1]
                    kisher_asar_koli = globals()[
                        f"square_{kisher_j}{kisher_i}"].asarha  # gereftan asarha ksi ke kish karde
                    for kisher_asar in kisher_asar_koli:  # j i har asar ha ksi ke kish karde

                        kisher_asar_j = kisher_asar[0]
                        kisher_asar_i = kisher_asar[1]
                        if main_asar_j == kisher_asar_j and main_asar_i == kisher_asar_i:  # age ba asarha piece frendly ma yeki bod
                            black_picemove_to_uncheck.append(
                                [temp_main_piece, main_asar_j, main_asar_i, main_j, main_i])  # to ye list mizarimesh

            ############ az inja hame onaii ke tasir mizaran ro kingeshon peyd amishan #################
            try:
                position_check_jsabet_imosbat = [[+ 0, + 1], [+ 0, + 2], [+ 0, + 3], [+ 0, + 4], [+ 0, + 5],
                                                 [+ 0, + 6], [+ 0, + 7]]

                for move in position_check_jsabet_imosbat:
                    move_j = move[0]
                    move_i = move[1]
                    king_j = black_king_position[0]
                    king_i = black_king_position[1]
                    hadaf_j = move_j + king_j
                    hadaf_i = move_i + king_i

                    if hadaf_j > 0 and hadaf_i > 0 and hadaf_j < 9 and hadaf_i < 9:
                        temp_piece = globals()[f"square_{hadaf_j}{hadaf_i}"].piece
                        if temp_piece[0] == "B" or temp_piece[0] == "H" or temp_piece[0] == "P" or temp_piece[
                            0] == "Q" or temp_piece[0] == "R":
                            piece_checked = 0
                            for move2 in position_check_jsabet_imosbat:
                                move2_j = move2[0]
                                move2_i = move2[1]
                                check_j = move2_j + hadaf_j
                                check_i = move2_i + hadaf_i
                                temp_piece2 = globals()[f"square_{check_j}{check_i}"].piece
                                if temp_piece2[0] == "r" or temp_piece2[0] == "q":
                                    black_friendly_list.append([hadaf_j, hadaf_i, False])
                                    piece_checked = 1
                                elif temp_piece2[0] == "p" or temp_piece2[0] == "b" or temp_piece2[0] == "k" or \
                                        temp_piece2[
                                            0] == "h":
                                    black_friendly_list.append([hadaf_j, hadaf_i, True])
                                    piece_checked = 1
                                elif temp_piece2[0] == "Q" or temp_piece2[0] == "P" or temp_piece2[0] == "R" or \
                                        temp_piece2[0] == "K" or temp_piece2[0] == "H" or temp_piece2[0] == "B":
                                    black_friendly_list.append([hadaf_j, hadaf_i, True])
                                    piece_checked = 1
                            if piece_checked == 0:
                                black_friendly_list.append([hadaf_j, hadaf_i, True])
                                #############1#############

                position_check_jsabet_imanfi = [[+ 0, - 1], [+ 0, - 2], [+ 0, - 3], [+ 0, - 4], [+ 0, - 5],
                                                [+ 0, - 6], [+ 0, - 7]]
                for move in position_check_jsabet_imanfi:
                    move_j = move[0]
                    move_i = move[1]
                    king_j = black_king_position[0]
                    king_i = black_king_position[1]
                    hadaf_j = move_j + king_j
                    hadaf_i = move_i + king_i

                    if hadaf_j > 0 and hadaf_i > 0 and hadaf_j < 9 and hadaf_i < 9:
                        temp_piece = globals()[f"square_{hadaf_j}{hadaf_i}"].piece
                        if temp_piece[0] == "B" or temp_piece[0] == "H" or temp_piece[0] == "P" or temp_piece[
                            0] == "Q" or temp_piece[0] == "R":
                            piece_checked = 0
                            for move2 in position_check_jsabet_imanfi:
                                move2_j = move2[0]
                                move2_i = move2[1]
                                check_j = move2_j + hadaf_j
                                check_i = move2_i + hadaf_i
                                temp_piece2 = globals()[f"square_{check_j}{check_i}"].piece
                                if temp_piece2[0] == "r" or temp_piece2[0] == "q":
                                    black_friendly_list.append([hadaf_j, hadaf_i, False])
                                    piece_checked = 1
                                elif temp_piece2[0] == "p" or temp_piece2[0] == "b" or temp_piece2[0] == "k" or \
                                        temp_piece2[
                                            0] == "h":
                                    black_friendly_list.append([hadaf_j, hadaf_i, True])
                                    piece_checked = 1
                                elif temp_piece2[0] == "Q" or temp_piece2[0] == "P" or temp_piece2[0] == "R" or \
                                        temp_piece2[0] == "K" or temp_piece2[0] == "H" or temp_piece2[0] == "B":
                                    black_friendly_list.append([hadaf_j, hadaf_i, True])
                                    piece_checked = 1
                            if piece_checked == 0:
                                black_friendly_list.append([hadaf_j, hadaf_i, True])
                            ##################2###############
                position_check_jmosbat_isabet = [[+ 1, 0], [+ 2, 0], [+ 3, 0], [+ 4, 0], [+ 5, 0], [+ 6, 0],
                                                 [+ 7, 0]]
                for move in position_check_jmosbat_isabet:
                    move_j = move[0]
                    move_i = move[1]
                    king_j = black_king_position[0]
                    king_i = black_king_position[1]
                    hadaf_j = move_j + king_j
                    hadaf_i = move_i + king_i

                    if hadaf_j > 0 and hadaf_i > 0 and hadaf_j < 9 and hadaf_i < 9:
                        temp_piece = globals()[f"square_{hadaf_j}{hadaf_i}"].piece
                        if temp_piece[0] == "B" or temp_piece[0] == "H" or temp_piece[0] == "P" or temp_piece[
                            0] == "Q" or temp_piece[0] == "R":
                            piece_checked = 0
                            for move2 in position_check_jmosbat_isabet:
                                move2_j = move2[0]
                                move2_i = move2[1]
                                check_j = move2_j + hadaf_j
                                check_i = move2_i + hadaf_i
                                temp_piece2 = globals()[f"square_{check_j}{check_i}"].piece
                                if temp_piece2[0] == "r" or temp_piece2[0] == "q":
                                    black_friendly_list.append([hadaf_j, hadaf_i, False])
                                    piece_checked = 1
                                elif temp_piece2[0] == "p" or temp_piece2[0] == "b" or temp_piece2[0] == "k" or \
                                        temp_piece2[
                                            0] == "h":
                                    black_friendly_list.append([hadaf_j, hadaf_i, True])
                                    piece_checked = 1
                                elif temp_piece2[0] == "Q" or temp_piece2[0] == "P" or temp_piece2[0] == "R" or \
                                        temp_piece2[0] == "K" or temp_piece2[0] == "H" or temp_piece2[0] == "B":
                                    black_friendly_list.append([hadaf_j, hadaf_i, True])
                                    piece_checked = 1
                            if piece_checked == 0:
                                black_friendly_list.append([hadaf_j, hadaf_i, True])
                    ####################3###################
                position_check_jmanfi_isabet = [[- 1, 0], [- 2, 0], [- 3, 0], [- 4, 0], [- 5, 0], [- 6, 0],
                                                [- 7, 0]]
                for move in position_check_jmanfi_isabet:
                    move_j = move[0]
                    move_i = move[1]
                    king_j = black_king_position[0]
                    king_i = black_king_position[1]
                    hadaf_j = move_j + king_j
                    hadaf_i = move_i + king_i

                    if hadaf_j > 0 and hadaf_i > 0 and hadaf_j < 9 and hadaf_i < 9:
                        temp_piece = globals()[f"square_{hadaf_j}{hadaf_i}"].piece
                        if temp_piece[0] == "B" or temp_piece[0] == "H" or temp_piece[0] == "P" or temp_piece[
                            0] == "Q" or temp_piece[0] == "R":
                            piece_checked = 0
                            for move2 in position_check_jmanfi_isabet:
                                move2_j = move2[0]
                                move2_i = move2[1]
                                check_j = move2_j + hadaf_j
                                check_i = move2_i + hadaf_i
                                temp_piece2 = globals()[f"square_{check_j}{check_i}"].piece
                                if temp_piece2[0] == "r" or temp_piece2[0] == "q":
                                    black_friendly_list.append([hadaf_j, hadaf_i, False])
                                    piece_checked = 1
                                elif temp_piece2[0] == "p" or temp_piece2[0] == "b" or temp_piece2[0] == "k" or \
                                        temp_piece2[
                                            0] == "h":
                                    black_friendly_list.append([hadaf_j, hadaf_i, True])
                                    piece_checked = 1
                                elif temp_piece2[0] == "Q" or temp_piece2[0] == "P" or temp_piece2[0] == "R" or \
                                        temp_piece2[0] == "K" or temp_piece2[0] == "H" or temp_piece2[0] == "B":
                                    black_friendly_list.append([hadaf_j, hadaf_i, True])
                                    piece_checked = 1
                            if piece_checked == 0:
                                black_friendly_list.append([hadaf_j, hadaf_i, True])
                        ####################4###################
                position_check_jmanfi_imosbat = [[- 1, + 1], [- 2, + 2], [- 3, + 3], [- 4, + 4], [- 5, + 5],
                                                 [- 6, + 6], [- 7, + 7]]
                for move in position_check_jmanfi_imosbat:
                    move_j = move[0]
                    move_i = move[1]
                    king_j = black_king_position[0]
                    king_i = black_king_position[1]
                    hadaf_j = move_j + king_j
                    hadaf_i = move_i + king_i

                    if hadaf_j > 0 and hadaf_i > 0 and hadaf_j < 9 and hadaf_i < 9:
                        temp_piece = globals()[f"square_{hadaf_j}{hadaf_i}"].piece
                        if temp_piece[0] == "B" or temp_piece[0] == "H" or temp_piece[0] == "P" or temp_piece[
                            0] == "Q" or temp_piece[0] == "R":
                            piece_checked = 0
                            for move2 in position_check_jmanfi_imosbat:
                                move2_j = move2[0]
                                move2_i = move2[1]
                                check_j = move2_j + hadaf_j
                                check_i = move2_i + hadaf_i
                                temp_piece2 = globals()[f"square_{check_j}{check_i}"].piece
                                if temp_piece2[0] == "b" or temp_piece2[0] == "q":
                                    black_friendly_list.append([hadaf_j, hadaf_i, False])
                                    piece_checked = 1
                                elif temp_piece2[0] == "p" or temp_piece2[0] == "r" or temp_piece2[0] == "k" or \
                                        temp_piece2[
                                            0] == "h":
                                    black_friendly_list.append([hadaf_j, hadaf_i, True])
                                    piece_checked = 1
                                elif temp_piece2[0] == "Q" or temp_piece2[0] == "P" or temp_piece2[0] == "R" or \
                                        temp_piece2[0] == "K" or temp_piece2[0] == "H" or temp_piece2[0] == "B":
                                    black_friendly_list.append([hadaf_j, hadaf_i, True])
                                    piece_checked = 1
                            if piece_checked == 0:
                                black_friendly_list.append([hadaf_j, hadaf_i, True])
                        #################5###################
                position_check_jmosbat_imosbat = [[+ 1, + 1], [+ 2, + 2], [+ 3, + 3], [+ 4, + 4], [+ 5, + 5],
                                                  [+ 6, + 6], [+ 7, + 7]]
                for move in position_check_jmosbat_imosbat:
                    move_j = move[0]
                    move_i = move[1]
                    king_j = black_king_position[0]
                    king_i = black_king_position[1]
                    hadaf_j = move_j + king_j
                    hadaf_i = move_i + king_i

                    if hadaf_j > 0 and hadaf_i > 0 and hadaf_j < 9 and hadaf_i < 9:
                        temp_piece = globals()[f"square_{hadaf_j}{hadaf_i}"].piece
                        if temp_piece[0] == "B" or temp_piece[0] == "H" or temp_piece[0] == "P" or temp_piece[
                            0] == "Q" or temp_piece[0] == "R":
                            piece_checked = 0
                            for move2 in position_check_jmosbat_imosbat:
                                move2_j = move2[0]
                                move2_i = move2[1]
                                check_j = move2_j + hadaf_j
                                check_i = move2_i + hadaf_i
                                temp_piece2 = globals()[f"square_{check_j}{check_i}"].piece
                                if temp_piece2[0] == "b" or temp_piece2[0] == "q":
                                    black_friendly_list.append([hadaf_j, hadaf_i, False])
                                    piece_checked = 1
                                elif temp_piece2[0] == "p" or temp_piece2[0] == "r" or temp_piece2[0] == "k" or \
                                        temp_piece2[
                                            0] == "h":
                                    black_friendly_list.append([hadaf_j, hadaf_i, True])
                                    piece_checked = 1
                                elif temp_piece2[0] == "Q" or temp_piece2[0] == "P" or temp_piece2[0] == "R" or \
                                        temp_piece2[0] == "K" or temp_piece2[0] == "H" or temp_piece2[0] == "B":
                                    black_friendly_list.append([hadaf_j, hadaf_i, True])
                                    piece_checked = 1
                            if piece_checked == 0:
                                black_friendly_list.append([hadaf_j, hadaf_i, True])
                            #############6###################
                position_check_jmanfi_imanfi = [[- 1, - 1], [- 2, - 2], [- 3, - 3], [- 4, - 4], [- 5, - 5],
                                                [- 6, - 6], [- 7, - 7]]
                for move in position_check_jmanfi_imanfi:
                    move_j = move[0]
                    move_i = move[1]
                    king_j = black_king_position[0]
                    king_i = black_king_position[1]
                    hadaf_j = move_j + king_j
                    hadaf_i = move_i + king_i

                    if hadaf_j > 0 and hadaf_i > 0 and hadaf_j < 9 and hadaf_i < 9:
                        temp_piece = globals()[f"square_{hadaf_j}{hadaf_i}"].piece
                        if temp_piece[0] == "B" or temp_piece[0] == "H" or temp_piece[0] == "P" or temp_piece[
                            0] == "Q" or temp_piece[0] == "R":
                            piece_checked = 0
                            for move2 in position_check_jmanfi_imanfi:
                                move2_j = move2[0]
                                move2_i = move2[1]
                                check_j = move2_j + hadaf_j
                                check_i = move2_i + hadaf_i
                                temp_piece2 = globals()[f"square_{check_j}{check_i}"].piece
                                if temp_piece2[0] == "b" or temp_piece2[0] == "q":
                                    black_friendly_list.append([hadaf_j, hadaf_i, False])
                                    piece_checked = 1
                                elif temp_piece2[0] == "p" or temp_piece2[0] == "r" or temp_piece2[0] == "k" or \
                                        temp_piece2[
                                            0] == "h":
                                    black_friendly_list.append([hadaf_j, hadaf_i, True])
                                    piece_checked = 1
                                elif temp_piece2[0] == "Q" or temp_piece2[0] == "P" or temp_piece2[0] == "R" or \
                                        temp_piece2[0] == "K" or temp_piece2[0] == "H" or temp_piece2[0] == "B":
                                    black_friendly_list.append([hadaf_j, hadaf_i, True])
                                    piece_checked = 1
                            if piece_checked == 0:
                                black_friendly_list.append([hadaf_j, hadaf_i, True])
                                #####################7########################
                position_check_jmosbat_imanfi = [[+ 1, - 1], [+ 2, - 2], [+ 3, - 3], [+ 4, - 4], [+ 5, - 5],
                                                 [+ 6, - 6], [+ 7, - 7]]
                for move in position_check_jmosbat_imanfi:
                    move_j = move[0]
                    move_i = move[1]
                    king_j = black_king_position[0]
                    king_i = black_king_position[1]
                    hadaf_j = move_j + king_j
                    hadaf_i = move_i + king_i

                    if hadaf_j > 0 and hadaf_i > 0 and hadaf_j < 9 and hadaf_i < 9:
                        temp_piece = globals()[f"square_{hadaf_j}{hadaf_i}"].piece
                        if temp_piece[0] == "B" or temp_piece[0] == "H" or temp_piece[0] == "P" or temp_piece[
                            0] == "Q" or temp_piece[0] == "R":
                            piece_checked = 0
                            for move2 in position_check_jmosbat_imanfi:
                                move2_j = move2[0]
                                move2_i = move2[1]
                                check_j = move2_j + hadaf_j
                                check_i = move2_i + hadaf_i
                                temp_piece2 = globals()[f"square_{check_j}{check_i}"].piece
                                if temp_piece2[0] == "b" or temp_piece2[0] == "q":
                                    black_friendly_list.append([hadaf_j, hadaf_i, False])
                                    piece_checked = 1
                                elif temp_piece2[0] == "p" or temp_piece2[0] == "r" or temp_piece2[0] == "k" or \
                                        temp_piece2[
                                            0] == "h":
                                    black_friendly_list.append([hadaf_j, hadaf_i, True])
                                    piece_checked = 1
                                elif temp_piece2[0] == "Q" or temp_piece2[0] == "P" or temp_piece2[0] == "R" or \
                                        temp_piece2[0] == "K" or temp_piece2[0] == "H" or temp_piece2[0] == "B":
                                    black_friendly_list.append([hadaf_j, hadaf_i, True])
                                    piece_checked = 1
                            if piece_checked == 0:
                                black_friendly_list.append([hadaf_j, hadaf_i, True])
                                #######################8################


            except Exception as err:
                print("problem in 1 ", err)
        #################################
        temp_piecemove_to_uncheck = []
        for item in black_picemove_to_uncheck:
            temp_piecemove_to_uncheck.append(item)
        for checked in black_friendly_list:
            checked_j = checked[0]
            checked_i = checked[1]
            for friend in black_picemove_to_uncheck:
                # j va i inja injorie
                friend_j = friend[3]
                friend_i = friend[4]
                try:
                    if checked_j == friend_j and checked_i == friend_i and checked[2] == True:
                        last_black_friendly_can_move.append([friend_j, friend_i, friend[0]])
                        temp_piecemove_to_uncheck.remove(
                            friend)  # onaii ke injri check shodan yani mitonan ro kingeshon tasir bezaran pak shodan
                    elif checked_j == friend_j and checked_i == friend_i and checked[2] == False:
                        temp_piecemove_to_uncheck.remove(friend)
                except Exception as err:
                    print("error toye  remove")

        black_picemove_to_uncheck = []
        for item2 in temp_piecemove_to_uncheck:
            black_picemove_to_uncheck.append(item2)
        # in paiinia baraye onaiie ke fagat unchek mikonan ba kingeshon kolan asib nemizanan
        for checkedd in black_picemove_to_uncheck:
            last_black_friendly_can_move.append([checkedd[1], checkedd[2], checkedd[0]])

    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

    # hala white ha ############################################################
    white_picemove_to_uncheck = []
    for sq in square_list:
        white_picemove_to_uncheck = []
        temp_main_piece = globals()[f"{sq}"].piece
        main_j = globals()[f"{sq}"].satr
        main_i = globals()[f"{sq}"].soton
        # ke dar team siah bod (- kodeh black king)
        if temp_main_piece[0] == "h" or temp_main_piece[0] == "p" or temp_main_piece[0] == "q" or temp_main_piece[
            0] == "r" or temp_main_piece[0] == "b":
            main_asar_koli = globals()[f"{sq}"].asarha  # asarasho begir
            if temp_main_piece[0] == "p":
                main_asar_koli = [[main_j - 1, main_i]]
            for main_asar in main_asar_koli:
                main_asar_j = main_asar[0]
                main_asar_i = main_asar[1]
                for kisher in white_king_kisher:  # j i ksi ke kish karde
                    kisher_j = kisher[0]
                    kisher_i = kisher[1]
                    kisher_asar_koli = globals()[
                        f"square_{kisher_j}{kisher_i}"].asarha  # gereftan asarha ksi ke kish karde
                    for kisher_asar in kisher_asar_koli:  # j i har asar ha ksi ke kish karde

                        kisher_asar_j = kisher_asar[0]
                        kisher_asar_i = kisher_asar[1]
                        if main_asar_j == kisher_asar_j and main_asar_i == kisher_asar_i:  # age ba asarha piece frendly ma yeki bod
                            white_picemove_to_uncheck.append(
                                [temp_main_piece, main_asar_j, main_asar_i, main_j, main_i])  # to ye list mizarimesh

            ############ az inja hame onaii ke tasir mizaran ro kingeshon peyd amishan #################
            try:
                position_check_jsabet_imosbat = [[+ 0, + 1], [+ 0, + 2], [+ 0, + 3], [+ 0, + 4], [+ 0, + 5],
                                                 [+ 0, + 6], [+ 0, + 7]]

                for move in position_check_jsabet_imosbat:
                    move_j = move[0]
                    move_i = move[1]
                    king_j = white_king_position[0]
                    king_i = white_king_position[1]
                    hadaf_j = move_j + king_j
                    hadaf_i = move_i + king_i

                    if hadaf_j > 0 and hadaf_i > 0 and hadaf_j < 9 and hadaf_i < 9:
                        temp_piece = globals()[f"square_{hadaf_j}{hadaf_i}"].piece
                        if temp_piece[0] == "b" or temp_piece[0] == "h" or temp_piece[0] == "p" or temp_piece[
                            0] == "q" or temp_piece[0] == "r":
                            piece_checked = 0
                            for move2 in position_check_jsabet_imosbat:
                                move2_j = move2[0]
                                move2_i = move2[1]
                                check_j = move2_j + hadaf_j
                                check_i = move2_i + hadaf_i
                                temp_piece2 = globals()[f"square_{check_j}{check_i}"].piece
                                if temp_piece2[0] == "R" or temp_piece2[0] == "Q":
                                    white_friendly_list.append([hadaf_j, hadaf_i, False])
                                    piece_checked = 1
                                elif temp_piece2[0] == "P" or temp_piece2[0] == "B" or temp_piece2[0] == "K" or \
                                        temp_piece2[
                                            0] == "H":
                                    white_friendly_list.append([hadaf_j, hadaf_i, True])
                                    piece_checked = 1
                                elif temp_piece2[0] == "q" or temp_piece2[0] == "p" or temp_piece2[0] == "r" or \
                                        temp_piece2[0] == "k" or temp_piece2[0] == "h" or temp_piece2[0] == "b":
                                    white_friendly_list.append([hadaf_j, hadaf_i, True])
                                    piece_checked = 1
                            if piece_checked == 0:
                                white_friendly_list.append([hadaf_j, hadaf_i, True])
                                #############1#############

                position_check_jsabet_imanfi = [[+ 0, - 1], [+ 0, - 2], [+ 0, - 3], [+ 0, - 4], [+ 0, - 5],
                                                [+ 0, - 6], [+ 0, - 7]]
                for move in position_check_jsabet_imanfi:
                    move_j = move[0]
                    move_i = move[1]
                    king_j = white_king_position[0]
                    king_i = white_king_position[1]
                    hadaf_j = move_j + king_j
                    hadaf_i = move_i + king_i

                    if hadaf_j > 0 and hadaf_i > 0 and hadaf_j < 9 and hadaf_i < 9:
                        temp_piece = globals()[f"square_{hadaf_j}{hadaf_i}"].piece
                        if temp_piece[0] == "b" or temp_piece[0] == "h" or temp_piece[0] == "p" or temp_piece[
                            0] == "q" or temp_piece[0] == "r":
                            piece_checked = 0
                            for move2 in position_check_jsabet_imanfi:
                                move2_j = move2[0]
                                move2_i = move2[1]
                                check_j = move2_j + hadaf_j
                                check_i = move2_i + hadaf_i
                                temp_piece2 = globals()[f"square_{check_j}{check_i}"].piece
                                if temp_piece2[0] == "R" or temp_piece2[0] == "Q":
                                    white_friendly_list.append([hadaf_j, hadaf_i, False])
                                    piece_checked = 1
                                elif temp_piece2[0] == "P" or temp_piece2[0] == "B" or temp_piece2[0] == "K" or \
                                        temp_piece2[
                                            0] == "H":
                                    white_friendly_list.append([hadaf_j, hadaf_i, True])
                                    piece_checked = 1
                                elif temp_piece2[0] == "q" or temp_piece2[0] == "p" or temp_piece2[0] == "r" or \
                                        temp_piece2[0] == "k" or temp_piece2[0] == "h" or temp_piece2[0] == "b":
                                    white_friendly_list.append([hadaf_j, hadaf_i, True])
                                    piece_checked = 1
                            if piece_checked == 0:
                                white_friendly_list.append([hadaf_j, hadaf_i, True])
                            ##################2###############
                position_check_jmosbat_isabet = [[+ 1, 0], [+ 2, 0], [+ 3, 0], [+ 4, 0], [+ 5, 0], [+ 6, 0],
                                                 [+ 7, 0]]
                for move in position_check_jmosbat_isabet:
                    move_j = move[0]
                    move_i = move[1]
                    king_j = white_king_position[0]
                    king_i = white_king_position[1]
                    hadaf_j = move_j + king_j
                    hadaf_i = move_i + king_i

                    if hadaf_j > 0 and hadaf_i > 0 and hadaf_j < 9 and hadaf_i < 9:
                        temp_piece = globals()[f"square_{hadaf_j}{hadaf_i}"].piece
                        if temp_piece[0] == "b" or temp_piece[0] == "h" or temp_piece[0] == "p" or temp_piece[
                            0] == "q" or temp_piece[0] == "r":
                            piece_checked = 0
                            for move2 in position_check_jmosbat_isabet:
                                move2_j = move2[0]
                                move2_i = move2[1]
                                check_j = move2_j + hadaf_j
                                check_i = move2_i + hadaf_i
                                temp_piece2 = globals()[f"square_{check_j}{check_i}"].piece
                                if temp_piece2[0] == "R" or temp_piece2[0] == "Q":
                                    white_friendly_list.append([hadaf_j, hadaf_i, False])
                                    piece_checked = 1
                                elif temp_piece2[0] == "P" or temp_piece2[0] == "B" or temp_piece2[0] == "K" or \
                                        temp_piece2[
                                            0] == "H":
                                    white_friendly_list.append([hadaf_j, hadaf_i, True])
                                    piece_checked = 1
                                elif temp_piece2[0] == "q" or temp_piece2[0] == "p" or temp_piece2[0] == "r" or \
                                        temp_piece2[0] == "k" or temp_piece2[0] == "h" or temp_piece2[0] == "b":
                                    white_friendly_list.append([hadaf_j, hadaf_i, True])
                                    piece_checked = 1
                            if piece_checked == 0:
                                white_friendly_list.append([hadaf_j, hadaf_i, True])
                    ####################3###################
                position_check_jmanfi_isabet = [[- 1, 0], [- 2, 0], [- 3, 0], [- 4, 0], [- 5, 0], [- 6, 0],
                                                [- 7, 0]]
                for move in position_check_jmanfi_isabet:
                    move_j = move[0]
                    move_i = move[1]
                    king_j = white_king_position[0]
                    king_i = white_king_position[1]
                    hadaf_j = move_j + king_j
                    hadaf_i = move_i + king_i

                    if hadaf_j > 0 and hadaf_i > 0 and hadaf_j < 9 and hadaf_i < 9:
                        temp_piece = globals()[f"square_{hadaf_j}{hadaf_i}"].piece
                        if temp_piece[0] == "b" or temp_piece[0] == "h" or temp_piece[0] == "p" or temp_piece[
                            0] == "q" or temp_piece[0] == "r":
                            piece_checked = 0
                            for move2 in position_check_jmanfi_isabet:
                                move2_j = move2[0]
                                move2_i = move2[1]
                                check_j = move2_j + hadaf_j
                                check_i = move2_i + hadaf_i
                                temp_piece2 = globals()[f"square_{check_j}{check_i}"].piece
                                if temp_piece2[0] == "R" or temp_piece2[0] == "Q":
                                    white_friendly_list.append([hadaf_j, hadaf_i, False])
                                    piece_checked = 1
                                elif temp_piece2[0] == "P" or temp_piece2[0] == "B" or temp_piece2[0] == "K" or \
                                        temp_piece2[
                                            0] == "H":
                                    white_friendly_list.append([hadaf_j, hadaf_i, True])
                                    piece_checked = 1
                                elif temp_piece2[0] == "q" or temp_piece2[0] == "p" or temp_piece2[0] == "r" or \
                                        temp_piece2[0] == "k" or temp_piece2[0] == "h" or temp_piece2[0] == "b":
                                    white_friendly_list.append([hadaf_j, hadaf_i, True])
                                    piece_checked = 1
                            if piece_checked == 0:
                                white_friendly_list.append([hadaf_j, hadaf_i, True])
                        ####################4###################
                position_check_jmanfi_imosbat = [[- 1, + 1], [- 2, + 2], [- 3, + 3], [- 4, + 4], [- 5, + 5],
                                                 [- 6, + 6], [- 7, + 7]]
                for move in position_check_jmanfi_imosbat:
                    move_j = move[0]
                    move_i = move[1]
                    king_j = white_king_position[0]
                    king_i = white_king_position[1]
                    hadaf_j = move_j + king_j
                    hadaf_i = move_i + king_i

                    if hadaf_j > 0 and hadaf_i > 0 and hadaf_j < 9 and hadaf_i < 9:
                        temp_piece = globals()[f"square_{hadaf_j}{hadaf_i}"].piece
                        if temp_piece[0] == "b" or temp_piece[0] == "h" or temp_piece[0] == "p" or temp_piece[
                            0] == "q" or temp_piece[0] == "r":
                            piece_checked = 0
                            for move2 in position_check_jmanfi_imosbat:
                                move2_j = move2[0]
                                move2_i = move2[1]
                                check_j = move2_j + hadaf_j
                                check_i = move2_i + hadaf_i
                                temp_piece2 = globals()[f"square_{check_j}{check_i}"].piece
                                if temp_piece2[0] == "B" or temp_piece2[0] == "Q":
                                    white_friendly_list.append([hadaf_j, hadaf_i, False])
                                    piece_checked = 1
                                elif temp_piece2[0] == "P" or temp_piece2[0] == "R" or temp_piece2[0] == "K" or \
                                        temp_piece2[
                                            0] == "H":
                                    white_friendly_list.append([hadaf_j, hadaf_i, True])
                                    piece_checked = 1
                                elif temp_piece2[0] == "q" or temp_piece2[0] == "p" or temp_piece2[0] == "r" or \
                                        temp_piece2[0] == "k" or temp_piece2[0] == "h" or temp_piece2[0] == "b":
                                    white_friendly_list.append([hadaf_j, hadaf_i, True])
                                    piece_checked = 1
                            if piece_checked == 0:
                                white_friendly_list.append([hadaf_j, hadaf_i, True])
                        #################5###################
                position_check_jmosbat_imosbat = [[+ 1, + 1], [+ 2, + 2], [+ 3, + 3], [+ 4, + 4], [+ 5, + 5],
                                                  [+ 6, + 6], [+ 7, + 7]]
                for move in position_check_jmosbat_imosbat:
                    move_j = move[0]
                    move_i = move[1]
                    king_j = white_king_position[0]
                    king_i = white_king_position[1]
                    hadaf_j = move_j + king_j
                    hadaf_i = move_i + king_i

                    if hadaf_j > 0 and hadaf_i > 0 and hadaf_j < 9 and hadaf_i < 9:
                        temp_piece = globals()[f"square_{hadaf_j}{hadaf_i}"].piece
                        if temp_piece[0] == "b" or temp_piece[0] == "h" or temp_piece[0] == "p" or temp_piece[
                            0] == "q" or temp_piece[0] == "r":
                            piece_checked = 0
                            for move2 in position_check_jmosbat_imosbat:
                                move2_j = move2[0]
                                move2_i = move2[1]
                                check_j = move2_j + hadaf_j
                                check_i = move2_i + hadaf_i
                                temp_piece2 = globals()[f"square_{check_j}{check_i}"].piece
                                if temp_piece2[0] == "B" or temp_piece2[0] == "Q":
                                    white_friendly_list.append([hadaf_j, hadaf_i, False])
                                    piece_checked = 1
                                elif temp_piece2[0] == "P" or temp_piece2[0] == "R" or temp_piece2[0] == "K" or \
                                        temp_piece2[
                                            0] == "H":
                                    white_friendly_list.append([hadaf_j, hadaf_i, True])
                                    piece_checked = 1
                                elif temp_piece2[0] == "q" or temp_piece2[0] == "p" or temp_piece2[0] == "r" or \
                                        temp_piece2[0] == "k" or temp_piece2[0] == "h" or temp_piece2[0] == "b":
                                    white_friendly_list.append([hadaf_j, hadaf_i, True])
                                    piece_checked = 1
                            if piece_checked == 0:
                                white_friendly_list.append([hadaf_j, hadaf_i, True])
                            #############6###################
                position_check_jmanfi_imanfi = [[- 1, - 1], [- 2, - 2], [- 3, - 3], [- 4, - 4], [- 5, - 5],
                                                [- 6, - 6], [- 7, - 7]]
                for move in position_check_jmanfi_imanfi:
                    move_j = move[0]
                    move_i = move[1]
                    king_j = white_king_position[0]
                    king_i = white_king_position[1]
                    hadaf_j = move_j + king_j
                    hadaf_i = move_i + king_i

                    if hadaf_j > 0 and hadaf_i > 0 and hadaf_j < 9 and hadaf_i < 9:
                        temp_piece = globals()[f"square_{hadaf_j}{hadaf_i}"].piece
                        if temp_piece[0] == "b" or temp_piece[0] == "h" or temp_piece[0] == "p" or temp_piece[
                            0] == "q" or temp_piece[0] == "r":
                            piece_checked = 0
                            for move2 in position_check_jmanfi_imanfi:
                                move2_j = move2[0]
                                move2_i = move2[1]
                                check_j = move2_j + hadaf_j
                                check_i = move2_i + hadaf_i
                                temp_piece2 = globals()[f"square_{check_j}{check_i}"].piece
                                if temp_piece2[0] == "B" or temp_piece2[0] == "Q":
                                    white_friendly_list.append([hadaf_j, hadaf_i, False])
                                    piece_checked = 1
                                elif temp_piece2[0] == "P" or temp_piece2[0] == "R" or temp_piece2[0] == "K" or \
                                        temp_piece2[
                                            0] == "H":
                                    white_friendly_list.append([hadaf_j, hadaf_i, True])
                                    piece_checked = 1
                                elif temp_piece2[0] == "q" or temp_piece2[0] == "p" or temp_piece2[0] == "r" or \
                                        temp_piece2[0] == "k" or temp_piece2[0] == "h" or temp_piece2[0] == "b":
                                    white_friendly_list.append([hadaf_j, hadaf_i, True])
                                    piece_checked = 1
                            if piece_checked == 0:
                                white_friendly_list.append([hadaf_j, hadaf_i, True])
                                #####################7########################
                position_check_jmosbat_imanfi = [[+ 1, - 1], [+ 2, - 2], [+ 3, - 3], [+ 4, - 4], [+ 5, - 5],
                                                 [+ 6, - 6], [+ 7, - 7]]
                for move in position_check_jmosbat_imanfi:
                    move_j = move[0]
                    move_i = move[1]
                    king_j = black_king_position[0]
                    king_i = black_king_position[1]
                    hadaf_j = move_j + king_j
                    hadaf_i = move_i + king_i

                    if hadaf_j > 0 and hadaf_i > 0 and hadaf_j < 9 and hadaf_i < 9:
                        temp_piece = globals()[f"square_{hadaf_j}{hadaf_i}"].piece
                        if temp_piece[0] == "b" or temp_piece[0] == "h" or temp_piece[0] == "p" or temp_piece[
                            0] == "q" or temp_piece[0] == "r":
                            piece_checked = 0
                            for move2 in position_check_jmosbat_imanfi:
                                move2_j = move2[0]
                                move2_i = move2[1]
                                check_j = move2_j + hadaf_j
                                check_i = move2_i + hadaf_i
                                temp_piece2 = globals()[f"square_{check_j}{check_i}"].piece
                                if temp_piece2[0] == "B" or temp_piece2[0] == "Q":
                                    white_friendly_list.append([hadaf_j, hadaf_i, False])
                                    piece_checked = 1
                                elif temp_piece2[0] == "P" or temp_piece2[0] == "R" or temp_piece2[0] == "K" or \
                                        temp_piece2[
                                            0] == "H":
                                    white_friendly_list.append([hadaf_j, hadaf_i, True])
                                    piece_checked = 1
                                elif temp_piece2[0] == "q" or temp_piece2[0] == "p" or temp_piece2[0] == "r" or \
                                        temp_piece2[0] == "k" or temp_piece2[0] == "h" or temp_piece2[0] == "b":
                                    white_friendly_list.append([hadaf_j, hadaf_i, True])
                                    piece_checked = 1
                            if piece_checked == 0:
                                white_friendly_list.append([hadaf_j, hadaf_i, True])
                                #######################8################


            except Exception as err:
                print("problem in 1 ", err)
        #################################
        temp_piecemove_to_uncheck = []
        for item in white_picemove_to_uncheck:
            temp_piecemove_to_uncheck.append(item)
        for checked in white_friendly_list:
            checked_j = checked[0]
            checked_i = checked[1]
            for friend in white_picemove_to_uncheck:
                # j va i inja injorie
                friend_j = friend[3]
                friend_i = friend[4]
                try:
                    if checked_j == friend_j and checked_i == friend_i and checked[2] == True:
                        last_white_friendly_can_move.append([friend_j, friend_i, friend[0]])
                        temp_piecemove_to_uncheck.remove(
                            friend)  # onaii ke injri check shodan yani mitonan ro kingeshon tasir bezaran pak shodan
                    elif checked_j == friend_j and checked_i == friend_i and checked[2] == False:
                        temp_piecemove_to_uncheck.remove(friend)
                except Exception as err:
                    print("error toye  remove")

        white_picemove_to_uncheck = []
        for item2 in temp_piecemove_to_uncheck:
            white_picemove_to_uncheck.append(item2)
        # in paiinia baraye onaiie ke fagat unchek mikonan ba kingeshon kolan asib nemizanan
        for checkedd in white_picemove_to_uncheck:
            last_white_friendly_can_move.append([checkedd[1], checkedd[2], checkedd[0]])

    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


last_black_piece_move = []
last_white_piece_move = []


def last_move():
    # aval black
    black_king_360 = []
    try:
        position_ok = 0
        temp_king_360 = []
        position_check_jsabet_imosbat = [[+ 0, + 1], [+ 0, + 2], [+ 0, + 3], [+ 0, + 4], [+ 0, + 5],
                                         [+ 0, + 6], [+ 0, + 7]]
        for move in position_check_jsabet_imosbat:
            move_j = move[0]
            move_i = move[1]
            king_j = black_king_position[0]
            king_i = black_king_position[1]
            hadaf_j = move_j + king_j
            hadaf_i = move_i + king_i

            if hadaf_j > 0 and hadaf_i > 0 and hadaf_j < 9 and hadaf_i < 9:
                temp_piece = globals()[f"square_{hadaf_j}{hadaf_i}"].piece
                if temp_piece[0] == ".":
                    temp_king_360.append([hadaf_j, hadaf_i])
                if temp_piece[0] == "q" or temp_piece[0] == "r":
                    temp_king_360.append([hadaf_j, hadaf_i])
                    position_ok = 1
                    break
        if position_ok == 1:
            for item in temp_king_360:
                black_king_360.append(item)

                #############1#############
        position_ok = 0
        temp_king_360 = []
        position_check_jsabet_imanfi = [[+ 0, - 1], [+ 0, - 2], [+ 0, - 3], [+ 0, - 4], [+ 0, - 5],
                                        [+ 0, - 6], [+ 0, - 7]]
        for move in position_check_jsabet_imanfi:
            move_j = move[0]
            move_i = move[1]
            king_j = black_king_position[0]
            king_i = black_king_position[1]
            hadaf_j = move_j + king_j
            hadaf_i = move_i + king_i
            if hadaf_j > 0 and hadaf_i > 0 and hadaf_j < 9 and hadaf_i < 9:
                temp_piece = globals()[f"square_{hadaf_j}{hadaf_i}"].piece
                if temp_piece[0] == ".":
                    temp_king_360.append([hadaf_j, hadaf_i])
                elif temp_piece[0] == "q" or temp_piece[0] == "r":
                    temp_king_360.append([hadaf_j, hadaf_i])
                    position_ok = 1
                    break
        if position_ok == 1:
            for item in temp_king_360:
                black_king_360.append(item)
                ##################2###############
        position_ok = 0
        temp_king_360 = []
        position_check_jmosbat_isabet = [[+ 1, 0], [+ 2, 0], [+ 3, 0], [+ 4, 0], [+ 5, 0], [+ 6, 0],
                                         [+ 7, 0]]
        for move in position_check_jmosbat_isabet:
            move_j = move[0]
            move_i = move[1]
            king_j = black_king_position[0]
            king_i = black_king_position[1]
            hadaf_j = move_j + king_j
            hadaf_i = move_i + king_i

            if hadaf_j > 0 and hadaf_i > 0 and hadaf_j < 9 and hadaf_i < 9:
                temp_piece = globals()[f"square_{hadaf_j}{hadaf_i}"].piece
                if temp_piece[0] == ".":
                    temp_king_360.append([hadaf_j, hadaf_i])
                if temp_piece[0] == "q" or temp_piece[0] == "r":
                    temp_king_360.append([hadaf_j, hadaf_i])
                    position_ok = 1
                    break
        if position_ok == 1:
            for item in temp_king_360:
                black_king_360.append(item)
            ####################3###################
        position_ok = 0
        temp_king_360 = []
        position_check_jmanfi_isabet = [[- 1, 0], [- 2, 0], [- 3, 0], [- 4, 0], [- 5, 0], [- 6, 0],
                                        [- 7, 0]]
        for move in position_check_jmanfi_isabet:
            move_j = move[0]
            move_i = move[1]
            king_j = black_king_position[0]
            king_i = black_king_position[1]
            hadaf_j = move_j + king_j
            hadaf_i = move_i + king_i

            if hadaf_j > 0 and hadaf_i > 0 and hadaf_j < 9 and hadaf_i < 9:
                temp_piece = globals()[f"square_{hadaf_j}{hadaf_i}"].piece
                if temp_piece[0] == ".":
                    temp_king_360.append([hadaf_j, hadaf_i])
                if temp_piece[0] == "q" or temp_piece[0] == "r":
                    temp_king_360.append([hadaf_j, hadaf_i])
                    position_ok = 1
                    break
        if position_ok == 1:
            for item in temp_king_360:
                black_king_360.append(item)
                ####################4###################
        position_ok = 0
        temp_king_360 = []
        position_check_jmanfi_imosbat = [[- 1, + 1], [- 2, + 2], [- 3, + 3], [- 4, + 4], [- 5, + 5],
                                         [- 6, + 6], [- 7, + 7]]
        for move in position_check_jmanfi_imosbat:
            move_j = move[0]
            move_i = move[1]
            king_j = black_king_position[0]
            king_i = black_king_position[1]
            hadaf_j = move_j + king_j
            hadaf_i = move_i + king_i

            if hadaf_j > 0 and hadaf_i > 0 and hadaf_j < 9 and hadaf_i < 9:
                temp_piece = globals()[f"square_{hadaf_j}{hadaf_i}"].piece
                if temp_piece[0] == ".":
                    temp_king_360.append([hadaf_j, hadaf_i])
                if temp_piece[0] == "q" or temp_piece[0] == "b":
                    temp_king_360.append([hadaf_j, hadaf_i])
                    position_ok = 1
                    break
        if position_ok == 1:
            for item in temp_king_360:
                black_king_360.append(item)
                #################5###################
        position_ok = 0
        temp_king_360 = []
        position_check_jmosbat_imosbat = [[+ 1, + 1], [+ 2, + 2], [+ 3, + 3], [+ 4, + 4], [+ 5, + 5],
                                          [+ 6, + 6], [+ 7, + 7]]
        for move in position_check_jmosbat_imosbat:
            move_j = move[0]
            move_i = move[1]
            king_j = black_king_position[0]
            king_i = black_king_position[1]
            hadaf_j = move_j + king_j
            hadaf_i = move_i + king_i

            if hadaf_j > 0 and hadaf_i > 0 and hadaf_j < 9 and hadaf_i < 9:
                temp_piece = globals()[f"square_{hadaf_j}{hadaf_i}"].piece
                if temp_piece[0] == ".":
                    temp_king_360.append([hadaf_j, hadaf_i])
                if temp_piece[0] == "q" or temp_piece[0] == "b":
                    temp_king_360.append([hadaf_j, hadaf_i])
                    position_ok = 1
                    break
        if position_ok == 1:
            for item in temp_king_360:
                black_king_360.append(item)
                #############6###################
        position_ok = 0
        temp_king_360 = []
        position_check_jmanfi_imanfi = [[- 1, - 1], [- 2, - 2], [- 3, - 3], [- 4, - 4], [- 5, - 5],
                                        [- 6, - 6], [- 7, - 7]]
        for move in position_check_jmanfi_imanfi:
            move_j = move[0]
            move_i = move[1]
            king_j = black_king_position[0]
            king_i = black_king_position[1]
            hadaf_j = move_j + king_j
            hadaf_i = move_i + king_i

            if hadaf_j > 0 and hadaf_i > 0 and hadaf_j < 9 and hadaf_i < 9:
                temp_piece = globals()[f"square_{hadaf_j}{hadaf_i}"].piece
                if temp_piece[0] == ".":
                    temp_king_360.append([hadaf_j, hadaf_i])
                if temp_piece[0] == "q" or temp_piece[0] == "b":
                    temp_king_360.append([hadaf_j, hadaf_i])
                    position_ok = 1
                    break
        if position_ok == 1:
            for item in temp_king_360:
                black_king_360.append(item)
                #####################7########################
        position_ok = 0
        temp_king_360 = []
        position_check_jmosbat_imanfi = [[+ 1, - 1], [+ 2, - 2], [+ 3, - 3], [+ 4, - 4], [+ 5, - 5],
                                         [+ 6, - 6], [+ 7, - 7]]
        for move in position_check_jmosbat_imanfi:
            move_j = move[0]
            move_i = move[1]
            king_j = black_king_position[0]
            king_i = black_king_position[1]
            hadaf_j = move_j + king_j
            hadaf_i = move_i + king_i

            if hadaf_j > 0 and hadaf_i > 0 and hadaf_j < 9 and hadaf_i < 9:
                temp_piece = globals()[f"square_{hadaf_j}{hadaf_i}"].piece
                if temp_piece[0] == ".":
                    temp_king_360.append([hadaf_j, hadaf_i])
                if temp_piece[0] == "q" or temp_piece[0] == "b":
                    temp_king_360.append([hadaf_j, hadaf_i])
                    position_ok = 1
                    break
        if position_ok == 1:
            for item in temp_king_360:
                black_king_360.append(item)
                #######################8################
    except Exception as err:
        print("!", err)
    for last in last_black_friendly_can_move:
        last_j = last[0]
        last_i = last[1]
        for king_360 in black_king_360:
            king_360_j = king_360[0]
            king_360_i = king_360[1]
            if last_j == king_360_j and last_i == king_360_i:
                last_black_piece_move.append(last)
    black_king_360 = []

    try:
        position_ok = 0
        temp_king_360 = []
        position_check_jsabet_imosbat = [[+ 0, + 1], [+ 0, + 2], [+ 0, + 3], [+ 0, + 4], [+ 0, + 5],
                                         [+ 0, + 6], [+ 0, + 7]]
        for move in position_check_jsabet_imosbat:
            move_j = move[0]
            move_i = move[1]
            king_j = black_king_position[0]
            king_i = black_king_position[1]
            hadaf_j = move_j + king_j
            hadaf_i = move_i + king_i

            if hadaf_j > 0 and hadaf_i > 0 and hadaf_j < 9 and hadaf_i < 9:
                temp_piece = globals()[f"square_{hadaf_j}{hadaf_i}"].piece
                if temp_piece[0] == ".":
                    temp_king_360.append([hadaf_j, hadaf_i])
                if temp_piece[0] == "q" or temp_piece[0] == "r":
                    temp_king_360.append([hadaf_j, hadaf_i])
                    position_ok = 1
                    break
        if position_ok == 1:
            for item in temp_king_360:
                black_king_360.append(item)

                #############1#############
        position_ok = 0
        temp_king_360 = []
        position_check_jsabet_imanfi = [[+ 0, - 1], [+ 0, - 2], [+ 0, - 3], [+ 0, - 4], [+ 0, - 5],
                                        [+ 0, - 6], [+ 0, - 7]]
        for move in position_check_jsabet_imanfi:
            move_j = move[0]
            move_i = move[1]
            king_j = black_king_position[0]
            king_i = black_king_position[1]
            hadaf_j = move_j + king_j
            hadaf_i = move_i + king_i

            if hadaf_j > 0 and hadaf_i > 0 and hadaf_j < 9 and hadaf_i < 9:
                temp_piece = globals()[f"square_{hadaf_j}{hadaf_i}"].piece
                if temp_piece[0] == ".":

                    temp_king_360.append([hadaf_j, hadaf_i])
                elif temp_piece[0] == "q" or temp_piece[0] == "r":

                    temp_king_360.append([hadaf_j, hadaf_i])
                    position_ok = 1
                    break
        if position_ok == 1:

            for item in temp_king_360:
                black_king_360.append(item)
                ##################2###############
        position_ok = 0
        temp_king_360 = []
        position_check_jmosbat_isabet = [[+ 1, 0], [+ 2, 0], [+ 3, 0], [+ 4, 0], [+ 5, 0], [+ 6, 0],
                                         [+ 7, 0]]
        for move in position_check_jmosbat_isabet:
            move_j = move[0]
            move_i = move[1]
            king_j = black_king_position[0]
            king_i = black_king_position[1]
            hadaf_j = move_j + king_j
            hadaf_i = move_i + king_i

            if hadaf_j > 0 and hadaf_i > 0 and hadaf_j < 9 and hadaf_i < 9:
                temp_piece = globals()[f"square_{hadaf_j}{hadaf_i}"].piece
                if temp_piece[0] == ".":
                    temp_king_360.append([hadaf_j, hadaf_i])
                if temp_piece[0] == "q" or temp_piece[0] == "r":
                    temp_king_360.append([hadaf_j, hadaf_i])
                    position_ok = 1
                    break
        if position_ok == 1:
            for item in temp_king_360:
                black_king_360.append(item)
            ####################3###################
        position_ok = 0
        temp_king_360 = []
        position_check_jmanfi_isabet = [[- 1, 0], [- 2, 0], [- 3, 0], [- 4, 0], [- 5, 0], [- 6, 0],
                                        [- 7, 0]]
        for move in position_check_jmanfi_isabet:
            move_j = move[0]
            move_i = move[1]
            king_j = black_king_position[0]
            king_i = black_king_position[1]
            hadaf_j = move_j + king_j
            hadaf_i = move_i + king_i

            if hadaf_j > 0 and hadaf_i > 0 and hadaf_j < 9 and hadaf_i < 9:
                temp_piece = globals()[f"square_{hadaf_j}{hadaf_i}"].piece
                if temp_piece[0] == ".":
                    temp_king_360.append([hadaf_j, hadaf_i])
                if temp_piece[0] == "q" or temp_piece[0] == "r":
                    temp_king_360.append([hadaf_j, hadaf_i])
                    position_ok = 1
                    break
        if position_ok == 1:
            for item in temp_king_360:
                black_king_360.append(item)
                ####################4###################
        position_ok = 0
        temp_king_360 = []
        position_check_jmanfi_imosbat = [[- 1, + 1], [- 2, + 2], [- 3, + 3], [- 4, + 4], [- 5, + 5],
                                         [- 6, + 6], [- 7, + 7]]
        for move in position_check_jmanfi_imosbat:
            move_j = move[0]
            move_i = move[1]
            king_j = black_king_position[0]
            king_i = black_king_position[1]
            hadaf_j = move_j + king_j
            hadaf_i = move_i + king_i

            if hadaf_j > 0 and hadaf_i > 0 and hadaf_j < 9 and hadaf_i < 9:
                temp_piece = globals()[f"square_{hadaf_j}{hadaf_i}"].piece
                if temp_piece[0] == ".":
                    temp_king_360.append([hadaf_j, hadaf_i])
                if temp_piece[0] == "q" or temp_piece[0] == "b":
                    temp_king_360.append([hadaf_j, hadaf_i])
                    position_ok = 1
                    break
        if position_ok == 1:
            for item in temp_king_360:
                black_king_360.append(item)
                #################5###################
        position_ok = 0
        temp_king_360 = []
        position_check_jmosbat_imosbat = [[+ 1, + 1], [+ 2, + 2], [+ 3, + 3], [+ 4, + 4], [+ 5, + 5],
                                          [+ 6, + 6], [+ 7, + 7]]
        for move in position_check_jmosbat_imosbat:
            move_j = move[0]
            move_i = move[1]
            king_j = black_king_position[0]
            king_i = black_king_position[1]
            hadaf_j = move_j + king_j
            hadaf_i = move_i + king_i

            if hadaf_j > 0 and hadaf_i > 0 and hadaf_j < 9 and hadaf_i < 9:
                temp_piece = globals()[f"square_{hadaf_j}{hadaf_i}"].piece
                if temp_piece[0] == ".":
                    temp_king_360.append([hadaf_j, hadaf_i])
                if temp_piece[0] == "q" or temp_piece[0] == "b":
                    temp_king_360.append([hadaf_j, hadaf_i])
                    position_ok = 1
                    break
        if position_ok == 1:
            for item in temp_king_360:
                black_king_360.append(item)
                #############6###################
        position_ok = 0
        temp_king_360 = []
        position_check_jmanfi_imanfi = [[- 1, - 1], [- 2, - 2], [- 3, - 3], [- 4, - 4], [- 5, - 5],
                                        [- 6, - 6], [- 7, - 7]]
        for move in position_check_jmanfi_imanfi:
            move_j = move[0]
            move_i = move[1]
            king_j = black_king_position[0]
            king_i = black_king_position[1]
            hadaf_j = move_j + king_j
            hadaf_i = move_i + king_i

            if hadaf_j > 0 and hadaf_i > 0 and hadaf_j < 9 and hadaf_i < 9:
                temp_piece = globals()[f"square_{hadaf_j}{hadaf_i}"].piece
                if temp_piece[0] == ".":
                    temp_king_360.append([hadaf_j, hadaf_i])
                if temp_piece[0] == "q" or temp_piece[0] == "b":
                    temp_king_360.append([hadaf_j, hadaf_i])
                    position_ok = 1
                    break
        if position_ok == 1:
            for item in temp_king_360:
                black_king_360.append(item)
                #####################7########################
        position_ok = 0
        temp_king_360 = []
        position_check_jmosbat_imanfi = [[+ 1, - 1], [+ 2, - 2], [+ 3, - 3], [+ 4, - 4], [+ 5, - 5],
                                         [+ 6, - 6], [+ 7, - 7]]
        for move in position_check_jmosbat_imanfi:
            move_j = move[0]
            move_i = move[1]
            king_j = black_king_position[0]
            king_i = black_king_position[1]
            hadaf_j = move_j + king_j
            hadaf_i = move_i + king_i

            if hadaf_j > 0 and hadaf_i > 0 and hadaf_j < 9 and hadaf_i < 9:
                temp_piece = globals()[f"square_{hadaf_j}{hadaf_i}"].piece
                if temp_piece[0] == ".":
                    temp_king_360.append([hadaf_j, hadaf_i])
                if temp_piece[0] == "q" or temp_piece[0] == "b":
                    temp_king_360.append([hadaf_j, hadaf_i])
                    position_ok = 1
                    break
        if position_ok == 1:
            for item in temp_king_360:
                black_king_360.append(item)
                #######################8################
    except Exception as err:
        print("!", err)
    for last in last_black_friendly_can_move:
        last_j = last[0]
        last_i = last[1]
        for king_360 in black_king_360:
            king_360_j = king_360[0]
            king_360_i = king_360[1]
            if last_j == king_360_j and last_i == king_360_i:
                last_black_piece_move.append(last)

    ##################### hala white ######################

    white_king_360 = []
    try:
        position_ok = 0
        temp_king_360 = []
        position_check_jsabet_imosbat = [[+ 0, + 1], [+ 0, + 2], [+ 0, + 3], [+ 0, + 4], [+ 0, + 5],
                                         [+ 0, + 6], [+ 0, + 7]]
        for move in position_check_jsabet_imosbat:
            move_j = move[0]
            move_i = move[1]
            king_j = white_king_position[0]
            king_i = white_king_position[1]
            hadaf_j = move_j + king_j
            hadaf_i = move_i + king_i

            if hadaf_j > 0 and hadaf_i > 0 and hadaf_j < 9 and hadaf_i < 9:
                temp_piece = globals()[f"square_{hadaf_j}{hadaf_i}"].piece
                if temp_piece[0] == ".":
                    temp_king_360.append([hadaf_j, hadaf_i])
                if temp_piece[0] == "Q" or temp_piece[0] == "R":
                    temp_king_360.append([hadaf_j, hadaf_i])
                    position_ok = 1
                    break
        if position_ok == 1:
            for item in temp_king_360:
                white_king_360.append(item)

                #############1#############
        position_ok = 0
        temp_king_360 = []
        position_check_jsabet_imanfi = [[+ 0, - 1], [+ 0, - 2], [+ 0, - 3], [+ 0, - 4], [+ 0, - 5],
                                        [+ 0, - 6], [+ 0, - 7]]
        for move in position_check_jsabet_imanfi:
            move_j = move[0]
            move_i = move[1]
            king_j = white_king_position[0]
            king_i = white_king_position[1]
            hadaf_j = move_j + king_j
            hadaf_i = move_i + king_i

            if hadaf_j > 0 and hadaf_i > 0 and hadaf_j < 9 and hadaf_i < 9:
                temp_piece = globals()[f"square_{hadaf_j}{hadaf_i}"].piece
                if temp_piece[0] == ".":

                    temp_king_360.append([hadaf_j, hadaf_i])
                elif temp_piece[0] == "Q" or temp_piece[0] == "R":

                    temp_king_360.append([hadaf_j, hadaf_i])
                    position_ok = 1
                    break
        if position_ok == 1:

            for item in temp_king_360:
                white_king_360.append(item)
                ##################2###############
        position_ok = 0
        temp_king_360 = []
        position_check_jmosbat_isabet = [[+ 1, 0], [+ 2, 0], [+ 3, 0], [+ 4, 0], [+ 5, 0], [+ 6, 0],
                                         [+ 7, 0]]
        for move in position_check_jmosbat_isabet:
            move_j = move[0]
            move_i = move[1]
            king_j = white_king_position[0]
            king_i = white_king_position[1]
            hadaf_j = move_j + king_j
            hadaf_i = move_i + king_i

            if hadaf_j > 0 and hadaf_i > 0 and hadaf_j < 9 and hadaf_i < 9:
                temp_piece = globals()[f"square_{hadaf_j}{hadaf_i}"].piece
                if temp_piece[0] == ".":
                    temp_king_360.append([hadaf_j, hadaf_i])
                if temp_piece[0] == "Q" or temp_piece[0] == "R":
                    temp_king_360.append([hadaf_j, hadaf_i])
                    position_ok = 1
                    break
        if position_ok == 1:
            for item in temp_king_360:
                white_king_360.append(item)
            ####################3###################
        position_ok = 0
        temp_king_360 = []
        position_check_jmanfi_isabet = [[- 1, 0], [- 2, 0], [- 3, 0], [- 4, 0], [- 5, 0], [- 6, 0],
                                        [- 7, 0]]
        for move in position_check_jmanfi_isabet:
            move_j = move[0]
            move_i = move[1]
            king_j = white_king_position[0]
            king_i = white_king_position[1]
            hadaf_j = move_j + king_j
            hadaf_i = move_i + king_i

            if hadaf_j > 0 and hadaf_i > 0 and hadaf_j < 9 and hadaf_i < 9:
                temp_piece = globals()[f"square_{hadaf_j}{hadaf_i}"].piece
                if temp_piece[0] == ".":
                    temp_king_360.append([hadaf_j, hadaf_i])
                if temp_piece[0] == "Q" or temp_piece[0] == "R":
                    temp_king_360.append([hadaf_j, hadaf_i])
                    position_ok = 1
                    break
        if position_ok == 1:
            for item in temp_king_360:
                white_king_360.append(item)
                ####################4###################
        position_ok = 0
        temp_king_360 = []
        position_check_jmanfi_imosbat = [[- 1, + 1], [- 2, + 2], [- 3, + 3], [- 4, + 4], [- 5, + 5],
                                         [- 6, + 6], [- 7, + 7]]
        for move in position_check_jmanfi_imosbat:
            move_j = move[0]
            move_i = move[1]
            king_j = white_king_position[0]
            king_i = white_king_position[1]
            hadaf_j = move_j + king_j
            hadaf_i = move_i + king_i

            if hadaf_j > 0 and hadaf_i > 0 and hadaf_j < 9 and hadaf_i < 9:
                temp_piece = globals()[f"square_{hadaf_j}{hadaf_i}"].piece
                if temp_piece[0] == ".":
                    temp_king_360.append([hadaf_j, hadaf_i])
                if temp_piece[0] == "Q" or temp_piece[0] == "B":
                    temp_king_360.append([hadaf_j, hadaf_i])
                    position_ok = 1
                    break
        if position_ok == 1:
            for item in temp_king_360:
                white_king_360.append(item)
                #################5###################
        position_ok = 0
        temp_king_360 = []
        position_check_jmosbat_imosbat = [[+ 1, + 1], [+ 2, + 2], [+ 3, + 3], [+ 4, + 4], [+ 5, + 5],
                                          [+ 6, + 6], [+ 7, + 7]]
        for move in position_check_jmosbat_imosbat:
            move_j = move[0]
            move_i = move[1]
            king_j = white_king_position[0]
            king_i = white_king_position[1]
            hadaf_j = move_j + king_j
            hadaf_i = move_i + king_i

            if hadaf_j > 0 and hadaf_i > 0 and hadaf_j < 9 and hadaf_i < 9:
                temp_piece = globals()[f"square_{hadaf_j}{hadaf_i}"].piece
                if temp_piece[0] == ".":
                    temp_king_360.append([hadaf_j, hadaf_i])
                if temp_piece[0] == "Q" or temp_piece[0] == "B":
                    temp_king_360.append([hadaf_j, hadaf_i])
                    position_ok = 1
                    break
        if position_ok == 1:
            for item in temp_king_360:
                white_king_360.append(item)
                #############6###################
        position_ok = 0
        temp_king_360 = []
        position_check_jmanfi_imanfi = [[- 1, - 1], [- 2, - 2], [- 3, - 3], [- 4, - 4], [- 5, - 5],
                                        [- 6, - 6], [- 7, - 7]]
        for move in position_check_jmanfi_imanfi:
            move_j = move[0]
            move_i = move[1]
            king_j = white_king_position[0]
            king_i = white_king_position[1]
            hadaf_j = move_j + king_j
            hadaf_i = move_i + king_i

            if hadaf_j > 0 and hadaf_i > 0 and hadaf_j < 9 and hadaf_i < 9:
                temp_piece = globals()[f"square_{hadaf_j}{hadaf_i}"].piece
                if temp_piece[0] == ".":
                    temp_king_360.append([hadaf_j, hadaf_i])
                if temp_piece[0] == "Q" or temp_piece[0] == "B":
                    temp_king_360.append([hadaf_j, hadaf_i])
                    position_ok = 1
                    break
        if position_ok == 1:
            for item in temp_king_360:
                white_king_360.append(item)
                #####################7########################
        position_ok = 0
        temp_king_360 = []
        position_check_jmosbat_imanfi = [[+ 1, - 1], [+ 2, - 2], [+ 3, - 3], [+ 4, - 4], [+ 5, - 5],
                                         [+ 6, - 6], [+ 7, - 7]]
        for move in position_check_jmosbat_imanfi:
            move_j = move[0]
            move_i = move[1]
            king_j = white_king_position[0]
            king_i = white_king_position[1]
            hadaf_j = move_j + king_j
            hadaf_i = move_i + king_i

            if hadaf_j > 0 and hadaf_i > 0 and hadaf_j < 9 and hadaf_i < 9:
                temp_piece = globals()[f"square_{hadaf_j}{hadaf_i}"].piece
                if temp_piece[0] == ".":
                    temp_king_360.append([hadaf_j, hadaf_i])
                if temp_piece[0] == "Q" or temp_piece[0] == "B":
                    temp_king_360.append([hadaf_j, hadaf_i])
                    position_ok = 1
                    break
        if position_ok == 1:
            for item in temp_king_360:
                white_king_360.append(item)
                #######################8################
    except Exception as err:
        print("!", err)
    for last in last_white_friendly_can_move:
        last_j = last[0]
        last_i = last[1]
        for king_360 in white_king_360:
            king_360_j = king_360[0]
            king_360_i = king_360[1]
            if last_j == king_360_j and last_i == king_360_i:
                last_white_piece_move.append(last)


def kish_va_mate():
    global white_kish
    global black_kish
    global black_mate
    global white_mate
    global wehave_white_king
    global wehave_black_king

    print("\n #####kish va mate #####")
    try:
        kisher_block_finder()
    except Exception as err:
        print("error piece koli", err)
    try:
        kish_check()
    except Exception as err:
        print("error kish koli", err)
    try:
        check_check()
    except Exception as err:
        print("error check check koli", err)
    try:
        uncheck_king_byking()
    except Exception as err:
        print("error uncheck king koli", err)
    try:
        uncheck_king_bypiece()
    except Exception as err:
        print("error piece koli", err)
    try:
        uncheck_by_piece_move()
    except Exception as err:
        print("error piece koli", err)
    try:
        last_move()
    except Exception as err:
        print("error piece koli", err)
    len_black_king_move_list = len(black_king_move_list)
    len_white_king_move_list = len(white_king_move_list)

    print("\n\n ################### natayej ########################")
    ##### aval black ######
    A, B, C, D, E, F = "", "", "", "", "", ""
    if wehave_black_king == True:
        if black_kish == 1:
            if len_black_king_move_list != 0:
                A = "black King can move !"
                black_mate = 0
            elif len_black_king_move_list == 0:
                A = "black King can NOT move !"
                temp_piece_len = len(black_friendly)
                if temp_piece_len > 0:
                    B = "a piece can uncheck the Black king"
                    print(black_friendly)
                    black_mate = 0
                elif temp_piece_len == 0:
                    B = "no one can attack enemy kisher"
                    temp_friendly_move_len = len(last_black_piece_move)
                    if temp_friendly_move_len > 0:
                        for friend_who_canmove in last_black_piece_move:
                            C = friend_who_canmove[2][0], "can uncheck king  by moving to ", friend_who_canmove[0], \
                                friend_who_canmove[1]
                            black_mate = 0
                    if temp_friendly_move_len == 0:
                        black_mate = 1
                        D = "!!!!! Black Mate Shod !!!!!!"
        else:
            E = "black king kish nashode !"
    else:
        F = "we dont have black king in game! :)"
    ###### hala white ########
    a, b, c, d, e, f = "", "", "", "", "", ""
    if wehave_white_king == True:
        if white_kish == 1:
            if len_white_king_move_list != 0:
                a = "white King can move !"
                white_mate = 0
            elif len_white_king_move_list == 0:
                a = "white King can NOT move !"
                temp_piece_len = len(white_friendly)
                if temp_piece_len > 0:
                    b = "a piece can uncheck the white king"
                    print(white_friendly)
                    white_mate = 0
                elif temp_piece_len == 0:
                    b = "no one can attack enemy kisher"
                    temp_friendly_move_len = len(last_white_piece_move)
                    if temp_friendly_move_len > 0:
                        for friend_who_canmove in last_white_piece_move:
                            c = friend_who_canmove[2][0], "can uncheck king  by moving to ", friend_who_canmove[0], \
                                friend_who_canmove[1]
                            white_mate = 0
                    if temp_friendly_move_len == 0:
                        white_mate = 1
                        d = "!!!!! white Mate Shod !!!!!!"
        else:
            e = "white king kish nashode !"
    else:
        f = "we dont have white king in game! :)"

    messagebox.showinfo("natayej !", f"{a}\n{b}\n{c}\n{d}\n{e}\n{f}\n")
    messagebox.showinfo("natayej !", f"{A}\n{B}\n{C}\n{D}\n{E}\n{F}\n")
    print("\n\n ##################################################")


# menu functions
"""def menu_names():
    print("\n")
    names=["Check Status","Change piece","check piece status","asar gozari","undo asar gozari(+ undo kish va mate)","check kish and mate!(bad az asar gozari!)"]
    counter=1
    while(counter<=len(names)):
        print(counter,"=",names[counter-1])
        counter+=1"""

"""def menu(choose):
    if choose == 1:
        clear()
        print("\nCheck Status selected !")
        print("\nmenu -> Check Status")
        for j in satr:
            for i in soton:
                check_status(j, i)

    elif choose ==2:
        clear()
        print("\nChange piece selected !")
        print("\nmenu -> Change piece ->")
        change_piece()
    elif choose == 3:
        clear()
        print("\nCheck piece Status selected !")
        print("\nmenu -> Check piece status")
        check_piece_status()

    elif choose == 4:
        clear()
        print("\nasar gozari selected !")
        print("\nmenu -> asar gozari")
        for p in piece_id_list:
            asargozari(p)


    elif choose==5:
        clear()
        print("\nundo asar gozari selected !")
        print("\nmenu -> asar gozari")
        undo_asargozari()
    elif choose==6:
        clear()
        print("\nkish va mate selected !")
        print("\nmenu -> check kish va mate")
        for j in satr:
            for i in soton:
                check_status(j, i)
        print("\n##############################")
        kish_va_mate()

    elif choose == 0:
        global menu_counter
        menu_counter=1"""


# create square objects
def asargozari_for_front():
    for sq in square_list:
        j = globals()[sq].satr
        i = globals()[sq].soton
        tempname = globals()[f"piece_{j}{i}_name"].get()
        if tempname != ".":
            add_piece([j, i, tempname])
    for p in piece_id_list:
        asargozari(p)


# ((((((((((((()))))))))))))
root = Tk()
# ((((((((((((()))))))))))))
soton = range(1, 9)
satr = range(1, 9)

for j in satr:
    for i in soton:
        globals()[f"square_{j}{i}"] = square(j, i, ".", 0)
        square_list.append(f"square_{j}{i}")
# ((((((((((((()))))))))))))
piece_names = [".", "p", "k", "r", "h", "b", "q", "P", "K", "R", "H", "B", "Q"]
temp_color = 0
counter_color = 0
for sq in square_list:
    j = globals()[sq].satr
    i = globals()[sq].soton
    globals()[f"piece_{j}{i}_name"] = StringVar()
    globals()[f"piece_{j}{i}_name"].set(".")
    globals()[f"square_{j}{i}_show"] = OptionMenu(root, globals()[f"piece_{j}{i}_name"], *piece_names)
    globals()[f"square_{j}{i}_show"].configure(padx=30, pady=30, fg="#F3120B")

    if temp_color == 1 and counter_color >= 8:
        counter_color = 0
        temp_color = 0
    elif temp_color == 0 and counter_color >= 8:
        counter_color = 0
        temp_color = 1
    if temp_color == 0 and counter_color < 8:
        globals()[f"square_{j}{i}_show"].configure(bg="#EDE8E7")
        temp_color = 1
        counter_color += 1
    elif temp_color == 1 and counter_color < 8:
        globals()[f"square_{j}{i}_show"].configure(bg="#2C2929")
        temp_color = 0
        counter_color += 1
    globals()[f"square_{j}{i}_show"].grid(row=j, column=i)

asargozari_btn = Button(root, text="asar gozari")
asargozari_btn.configure(padx=10, pady=10, fg="red", bg="#E8F30B", command=asargozari_for_front)
asargozari_btn.grid(row=9, column=4)

asargozari_btn = Button(root, text="natije")
asargozari_btn.configure(padx=10, pady=10, fg="red", bg="#E8F30B", command=kish_va_mate)
asargozari_btn.grid(row=9, column=5)
# ((((((((((((()))))))))))))
# menu
"""
menu_counter=0
print("hadaf bazi shatranj")
try:
    while(menu_counter ==0):

        print("\n menu ->")
        menu_names()
        print("0 = Exit")



        try:
            choose=int(input("\n\nchoose menu ="))
            menu(choose)
        except Exception as err:
            print(err)
except Exception as err:
    print("! in main menu",err)

"""
root.mainloop()
