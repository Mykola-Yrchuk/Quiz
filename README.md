# 🎯 Quiz App

Wielojęzyczna gra quizowa stworzona w Pythonie przy użyciu biblioteki Tkinter.

[![Python CI](https://github.com/Mykola-Yrchuk/Quiz/actions/workflows/main.yml/badge.svg)](https://github.com/Mykola-Yrchuk/Quiz/actions/workflows/main.yml)
![Docker Pulls](https://img.shields.io/docker/pulls/beezb/quiz-app)

## 🌍 O projekcie
Quiz App to interaktywna gra edukacyjna, która oferuje zabawę w trzech językach: angielskim, polskim i ukraińskim. Aplikacja zawiera różnorodne kategorie, system czasowy oraz rozbudowany system osiągnięć.

## 🚀 Automatyzacja i CI/CD
Projekt wykorzystuje nowoczesne podejście DevOps:
* **CI (Continuous Integration):** Automatyczne testy jednostkowe uruchamiane przy każdym `push` do gałęzi `main`.
* **CD (Continuous Deployment):** Automatyczne budowanie obrazu Docker i publikacja na Docker Hub po pomyślnym przejściu testów.

## 📚 Funkcje
* **Wsparcie językowe:** Angielski 🇬🇧, Polski 🇵🇱, Ukraiński 🇺🇦.
* **Kategorie:** Matematyka, Natura, Logika, Bajki, Geografia, Sport.
* **Rozgrywka:**
    * Losowe pytania i pozycje odpowiedzi.
    * 10-sekundowy licznik czasu na każde pytanie.
    * Automatyczne pomijanie pytań po upływie czasu.
    * Podsumowanie wyników i system nagród.
* **Interfejs:** Nowoczesny, ciemny design z animacjami przycisków i paskiem postępu.

## 🏆 System Osiągnięć
W zależności od wyniku, gracz może odblokować różne rangi:
🏆 GOD MODE | 🔥 NEAR GENIUS | 👍 GOOD JOB | 🙂 NOT BAD | 😅 KEEP TRYING | 😂 TRY AGAIN BRO

## 🛠️ Technologie
* Python 3.10+
* Tkinter (GUI)
* Docker
* GitHub Actions (CI/CD)

## 🐳 Uruchamianie przez Docker
Aplikacja jest dostępna jako obraz Docker na Docker Hub. Aby pobrać i uruchomić aplikację:

1. Pobierz obraz:
   ```bash
   docker pull beezb/quiz-app:latest
Uruchom kontener:
ff

Bash
docker run -it beezb/quiz-app:latest
Uwaga: Aplikacja GUI wymaga środowiska graficznego do poprawnego wyświetlenia okna.

📄 Licencja
Projekt jest open-source i darmowy do użytku.

Projekt przygotowany na zajęcia z automatyzacji procesów oprogramowania.
