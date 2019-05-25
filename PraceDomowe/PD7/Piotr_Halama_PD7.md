# Praca domowa nr 7
Autor: Piotr Halama

W ramach zadania przeprowadziłem krótką rozmowę z botem wyjaśniającym model wytrenowany na danych o przeżyciu na Tytaniku. Bot potrafi powiedzieć jaki model był wytrenowany, wymienić zmienne, wyświetlić wykresy Ceteris Paribus i Breakdown (nawet dla pytań, które nie proszą o nie bezpośrednio).

## Czego bot nie zrozumiał?
- Bot nie odpowiada w jednolity sposób:

    > 👨: What are chances of survival for 25 year old man
    >
    > 🤖: Your chance of survival equals 0.4344. It's close to a toss of a coin!
    >
    > 👨: Show me a plot of chances for 25 year old man
    >
    > 🤖: I'm sorry. It looks like you would've died on Titanic. Your chance of survival equals 0.2551

- Zapytany o histogram wieku w zbiorze danych wyświetla wykres Ceteris Paribus.
- Nie jest w stanie opowiedzieć o tym, jakie metody potrafi użyć w wyjaśnianiu modelu.
- Nie jest w stanie wyjaśnić metody, której używa w wyjaśnianiu:

   > 👨: Explain to me, how does Ceteris Paribus work?
   >
   > 🤖: Sorry, I don't understand yet. But I'll learn from this conversation and improve in the future!

  W tym przypadku przynajmniej przyznaje się do braku wiedzy.

## Jakie dodatkowe intencje powinien bot rozumieć?

- Powinien mieć możliwość rysowania większej ilości wykresów (ALE, LIME).
- Wyświetlać drzewo klasyfikacyjne wytrenowane jako model zastępczy.
- Przydatne byłyby odpowiedzi na pytania o sam zbiór danych (np. histogram wartości).
- Dodatkowo, bot mógłby opowiedzieć jak dobrze model jest wytrenowany. Teraz nie wiemy, czy analizujemy wyniki modelu, który jest dobrze wytrenowany, czy też nie. Oczywiście, ta informacja byłaby przydatna w przypadku, gdy bot sam trenuje model (AutoML) i prezentuje nam swoje wyniki.
- Zadając pytania botowi, pytamy z zasady o sytuacje kontrfaktywne - nikt z nas nie był na Tytaniku.
  Mimo to, bot opowiada tylko o "Twoich" szansach przeżycia - co jeśli pytam o szanse kogoś innego?
