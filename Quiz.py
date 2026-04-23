import tkinter as tk
import random
import time

# ---------------- STYLE ----------------
BG_COLOR = "#1e1e2f"
BTN_COLORS = ["#ff914d", "#4da6ff", "#66cc66"]

# 🔥 УВЕЛИЧЕННЫЕ КНОПКИ
BTN_FONT = ("Arial", 16, "bold")
BTN_WIDTH = 25
BTN_HEIGHT = 2

# ---------------- TIMER ----------------
start_time = 0

def get_time():
    return int(time.time() - start_time)

# ---------------- QUESTIONS ----------------

math_q = [
    {"q": "5 + 3 = ?", "a": "8", "o": ["6", "7", "8", "9"]},
    {"q": "10 - 4 = ?", "a": "6", "o": ["5", "6", "7", "8"]},
    {"q": "2 * 6 = ?", "a": "12", "o": ["10", "11", "12", "13"]},
    {"q": "18 / 3 = ?", "a": "6", "o": ["5", "6", "7", "8"]},
    {"q": "9 + 9 = ?", "a": "18", "o": ["16", "17", "18", "19"]},
    {"q": "7 * 2 = ?", "a": "14", "o": ["12", "13", "14", "15"]},
    {"q": "15 - 7 = ?", "a": "8", "o": ["6", "7", "8", "9"]},
    {"q": "3 * 3 = ?", "a": "9", "o": ["6", "8", "9", "10"]},
    {"q": "20 / 5 = ?", "a": "4", "o": ["3", "4", "5", "6"]},
    {"q": "6 + 6 = ?", "a": "12", "o": ["10", "11", "12", "13"]},
    {"q": "8 + 7 = ?", "a": "15", "o": ["13", "14", "15", "16"]},
    {"q": "9 - 3 = ?", "a": "6", "o": ["5", "6", "7", "8"]},
    {"q": "4 * 4 = ?", "a": "16", "o": ["14", "15", "16", "17"]},
    {"q": "25 / 5 = ?", "a": "5", "o": ["4", "5", "6", "7"]},
    {"q": "11 + 2 = ?", "a": "13", "o": ["12", "13", "14", "15"]},
    {"q": "14 - 6 = ?", "a": "8", "o": ["7", "8", "9", "10"]},
    {"q": "5 * 5 = ?", "a": "25", "o": ["20", "24", "25", "26"]},
    {"q": "30 / 6 = ?", "a": "5", "o": ["4", "5", "6", "7"]},
    {"q": "7 + 6 = ?", "a": "13", "o": ["12", "13", "14", "15"]},
    {"q": "12 - 5 = ?", "a": "7", "o": ["6", "7", "8", "9"]},
]

nature_q = [
    {"q": "Co to jest 🌳?", "a": "Drzewo", "o": ["Kwiat", "Drzewo", "Trawa", "Liść"]},
    {"q": "Co świeci 🌞?", "a": "Słońce", "o": ["Księżyc", "Słońce", "Gwiazda", "Planeta"]},
    {"q": "Gdzie żyją ryby?", "a": "Woda", "o": ["Ląd", "Woda", "Las", "Powietrze"]},
    {"q": "Co pada z nieba?", "a": "Deszcz", "o": ["Wiatr", "Deszcz", "Śnieg", "Mgła"]},
    {"q": "Co jest zielone?", "a": "Trawa", "o": ["Kamień", "Trawa", "Ogień", "Piasek"]},
    {"q": "Co daje tlen?", "a": "Drzewa", "o": ["Kamień", "Drzewa", "Metal", "Plastik"]},
    {"q": "Co rośnie w lesie?", "a": "Drzewa", "o": ["Samochody", "Drzewa", "Domy", "Ulice"]},
    {"q": "Co jest zimne?", "a": "Lód", "o": ["Ogień", "Lód", "Słońce", "Piasek"]},
    {"q": "Co lata?", "a": "Ptak", "o": ["Ryba", "Ptak", "Krowa", "Koń"]},
    {"q": "Co ma liście?", "a": "Drzewo", "o": ["Kamień", "Drzewo", "Metal", "Szkło"]},
    {"q": "Co pije wodę?", "a": "Rośliny", "o": ["Kamienie", "Rośliny", "Metal", "Plastik"]},
    {"q": "Co świeci nocą?", "a": "Księżyc", "o": ["Słońce", "Księżyc", "Drzewo", "Ogień"]},
    {"q": "Co jest mokre?", "a": "Woda", "o": ["Ogień", "Woda", "Kamień", "Piasek"]},
    {"q": "Co jest wysokie?", "a": "Góra", "o": ["Rzeka", "Góra", "Morze", "Łąka"]},
    {"q": "Co żyje w lesie?", "a": "Zwierzęta", "o": ["Samochody", "Zwierzęta", "Komputery", "Telefony"]},
    {"q": "Co daje cień?", "a": "Drzewo", "o": ["Światło", "Drzewo", "Ogień", "Wiatr"]},
    {"q": "Co jest słone?", "a": "Morze", "o": ["Jezioro", "Morze", "Rzeka", "Deszcz"]},
    {"q": "Co jest czerwone w naturze?", "a": "Jabłko", "o": ["Kamień", "Jabłko", "Metal", "Piasek"]},
    {"q": "Co oddycha?", "a": "Zwierzęta", "o": ["Kamienie", "Zwierzęta", "Stół", "Krzesło"]},
    {"q": "Co rośnie?", "a": "Rośliny", "o": ["Metal", "Rośliny", "Plastik", "Szkło"]},
]
logic_q = [
    {"q": "1kg żelaza czy 1kg piór?", "a": "Równe", "o": ["Żelazo", "Pióra", "Równe", "Nie wiem"]},
    {"q": "2,4,6,?", "a": "8", "o": ["7", "8", "9", "10"]},
    {"q": "Dziś poniedziałek, jutro?", "a": "Wtorek", "o": ["Niedziela", "Wtorek", "Środa", "Piątek"]},
    {"q": "Co nie ma końca?", "a": "Koło", "o": ["Linia", "Koło", "Droga", "Książka"]},
    {"q": "Co rośnie bez wody?", "a": "Cień", "o": ["Drzewo", "Cień", "Trawa", "Kwiat"]},
    {"q": "Jeśli 2+2=4 to 4+4=?", "a": "8", "o": ["6", "8", "10", "12"]},
    {"q": "Co jest cięższe?", "a": "Zależy", "o": ["Zawsze A", "Zawsze B", "Zależy", "Nie wiem"]},
    {"q": "Który dzień po piątku?", "a": "Sobota", "o": ["Czwartek", "Sobota", "Niedziela", "Poniedziałek"]},
    {"q": "Co jest większe: 10 czy 100?", "a": "100", "o": ["10", "100", "Równe", "Nie wiem"]},
    {"q": "Co jest logiczne?", "a": "Prawda", "o": ["Fałsz", "Prawda", "Chaos", "Los"]},
    {"q": "1+1=?", "a": "2", "o": ["1", "2", "3", "4"]},
    {"q": "3+3=?", "a": "6", "o": ["5", "6", "7", "8"]},
    {"q": "5-2=?", "a": "3", "o": ["2", "3", "4", "5"]},
    {"q": "10-10=?", "a": "0", "o": ["0", "1", "2", "10"]},
    {"q": "Co jest dalej?", "a": "Nie wiadomo", "o": ["A", "B", "Nie wiadomo", "C"]},
    {"q": "Co jest pierwsze?", "a": "Pytanie", "o": ["Odpowiedź", "Pytanie", "Czas", "Liczba"]},
    {"q": "Czy 2 jest parzyste?", "a": "Tak", "o": ["Tak", "Nie", "Może", "Nie wiem"]},
    {"q": "Czy 3 jest parzyste?", "a": "Nie", "o": ["Tak", "Nie", "Może", "Zawsze"]},
    {"q": "Co jest szybsze?", "a": "Zależy", "o": ["Samolot", "Auto", "Zależy", "Pies"]},
    {"q": "Co jest logiczne w życiu?", "a": "Myślenie", "o": ["Sen", "Myślenie", "Gra", "Los"]},
]

fairy_q = [
    {"q": "Kto spał 100 lat?", "a": "Śpiąca Królewna", "o": ["Elsa", "Kopciuszek", "Śpiąca Królewna", "Anna"]},
    {"q": "Kto zgubił pantofelek?", "a": "Kopciuszek", "o": ["Anna", "Elsa", "Kopciuszek", "Roszpunka"]},
    {"q": "Kto walczy ze smokiem?", "a": "Rycerz", "o": ["Król", "Rycerz", "Kupiec", "Chłop"]},
    {"q": "Kto spełnia życzenia?", "a": "Dżin", "o": ["Elf", "Dżin", "Król", "Czarodziej"]},
    {"q": "Kogo zjadł wilk?", "a": "Kapturek", "o": ["Babcia", "Kapturek", "Kopciuszek", "Król"]},
    {"q": "Kto miał złote włosy?", "a": "Roszpunka", "o": ["Elsa", "Anna", "Roszpunka", "Bella"]},
    {"q": "Kto mieszkał w lesie z krasnoludkami?", "a": "Królewna Śnieżka", "o": ["Kopciuszek", "Śnieżka", "Elsa", "Anna"]},
    {"q": "Kto ma magiczną różdżkę?", "a": "Wróżka", "o": ["Rycerz", "Wróżka", "Król", "Smok"]},
    {"q": "Kto był zły w bajkach?", "a": "Czarownica", "o": ["Król", "Czarownica", "Książę", "Rycerz"]},
    {"q": "Kto ratuje księżniczki?", "a": "Książę", "o": ["Smok", "Książę", "Wilk", "Lis"]},
    {"q": "Kto mieszka w zamku?", "a": "Król", "o": ["Chłop", "Król", "Wilk", "Kot"]},
    {"q": "Kto lata na miotle?", "a": "Czarownica", "o": ["Księżniczka", "Czarownica", "Król", "Elf"]},
    {"q": "Kto jest z bajki o lodzie?", "a": "Elsa", "o": ["Anna", "Elsa", "Bella", "Ariel"]},
    {"q": "Kto żył w morzu?", "a": "Ariel", "o": ["Elsa", "Ariel", "Anna", "Bella"]},
    {"q": "Kto miał siedmiu krasnoludków?", "a": "Śnieżka", "o": ["Elsa", "Śnieżka", "Anna", "Bella"]},
    {"q": "Kto był piękny w bajce?", "a": "Księżniczka", "o": ["Smok", "Księżniczka", "Wilk", "Cień"]},
    {"q": "Kto był odważny?", "a": "Rycerz", "o": ["Król", "Rycerz", "Kot", "Lis"]},
    {"q": "Kto żył w lesie?", "a": "Wilk", "o": ["Wilk", "Król", "Rycerz", "Smok"]},
    {"q": "Kto miał magiczne lustro?", "a": "Czarownica", "o": ["Królewna", "Czarownica", "Rycerz", "Król"]},
    {"q": "Kto był bohaterem?", "a": "Książę", "o": ["Wilk", "Książę", "Smok", "Kot"]},
]

categories = {
    "Matematyka": math_q,
    "Przyroda": nature_q,
    "Logika": logic_q,
    "Bajki": fairy_q
}

# ---------------- APP ----------------

root = tk.Tk()
root.title("Quiz App")
root.geometry("520x650")
root.configure(bg=BG_COLOR)

current_q = 0
score = 0
questions = []
paused = False
start_time = 0
# ---------------- HELPERS ----------------
def clear():
    for w in root.winfo_children():
        w.destroy()

def big_btn(text, cmd, color=None):
    return tk.Button(
        root,
        text=text,
        command=cmd,
        width=BTN_WIDTH,
        height=BTN_HEIGHT,
        font=BTN_FONT,
        bg=color if color else random.choice(BTN_COLORS),
        fg="white",
        relief="flat"
    )

# ---------------- MENU ----------------
def main_menu():
    clear()

    tk.Label(root, text="🎯 QUIZ APP",
             bg=BG_COLOR, fg="white",
             font=("Arial", 26, "bold")).pack(pady=25)

    tk.Label(root, text="Wybierz kategorię",
             bg=BG_COLOR, fg="white",
             font=("Arial", 14)).pack(pady=10)

    for cat in categories:
        big_btn(cat, lambda c=cat: start_quiz(c)).pack(pady=8)

# ---------------- START ----------------
def start_quiz(cat):
    global questions, current_q, score, start_time

    current_q = 0
    score = 0
    start_time = time.time()

    q = categories[cat]
    first = q[:10]
    last = q[10:]
    random.shuffle(last)

    questions = first + last
    show_question()

# ---------------- QUESTION ----------------
def show_question():
    clear()

    if current_q >= len(questions):
        tk.Label(root,
                 text=f"Wynik: {score}/20\nCzas: {get_time()}s",
                 bg=BG_COLOR, fg="white",
                 font=("Arial", 18)).pack(pady=50)

        big_btn("MENU", main_menu).pack()
        return

    q = questions[current_q]

    tk.Button(root, text="⏸",
              command=toggle_pause,
              font=("Arial", 14, "bold")).place(x=470, y=10)

    tk.Label(root, text=q["q"],
             bg=BG_COLOR, fg="white",
             font=("Arial", 18, "bold")).pack(pady=20)

    opts = q["o"].copy()
    random.shuffle(opts)

    for opt in opts:
        big_btn(opt, lambda o=opt: check(o)).pack(pady=6)

# ---------------- CHECK ----------------
def check(ans):
    global current_q, score

    if ans == questions[current_q]["a"]:
        score += 1

    current_q += 1
    show_question()

# ---------------- PAUSE ----------------
def toggle_pause():
    global paused
    paused = not paused

    clear()

    if paused:
        tk.Label(root, text="⏸ PAUZA",
                 bg=BG_COLOR, fg="white",
                 font=("Arial", 24, "bold")).pack(pady=50)

        big_btn("▶ Wznów", toggle_pause).pack(pady=10)
        big_btn("🏠 Menu", main_menu).pack(pady=10)
    else:
        show_question()

# ---------------- START APP ----------------
main_menu()
root.mainloop()