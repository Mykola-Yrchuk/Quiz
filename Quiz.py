import tkinter as tk
from tkinter import ttk
import random
import time

# ---------------- STYLE ----------------
BG_COLOR = "#1e1e2f"
BTN_COLORS = ["#ff914d", "#4da6ff", "#66cc66", "#dc01bb"]
BTN_FONT = ("Arial", 16, "bold")
BTN_WIDTH = 25
BTN_HEIGHT = 2

# ---------------- HELPERS ----------------
def unlock_and_next():
    global can_click
    can_click = True
    show_question()

def get_unique_colors(n):
    colors = BTN_COLORS.copy()
    random.shuffle(colors)
    return [colors[i % len(colors)] for i in range(n)]

progress = None
timer_label = None
# ---------------- APP ----------------
root = tk.Tk()
root.title("Quiz App")
root.geometry("520x720")
root.configure(bg=BG_COLOR)

current_lang = "pl"
current_q, score, start_time = 0, 0, 0
active_questions = []

timer_running = False
stop_timer = False

time_limit = 10
question_start_time = 0
achievements = []

# ---------------- UI ----------------
progress = None
timer_label = None

def clear():
    global progress, timer_label, stop_timer
    stop_timer = True
    for w in root.winfo_children():
        w.destroy()
    progress = None
    timer_label = None

def get_time():
    return int(time.time() - start_time)

def big_btn(text, cmd, color=None):
    base_color = color if color else random.choice(BTN_COLORS)

    btn = tk.Button(
        root,
        text=text,
        command=cmd,
        width=BTN_WIDTH,
        height=BTN_HEIGHT,
        font=BTN_FONT,
        bg=base_color,
        fg="white",
        relief="flat",
        activebackground=base_color
    )

    def on_enter(e):
        btn.config(bg="#2c2c3a")

    def on_leave(e):
        btn.config(bg=base_color)

    btn.bind("<Enter>", on_enter)
    btn.bind("<Leave>", on_leave)

    return btn

# ---------------- TIMER ----------------
def start_question_timer():
    global question_start_time, timer_running, stop_timer

    stop_timer = False
    timer_running = True
    question_start_time = time.time()

    update_timer()

    if not timer_running:
        timer_running = True
        update_timer()


def update_timer():
    global progress

    if stop_timer:
        return

    if current_q >= len(active_questions):
        return

    elapsed = int(time.time() - question_start_time)
    remaining = max(0, time_limit - elapsed)

    if timer_label:
        timer_label.config(text=f"Time: {remaining}s")

    if progress:
        progress["value"] = (current_q / len(active_questions)) * 100
        progress.update_idletasks()

    if elapsed >= time_limit:
        auto_fail()
        return

    root.after(1000, update_timer)


def auto_fail():
    global current_q
    current_q += 1
    show_question()
    start_question_timer()

# ---------------- ACHIEVEMENTS ----------------
def give_achievement():
    global achievements

    if current_lang == "en":
        if score == len(active_questions):
            achievements.append("🏆 GOD MODE")
        elif score >= len(active_questions) * 0.8:
            achievements.append("🔥 NEAR GENIUS")
        elif score >= len(active_questions) * 0.6:
            achievements.append("👍 GOOD JOB")
        elif score >= len(active_questions) * 0.4:
            achievements.append("🙂 NOT BAD")
        elif score > 0:
            achievements.append("😅 KEEP TRYING")
        else:
            achievements.append("😂 TRY AGAIN BRO")

    elif current_lang == "pl":
        if score == len(active_questions):
            achievements.append("🏆 BOS QUIZU")
        elif score >= len(active_questions) * 0.8:
            achievements.append("🔥 PRAWIE GENIUSZ")
        elif score >= len(active_questions) * 0.6:
            achievements.append("👍 DOBRA ROBOTA")
        elif score >= len(active_questions) * 0.4:
            achievements.append("🙂 NIEŹLE")
        elif score > 0:
            achievements.append("😅 ĆWICZ DALEJ")
        else:
            achievements.append("😂 SPRÓBUJ JESZCZE RAZ")

    elif current_lang == "ua":
        if score == len(active_questions):
            achievements.append("🏆 БОГ КВІЗУ")
        elif score >= len(active_questions) * 0.8:
            achievements.append("🔥 МАЙЖЕ ГЕНІЙ")
        elif score >= len(active_questions) * 0.6:
            achievements.append("👍 ДОБРА РОБОТА")
        elif score >= len(active_questions) * 0.4:
            achievements.append("🙂 НЕПЛОХО")
        elif score > 0:
            achievements.append("😅 ТРЕНУЙСЯ ДАЛІ")
        else:
            achievements.append("😂 СПРОБУЙ ЩЕ РАЗ")

# ---------------- TEXT ----------------
LANG_TEXT = {
    "pl": {"title": "🎯 QUIZ APP", "select_cat": "Wybierz kategorię",
           "score": "Wynik", "time": "Czas", "menu": "MENU"},
    "en": {"title": "🎯 QUIZ APP", "select_cat": "Select Category",
           "score": "Score", "time": "Time", "menu": "MENU"},
    "ua": {"title": "🎯 КВІЗ", "select_cat": "Оберіть категорію",
           "score": "Результат", "time": "Час", "menu": "МЕНЮ"}
}

# ---------------- QUESTIONS ----------------
math_12 = [
    {"q": "5 + 3 = ?", "a": "8", "o": ["6", "7", "8", "9"]},
    {"q": "10 - 4 = ?", "a": "6", "o": ["5", "6", "7", "8"]},
    {"q": "2 * 6 = ?", "a": "12", "o": ["10", "11", "12", "13"]},
    {"q": "18 / 3 = ?", "a": "6", "o": ["5", "6", "7", "8"]},
    {"q": "9 + 9 = ?", "a": "18", "o": ["16", "17", "18", "19"]},
    {"q": "25 / 5 = ?", "a": "5", "o": ["4", "5", "6", "7"]},
    {"q": "12 * 2 = ?", "a": "24", "o": ["22", "24", "26", "28"]},
    {"q": "100 - 50 = ?", "a": "50", "o": ["40", "50", "60", "70"]},
    {"q": "7 * 3 = ?", "a": "21", "o": ["20", "21", "22", "23"]},
    {"q": "81 / 9 = ?", "a": "9", "o": ["7", "8", "9", "10"]},
    {"q": "15 + 15 = ?", "a": "30", "o": ["25", "30", "35", "40"]},
    {"q": "6 * 4 = ?", "a": "24", "o": ["20", "22", "24", "26"]}
]

nature_pl = [
    {"q": "Co to jest 🌳?", "a": "Drzewo", "o": ["Kwiat", "Drzewo", "Trawa", "Liść"]}, {"q": "Co świeci 🌞?", "a": "Słońce", "o": ["Księżyc", "Słońce", "Gwiazda", "Planeta"]},
    {"q": "Gdzie żyją ryby?", "a": "Woda", "o": ["Ląd", "Woda", "Las", "Powietrze"]}, {"q": "Co pada z nieba?", "a": "Deszcz", "o": ["Wiatr", "Deszcz", "Śnieg", "Mgła"]},
    {"q": "Co jest zielone?", "a": "Trawa", "o": ["Kamień", "Trawa", "Ogień", "Piasek"]}, {"q": "Co daje tlen?", "a": "Drzewa", "o": ["Kamień", "Drzewa", "Metal", "Plastik"]},
    {"q": "Co jest zimne?", "a": "Lód", "o": ["Ogień", "Lód", "Słońce", "Piasek"]}, {"q": "Co lata?", "a": "Ptak", "o": ["Ryba", "Ptak", "Krowa", "Koń"]},
    {"q": "Co jest wysokie?", "a": "Góra", "o": ["Rzeka", "Góra", "Morze", "Łąka"]}, {"q": "Co jest mokre?", "a": "Woda", "o": ["Ogień", "Woda", "Kamień", "Sucho"]},
    {"q": "Co ma piasek?", "a": "Pustynia", "o": ["Las", "Pustynia", "Rzeka", "Góra"]}, {"q": "Co ma płatki?", "a": "Kwiat", "o": ["Kamień", "Kwiat", "Metal", "Woda"]}
]
nature_en = [
    {"q": "What is this 🌳?", "a": "Tree", "o": ["Flower", "Tree", "Grass", "Leaf"]}, {"q": "What shines 🌞?", "a": "Sun", "o": ["Moon", "Sun", "Star", "Planet"]},
    {"q": "Where do fish live?", "a": "Water", "o": ["Land", "Water", "Forest", "Air"]}, {"q": "What falls from sky?", "a": "Rain", "o": ["Wind", "Rain", "Snow", "Fog"]},
    {"q": "What is green?", "a": "Grass", "o": ["Stone", "Grass", "Fire", "Sand"]}, {"q": "What gives oxygen?", "a": "Trees", "o": ["Stone", "Trees", "Metal", "Plastic"]},
    {"q": "What is cold?", "a": "Ice", "o": ["Fire", "Ice", "Sun", "Sand"]}, {"q": "What flies?", "a": "Bird", "o": ["Fish", "Bird", "Cow", "Horse"]},
    {"q": "What is high?", "a": "Mountain", "o": ["River", "Mountain", "Sea", "Meadow"]}, {"q": "What is wet?", "a": "Water", "o": ["Fire", "Water", "Stone", "Dry"]},
    {"q": "What has sand?", "a": "Desert", "o": ["Forest", "Desert", "River", "Mountain"]}, {"q": "What has petals?", "a": "Flower", "o": ["Stone", "Flower", "Metal", "Water"]}
]
nature_ua = [
    {"q": "Що це 🌳?", "a": "Дерево", "o": ["Квітка", "Дерево", "Трава", "Листок"]}, {"q": "Що світить 🌞?", "a": "Сонце", "o": ["Місяць", "Сонце", "Зоря", "Планета"]},
    {"q": "Де живуть риби?", "a": "Вода", "o": ["Суша", "Вода", "Ліс", "Повітря"]}, {"q": "Що падає з неба?", "a": "Дощ", "o": ["Вітер", "Дощ", "Сніг", "Туман"]},
    {"q": "Що зелене?", "a": "Трава", "o": ["Камінь", "Трава", "Вогонь", "Пісок"]}, {"q": "Що дає кисень?", "a": "Дерева", "o": ["Камінь", "Дерева", "Метал", "Пластик"]},
    {"q": "Що холодне?", "a": "Лід", "o": ["Вогонь", "Лід", "Сонце", "Пісок"]}, {"q": "Хто літає?", "a": "Птах", "o": ["Риба", "Птах", "Корова", "Кінь"]},
    {"q": "Що високе?", "a": "Гора", "o": ["Річка", "Гора", "Море", "Луг"]}, {"q": "Що мокре?", "a": "Вода", "o": ["Вогонь", "Вода", "Камінь", "Сухо"]},
    {"q": "Де багато піску?", "a": "Пустеля", "o": ["Ліс", "Пустеля", "Річка", "Гора"]}, {"q": "Що має пелюстки?", "a": "Квітка", "o": ["Камінь", "Квітка", "Метал", "Вода"]}
]

# Логика
logic_pl = [
    {"q": "1kg żelaza czy 1kg piór?", "a": "Równe", "o": ["Żelazo", "Pióra", "Równe", "Nie wiem"]}, {"q": "2,4,6,?", "a": "8", "o": ["7", "8", "9", "10"]},
    {"q": "Dziś poniedziałek, jutro?", "a": "Wtorek", "o": ["Niedziela", "Wtorek", "Środa", "Piątek"]}, {"q": "Co nie ma końca?", "a": "Koło", "o": ["Linia", "Koło", "Droga", "Książka"]},
    {"q": "Co rośnie bez wody?", "a": "Cień", "o": ["Drzewo", "Cień", "Trawa", "Kwiat"]}, {"q": "Jeśli 2+2=4 to 4+4=?", "a": "8", "o": ["6", "8", "10", "12"]},
    {"q": "Który dzień po piątku?", "a": "Sobota", "o": ["Czwartek", "Sobota", "Niedziela", "Poniedziałek"]}, {"q": "Co jest większe: 10 czy 100?", "a": "100", "o": ["10", "100", "Równe", "Nie wiem"]},
    {"q": "1+1=?", "a": "2", "o": ["1", "2", "3", "4"]}, {"q": "Co jest szybsze?", "a": "Zależy", "o": ["Samolot", "Auto", "Zależy", "Pies"]},
    {"q": "Czy 2 jest parzyste?", "a": "Tak", "o": ["Tak", "Nie", "Może", "Nie wiem"]}, {"q": "Ile to 10-10?", "a": "0", "o": ["0", "1", "10", "20"]}
]
logic_en = [
    {"q": "1kg iron or 1kg feathers?", "a": "Equal", "o": ["Iron", "Feathers", "Equal", "Don't know"]}, {"q": "2,4,6,?", "a": "8", "o": ["7", "8", "9", "10"]},
    {"q": "Today Monday, tomorrow?", "a": "Tuesday", "o": ["Sunday", "Tuesday", "Wednesday", "Friday"]}, {"q": "What has no end?", "a": "Circle", "o": ["Line", "Circle", "Road", "Book"]},
    {"q": "What grows without water?", "a": "Shadow", "o": ["Tree", "Shadow", "Grass", "Flower"]}, {"q": "If 2+2=4 then 4+4=?", "a": "8", "o": ["6", "8", "10", "12"]},
    {"q": "Day after Friday?", "a": "Saturday", "o": ["Thursday", "Saturday", "Sunday", "Monday"]}, {"q": "Which is bigger: 10 or 100?", "a": "100", "o": ["10", "100", "Equal", "Don't know"]},
    {"q": "1+1=?", "a": "2", "o": ["1", "2", "3", "4"]}, {"q": "What is faster?", "a": "Depends", "o": ["Plane", "Car", "Depends", "Dog"]},
    {"q": "Is 2 even?", "a": "Yes", "o": ["Yes", "No", "Maybe", "Don't know"]}, {"q": "What is 10-10?", "a": "0", "o": ["0", "1", "10", "20"]}
]
logic_ua = [
    {"q": "1кг заліза чи 1кг пір'я?", "a": "Однаково", "o": ["Залізо", "Пір'я", "Однаково", "Не знаю"]}, {"q": "2,4,6,?", "a": "8", "o": ["7", "8", "9", "10"]},
    {"q": "Сьогодні понеділок, завтра?", "a": "Вівторок", "o": ["Неділя", "Вівторок", "Середа", "П'ятниця"]}, {"q": "Що не має кінця?", "a": "Коло", "o": ["Лінія", "Коло", "Дорога", "Книга"]},
    {"q": "Що росте без води?", "a": "Тінь", "o": ["Дерево", "Тінь", "Трава", "Квітка"]}, {"q": "Якщо 2+2=4 то 4+4=?", "a": "8", "o": ["6", "8", "10", "12"]},
    {"q": "Який день після п'ятниці?", "a": "Субота", "o": ["Четвер", "Субота", "Неділя", "Понеділок"]}, {"q": "Що більше: 10 чи 100?", "a": "100", "o": ["10", "100", "Однаково", "Не знаю"]},
    {"q": "1+1=?", "a": "2", "o": ["1", "2", "3", "4"]}, {"q": "Що швидше?", "a": "Залежить", "o": ["Літак", "Авто", "Залежить", "Собака"]},
    {"q": "2 - парне число?", "a": "Так", "o": ["Так", "Ні", "Можливо", "Не знаю"]}, {"q": "Скільки буде 10-10?", "a": "0", "o": ["0", "1", "10", "20"]}
]

# Сказки
fairy_pl = [
    {"q": "Kto spał 100 lat?", "a": "Śpiąca Królewna", "o": ["Elsa", "Kopciuszek", "Śpiąca Królewna", "Anna"]}, {"q": "Kto zgubił pantofelek?", "a": "Kopciuszek", "o": ["Anna", "Elsa", "Kopciuszek", "Roszpunka"]},
    {"q": "Kto walczy ze smokiem?", "a": "Rycerz", "o": ["Król", "Rycerz", "Kupiec", "Chłop"]}, {"q": "Kto spełnia życzenia?", "a": "Dżin", "o": ["Elf", "Dżin", "Król", "Czarodziej"]},
    {"q": "Kogo zjadł wilk?", "a": "Kapturek", "o": ["Babcia", "Kapturek", "Kopciuszek", "Król"]}, {"q": "Kto miał złote włosy?", "a": "Roszpunka", "o": ["Elsa", "Anna", "Roszpunka", "Bella"]},
    {"q": "Kto mieszkał z krasnoludkami?", "a": "Śnieżka", "o": ["Kopciuszek", "Śnieżka", "Elsa", "Anna"]}, {"q": "Kto ma magiczną różdżkę?", "a": "Wróżka", "o": ["Rycerz", "Wróżka", "Król", "Smok"]},
    {"q": "Kto lata na miotle?", "a": "Czarownica", "o": ["Księżniczka", "Czarownica", "Król", "Elf"]}, {"q": "Kto żył w morzu?", "a": "Ariel", "o": ["Elsa", "Ariel", "Anna", "Bella"]},
    {"q": "Kto jest z lodu?", "a": "Elsa", "o": ["Anna", "Elsa", "Bella", "Ariel"]}, {"q": "Kto ma długi nos?", "a": "Pinokio", "o": ["Shrek", "Pinokio", "Kot", "Wilk"]}
]
fairy_en = [
    {"q": "Who slept 100 years?", "a": "Sleeping Beauty", "o": ["Elsa", "Cinderella", "Sleeping Beauty", "Anna"]}, {"q": "Who lost a slipper?", "a": "Cinderella", "o": ["Anna", "Elsa", "Cinderella", "Rapunzel"]},
    {"q": "Who fights dragons?", "a": "Knight", "o": ["King", "Knight", "Merchant", "Peasant"]}, {"q": "Who grants wishes?", "a": "Genie", "o": ["Elf", "Genie", "King", "Wizard"]},
    {"q": "Who was eaten by wolf?", "a": "Little Red", "o": ["Grandma", "Little Red", "Cinderella", "King"]}, {"q": "Who had long gold hair?", "a": "Rapunzel", "o": ["Elsa", "Anna", "Rapunzel", "Bella"]},
    {"q": "Who lived with dwarfs?", "a": "Snow White", "o": ["Cinderella", "Snow White", "Elsa", "Anna"]}, {"q": "Who has a magic wand?", "a": "Fairy", "o": ["Knight", "Fairy", "King", "Dragon"]},
    {"q": "Who flies on a broom?", "a": "Witch", "o": ["Princess", "Witch", "King", "Elf"]}, {"q": "Who lived in the sea?", "a": "Ariel", "o": ["Elsa", "Ariel", "Anna", "Bella"]},
    {"q": "Who is from ice?", "a": "Elsa", "o": ["Anna", "Elsa", "Bella", "Ariel"]}, {"q": "Who has a long nose?", "a": "Pinocchio", "o": ["Shrek", "Pinocchio", "Cat", "Wolf"]}
]
fairy_ua = [
    {"q": "Хто спав 100 років?", "a": "Спляча красуня", "o": ["Ельза", "Попелюшка", "Спляча красуня", "Анна"]}, {"q": "Хто загубив черевичок?", "a": "Попелюшка", "o": ["Анна", "Ельза", "Попелюшка", "Рапунцель"]},
    {"q": "Хто б'ється з драконом?", "a": "Лицар", "o": ["Король", "Лицар", "Купець", "Селянин"]}, {"q": "Хто виконує бажання?", "a": "Джин", "o": ["Ельф", "Джин", "Король", "Чарівник"]},
    {"q": "Кого з'їв вовк?", "a": "Червона Шапочка", "o": ["Бабуся", "Червона Шапочка", "Попелюшка", "Король"]}, {"q": "Хто мав золоте волосся?", "a": "Рапунцель", "o": ["Ельза", "Анна", "Рапунцель", "Белла"]},
    {"q": "Хто жив з гномами?", "a": "Білосніжка", "o": ["Попелюшка", "Білосніжка", "Ельза", "Анна"]}, {"q": "Хто має чарівну паличку?", "a": "Фея", "o": ["Лицар", "Фея", "Король", "Дракон"]},
    {"q": "Хто літає на мітлі?", "a": "Відьма", "o": ["Принцеса", "Відьма", "Король", "Ельф"]}, {"q": "Хто жив у морі?", "a": "Аріель", "o": ["Ельза", "Аріель", "Анна", "Белла"]},
    {"q": "Хто з льоду?", "a": "Ельза", "o": ["Анна", "Ельза", "Белла", "Аріель"]}, {"q": "У кого довгий ніс?", "a": "Піноккіо", "o": ["Шрек", "Піноккіо", "Кіт", "Вовк"]}
]

# География
geo_pl = [
    {"q": "Stolica Polski?", "a": "Warszawa", "o": ["Kraków", "Warszawa", "Gdańsk", "Poznań"]}, {"q": "Największy ocean?", "a": "Spokojny", "o": ["Atlantycki", "Indyjski", "Spokojny", "Arktyczny"]},
    {"q": "Gdzie jest Wieża Eiffla?", "a": "Francja", "o": ["Włochy", "Francja", "Niemcy", "Hiszpania"]}, {"q": "Najwyższa góra?", "a": "Everest", "o": ["K2", "Everest", "Rysy", "Mont Blanc"]},
    {"q": "Najdłuższa rzeka?", "a": "Nil", "o": ["Wisła", "Nil", "Amazonka", "Dunaj"]}, {"q": "Stolica Japonii?", "a": "Tokio", "o": ["Pekin", "Seul", "Tokio", "Bangkok"]},
    {"q": "Największy las?", "a": "Amazonia", "o": ["Tajga", "Amazonia", "Białowieża", "Dżungla"]}, {"q": "Stolica Włoch?", "a": "Rzym", "o": ["Mediolan", "Wenecja", "Rzym", "Neapol"]},
    {"q": "Największa pustynia?", "a": "Sahara", "o": ["Gobi", "Sahara", "Atakama", "Kalahari"]}, {"q": "Najmniejszy kontynent?", "a": "Australia", "o": ["Europa", "Australia", "Azja", "Afryka"]},
    {"q": "Stolica USA?", "a": "Waszyngton", "o": ["Nowy Jork", "Waszyngton", "L.A.", "Chicago"]}, {"q": "Gdzie jest Wielki Mur?", "a": "Chiny", "o": ["Indie", "Chiny", "Japonia", "Rosja"]}
]
geo_en = [
    {"q": "Capital of Poland?", "a": "Warsaw", "o": ["Krakow", "Warsaw", "Gdansk", "Poznan"]}, {"q": "Largest ocean?", "a": "Pacific", "o": ["Atlantic", "Indian", "Pacific", "Arctic"]},
    {"q": "Where is the Eiffel Tower?", "a": "France", "o": ["Italy", "France", "Germany", "Spain"]}, {"q": "Highest mountain?", "a": "Everest", "o": ["K2", "Everest", "Rysy", "Mont Blanc"]},
    {"q": "Longest river?", "a": "Nile", "o": ["Vistula", "Nile", "Amazon", "Danube"]}, {"q": "Capital of Japan?", "a": "Tokyo", "o": ["Beijing", "Seoul", "Tokyo", "Bangkok"]},
    {"q": "Largest rainforest?", "a": "Amazon", "o": ["Taiga", "Amazon", "Congo", "Jungle"]}, {"q": "Capital of Italy?", "a": "Rome", "o": ["Milan", "Venice", "Rome", "Naples"]},
    {"q": "Largest desert?", "a": "Sahara", "o": ["Gobi", "Sahara", "Atakama", "Kalahari"]}, {"q": "Smallest continent?", "a": "Australia", "o": ["Europe", "Australia", "Asia", "Africa"]},
    {"q": "Capital of USA?", "a": "Washington", "o": ["New York", "Washington", "L.A.", "Chicago"]}, {"q": "Where is the Great Wall?", "a": "China", "o": ["India", "China", "Japan", "Russia"]}
]
geo_ua = [
    {"q": "Столиця Польщі?", "a": "Варшава", "o": ["Краків", "Варшава", "Гданськ", "Познань"]}, {"q": "Найбільший океан?", "a": "Тихий", "o": ["Атлантичний", "Індійський", "Тихий", "Арктичний"]},
    {"q": "Де Ейфелева вежа?", "a": "Франція", "o": ["Італія", "Франція", "Німеччина", "Іспанія"]}, {"q": "Найвища гора?", "a": "Еверест", "o": ["К2", "Еверест", "Говерла", "Монблан"]},
    {"q": "Найдовша річка?", "a": "Ніл", "o": ["Дніпро", "Ніл", "Амазонка", "Дунай"]}, {"q": "Столиця Японії?", "a": "Токіо", "o": ["Пекін", "Сеул", "Токіо", "Бангкок"]},
    {"q": "Найбільший ліс?", "a": "Амазонія", "o": ["Тайга", "Амазонія", "Полісся", "Джунглі"]}, {"q": "Столиця Італії?", "a": "Рим", "o": ["Мілан", "Венеція", "Рим", "Неаполь"]},
    {"q": "Найбільша пустеля?", "a": "Сахара", "o": ["Гобі", "Сахара", "Атакама", "Калахарі"]}, {"q": "Найменший континент?", "a": "Австралія", "o": ["Європа", "Австралія", "Азія", "Африка"]},
    {"q": "Столиця США?", "a": "Вашингтон", "o": ["Нью-Йорк", "Вашингтон", "Л.А.", "Чикаго"]}, {"q": "Де Великий мур?", "a": "Китай", "o": ["Індія", "Китай", "Японія", "Росія"]}
]

# Спорт
sport_pl = [
    {"q": "Ile trwa połowa meczu piłki nożnej?", "a": "45 min", "o": ["30 min", "45 min", "60 min", "90 min"]}, {"q": "W jakim sporcie jest rakieta?", "a": "Tenis", "o": ["Boks", "Tenis", "Golf", "Hokej"]},
    {"q": "Ile kół ma flaga olimpijska?", "a": "5", "o": ["3", "5", "6", "7"]}, {"q": "Ilu graczy w drużynie piłkarskiej?", "a": "11", "o": ["7", "9", "11", "12"]},
    {"q": "Ilu graczy w koszykówce?", "a": "5", "o": ["5", "6", "10", "11"]}, {"q": "Gdzie odbywa się boks?", "a": "Ring", "o": ["Boisko", "Ring", "Basen", "Kort"]},
    {"q": "Dystans maratonu?", "a": "42 km", "o": ["10 km", "21 km", "42 km", "100 km"]}, {"q": "W czym pływamy?", "a": "Basen", "o": ["Kort", "Basen", "Bieżnia", "Ring"]},
    {"q": "W co gra się krążkiem?", "a": "Hokej", "o": ["Piłka nożna", "Hokej", "Rugby", "Tenis"]}, {"q": "Co to jest 'szach-mat'?", "a": "Szachy", "o": ["Warcaby", "Szachy", "Karty", "Poker"]},
    {"q": "W co gra się przez siatkę rękami?", "a": "Siatkówka", "o": ["Tenis", "Siatkówka", "Piłka", "Golf"]}, {"q": "Najszybszy wyścig samochodowy?", "a": "F1", "o": ["Rajdy", "F1", "NASCAR", "Karting"]}
]
sport_en = [
    {"q": "How long is a football half?", "a": "45 min", "o": ["30 min", "45 min", "60 min", "90 min"]}, {"q": "Which sport uses a racket?", "a": "Tennis", "o": ["Boxing", "Tennis", "Golf", "Hockey"]},
    {"q": "How many rings on Olympic flag?", "a": "5", "o": ["3", "5", "6", "7"]}, {"q": "How many players in a football team?", "a": "11", "o": ["7", "9", "11", "12"]},
    {"q": "How many players in basketball?", "a": "5", "o": ["5", "6", "10", "11"]}, {"q": "Where does boxing happen?", "a": "Ring", "o": ["Field", "Ring", "Pool", "Court"]},
    {"q": "Marathon distance?", "a": "42 km", "o": ["10 km", "21 km", "42 km", "100 km"]}, {"q": "Where do we swim?", "a": "Pool", "o": ["Court", "Pool", "Track", "Ring"]},
    {"q": "Which sport uses a puck?", "a": "Hockey", "o": ["Football", "Hockey", "Rugby", "Tennis"]}, {"q": "What is 'checkmate'?", "a": "Chess", "o": ["Checkers", "Chess", "Cards", "Poker"]},
    {"q": "Played over a net with hands?", "a": "Volleyball", "o": ["Tennis", "Volleyball", "Football", "Golf"]}, {"q": "Fastest car race?", "a": "F1", "o": ["Rally", "F1", "NASCAR", "Karting"]}
]
sport_ua = [
    {"q": "Скільки триває тайм у футболі?", "a": "45 хв", "o": ["30 хв", "45 хв", "60 хв", "90 хв"]}, {"q": "У якому спорті ракетка?", "a": "Теніс", "o": ["Бокс", "Теніс", "Гольф", "Хокей"]},
    {"q": "Скільки кілець на прапорі олімпіади?", "a": "5", "o": ["3", "5", "6", "7"]}, {"q": "Скільки гравців у футбольній команді?", "a": "11", "o": ["7", "9", "11", "12"]},
    {"q": "Скільки гравців у баскетболі?", "a": "5", "o": ["5", "6", "10", "11"]}, {"q": "Де боксують?", "a": "Ринг", "o": ["Поле", "Ринг", "Басейн", "Корт"]},
    {"q": "Дистанція марафону?", "a": "42 км", "o": ["10 км", "21 км", "42 км", "100 км"]}, {"q": "Де ми плаваємо?", "a": "Басейн", "o": ["Корт", "Басейн", "Трек", "Ринг"]},
    {"q": "У чому використовують шайбу?", "a": "Хокей", "o": ["Футбол", "Хокей", "Регбі", "Теніс"]}, {"q": "Що таке 'шах і мат'?", "a": "Шахи", "o": ["Шашки", "Шахи", "Карти", "Покер"]},
    {"q": "Грають через сітку руками?", "a": "Волейбол", "o": ["Теніс", "Волейбол", "Футбол", "Гольф"]}, {"q": "Найшвидші автоперегони?", "a": "Ф1", "o": ["Ралі", "Ф1", "NASCAR", "Карти"]}
]
questions_data = {
    "pl": {"Matematyka": math_12, "Przyroda": nature_pl, "Logika": logic_pl, "Bajki": fairy_pl, "Geografia": geo_pl, "Sport": sport_pl},
    "en": {"Math": math_12, "Nature": nature_en, "Logic": logic_en, "Fairy Tales": fairy_en, "Geography": geo_en, "Sports": sport_en},
    "ua": {"Математика": math_12, "Природа": nature_ua, "Логіка": logic_ua, "Казки": fairy_ua, "Географія": geo_ua, "Спорт": sport_ua}
}

# ---------------- SCREENS ----------------
def language_selection():
    clear()
    tk.Label(root, text="Select Language",
             bg=BG_COLOR, fg="white",
             font=("Arial", 20, "bold")).pack(pady=40)

    langs = [("English 🇬🇧", "en"),
             ("Polski 🇵🇱", "pl"),
             ("Українська 🇺🇦", "ua")]

    colors = get_unique_colors(len(langs))

    def add(i):
        if i >= len(langs):
            return
        text, code = langs[i]
        big_btn(text, lambda c=code: set_language(c),
                color=colors[i]).pack(pady=10)
        root.after(120, lambda: add(i + 1))

    add(0)

def set_language(lang):
    global current_lang
    current_lang = lang
    main_menu()

def main_menu():
    clear()
    texts = LANG_TEXT[current_lang]

    tk.Label(root, text=texts["title"],
             bg=BG_COLOR, fg="white",
             font=("Arial", 26, "bold")).pack(pady=25)

    tk.Label(root, text=texts["select_cat"],
             bg=BG_COLOR, fg="white",
             font=("Arial", 14)).pack(pady=10)

    cats = list(questions_data[current_lang].keys())
    colors = get_unique_colors(len(cats))

    def add(i):
        if i >= len(cats):
            return
        cat = cats[i]
        big_btn(cat, lambda c=cat: start_quiz(c),
                color=colors[i]).pack(pady=5)
        root.after(120, lambda: add(i + 1))

    add(0)

    tk.Button(root, text="🌐 Language",
              command=language_selection,
              bg="#444", fg="white").pack(side="bottom", pady=20)

def start_quiz(cat):
    global active_questions, current_q, score, start_time, achievements

    current_q, score = 0, 0
    achievements = []
    start_time = time.time()

    active_questions = list(questions_data[current_lang][cat])
    random.shuffle(active_questions)

    show_question()
    start_question_timer()

def show_question():
    global progress, timer_label, stop_timer
    stop_timer = False

    clear()
    texts = LANG_TEXT[current_lang]


    bar_frame = tk.Frame(root, bg=BG_COLOR)
    bar_frame.pack(fill="x", padx=20, pady=10)

    progress = ttk.Progressbar(
        bar_frame,
        length=400,
        mode="determinate",
        maximum=100
    )
    progress.pack(fill="x")

    progress["value"] = (current_q / len(active_questions)) * 100
    timer_label = tk.Label(root, text="Time: 10s", bg=BG_COLOR, fg="white", font=("Arial", 14))
    timer_label.pack(pady=5)

    style = ttk.Style()
    style.theme_use("default")

    style.configure("TProgressbar",
                    thickness=20,
                    background="#4da6ff",
                    troughcolor="#2c2c3a",
                    bordercolor="#2c2c3a")

    if current_q >= len(active_questions):
        give_achievement()

        tk.Label(root,
                 text=f"{texts['score']}: {score}/{len(active_questions)}\n{texts['time']}: {get_time()}s",
                 bg=BG_COLOR, fg="white",
                 font=("Arial", 18)).pack(pady=20)

        if achievements:
            tk.Label(root,
                     text="Achievements:\n" + "\n".join(achievements),
                     bg=BG_COLOR, fg="yellow",
                     font=("Arial", 14)).pack(pady=10)

        big_btn(texts["menu"], main_menu).pack()
        return

    q = active_questions[current_q]

    tk.Label(root, text=q["q"],
             bg=BG_COLOR, fg="white",
             font=("Arial", 18, "bold")).pack(pady=40)

    opts = q["o"].copy()
    random.shuffle(opts)
    colors = get_unique_colors(len(opts))

    def add(i):
        if i >= len(opts):
            return
        opt = opts[i]
        big_btn(opt, lambda o=opt: check(o),
                color=colors[i]).pack(pady=6)
        root.after(80, lambda: add(i + 1))

    add(0)

def check(ans):
    global current_q, score

    if current_q >= len(active_questions):
        return

    if ans == active_questions[current_q]["a"]:
        score += 1

    current_q += 1
    if progress:
        progress["value"] = (current_q / len(active_questions)) * 100
    show_question()
    start_question_timer()

# ---------------- START ----------------
language_selection()
root.mainloop()
