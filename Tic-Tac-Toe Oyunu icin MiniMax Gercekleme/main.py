import tkinter as tk
from tkinter import messagebox

# Oyun tahtasını temsil edecek 3x3'lük bir liste
board = [[" " for _ in range(3)] for _ in range(3)]

# Oyunun bitip bitmediğini kontrol eden fonksiyon
def is_winner(board, player):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == player:
            return True
        if board[0][i] == board[1][i] == board[2][i] == player:
            return True
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True
    return False

# Hamle yapılabilir pozisyonları döndüren fonksiyon
def get_possible_moves(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == " "]

# Minimax algoritmasının ana fonksiyonu
def minimax(board, is_maximizing):
    # Baz durumlar
    if is_winner(board, "X"):
        return (None, 10)
    if is_winner(board, "O"):
        return (None, -10)
    if not any(" " in row for row in board):
        return (None, 0)

    if is_maximizing:
        best_score = -float("inf")
        best_move = None
        for move in get_possible_moves(board):
            board[move[0]][move[1]] = "X"
            _, score = minimax(board, False)
            board[move[0]][move[1]] = " "
            if score > best_score:
                best_score = score
                best_move = move
        return (best_move, best_score)
    else:
        best_score = float("inf")
        best_move = None
        for move in get_possible_moves(board):
            board[move[0]][move[1]] = "O"
            _, score = minimax(board, True)
            board[move[0]][move[1]] = " "
            if score < best_score:
                best_score = score
                best_move = move
        return (best_move, best_score)

# Buton tıklama olayını işleyen fonksiyon
def on_click(row, col):
    global board, buttons
    if board[row][col] == " " and not is_winner(board, "X") and not is_winner(board, "O"):
        board[row][col] = "O"
        buttons[row][col].config(text="O")
        buttons[row][col].update_idletasks()  # Bu satırı ekleyin
        if is_winner(board, "O"):
            messagebox.showinfo("Tic-Tac-Toe", "O kazandı!")
            reset_board()
        else:
            move, _ = minimax(board, True)
            if move:
                board[move[0]][move[1]] = "X"
                buttons[move[0]][move[1]].config(text="X")
                buttons[move[0]][move[1]].update_idletasks()  # Ve bu satırı ekleyin
                if is_winner(board, "X"):
                    messagebox.showinfo("Tic-Tac-Toe", "X kazandı!")
                    reset_board()
            if not any(" " in row for row in board):
                messagebox.showinfo("Tic-Tac-Toe", "Berabere!")
                reset_board()


# Tahtayı sıfırlayan fonksiyon
def reset_board():
    global board
    board = [[" " for _ in range(3)] for _ in range(3)]
    for i in range(3):
        for j in range(3):
            buttons[i][j].config(text=" ", state=tk.NORMAL)

# Tkinter penceresini oluşturma
root = tk.Tk()
root.title("Tic-Tac-Toe")
buttons = [[tk.Button(root, text=" ", font=('normal', 20), width=5, height=2,
                      command=lambda i=i, j=j: on_click(i, j)) for j in range(3)] for i in range(3)]

# Butonları grid yapısına yerleştirme
for i in range(3):
    for j in range(3):
        buttons[i][j].grid(row=i, column=j)

# Pencereyi gösterme
root.mainloop()

"""
Bu rapor, Python'un tkinter kütüphanesi kullanılarak oluşturulan basit bir Tic-Tac-Toe oyununu kapsamaktadır. Oyun, iki oyunculu klasik bir strateji oyunu olan Tic-Tac-Toe'nun bilgisayara karşı oynanan bir versiyonudur.

Oyun Mekaniği
Oyun, 3x3'lük bir kare ızgarada oynanır. İki oyuncudan biri "X", diğeri "O" işaretlerini kullanır. Oyunun amacı, sırasıyla işaretlerini yatay, dikey veya çapraz olarak sıralamak olan iki oyuncu arasında gerçekleşir. Bu oyun, kullanıcıya "O" işareti verirken, bilgisayar "X" işareti ile oynamaktadır.

Algoritma
Oyunun yapay zeka kısmı, her iki oyuncu için en iyi hamleleri belirlemek üzere tasarlanmış minimax algoritması kullanmaktadır. Minimax, oyun teorisinde tam bilgiye sahip iki rakip oyuncu arasındaki oyunlar için bir karar kuralları algoritmasıdır. Bu oyun için algoritma, bilgisayarın hamlelerini yönetir ve her zaman en iyi hamleyi seçmeye çalışır.

Kodun Yapısı
İthalatlar
Kod, tkinter ve messagebox modüllerini içe aktararak başlar. Bu, kullanıcı arayüzünü oluşturmak ve kullanıcıya bilgi vermek için gereklidir.

Oyun Tahtası
Oyunun durumu, 3x3'lük bir liste listesi olarak temsil edilir ve her hücre başlangıçta boş bir string (" ") ile doldurulur.

Fonksiyonlar
is_winner: Belirli bir oyuncunun kazanıp kazanmadığını kontrol eder.
get_possible_moves: Boş hücrelerin konumlarını döndürür.
minimax: Oyunun mevcut durumu için en iyi hamleyi ve skoru hesaplar.
on_click: Kullanıcının hamlesini işler ve bilgisayarın hamlesini tetikler.
reset_board: Oyun tahtasını ve butonları başlangıç durumuna sıfırlar.
GUI
Tkinter penceresi oluşturulur ve başlığa "Tic-Tac-Toe" atanır.
Butonlar, oyun tahtası hücrelerini temsil eder ve bir grid yapısına yerleştirilir.
Her buton, on_click fonksiyonunu kendi koordinatları ile çağıracak şekilde ayarlanır.
Sonuç
Bu kod, kullanıcıların "O" olarak oynayabileceği ve bilgisayarın "X" olarak yanıt vereceği etkileşimli bir Tic-Tac-Toe oyunu sağlar. Oyun, bir oyuncu üçlü bir sıra oluşturana veya tüm hücreler dolana kadar devam eder. Oyun sona erdiğinde, kazanan hakkında bir mesaj gösterilir ve tahta sıfırlanır.
"""
