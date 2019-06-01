# Interpretable Machine Learning: PD7

### Czego bot nie zrozumiał?

#### PDP dla `fare`
Wszystkie poniższe teksty poskutkowały narysowaniem PDP dla zmiennej `fare`:

* Please plot PDP for fare
* partial dependence for amount paid 
* ALE plot for fare 

#### Wiek chyba poza zakresem
Wpisałem co następuje: `age 10, fare 0, class 3, give probability` i dostałem odpowiedź `Age in years.` Najprawdopodobniej jest nałożone jakies ograniczenie na wiek, ale 10-latek chyba brzmi sensownie. W takim wypadku jakby dobrze działała komenda `age valid range` czy coś podobnego.

#### Reakcja na komendy bez kontekstu
Wpisanie po prostu `plot` powoduje pokazanie PDP dla wieku, a `breakdown` odpowiedniego wykresu dla Jacka. 

#### Wpisywanie losowych imion powoduje wyświetlenie informacji o Jacku (nawet po wpisaniu Kate Winslet!)

####

### Jakie nowe funkcjonalności?

Po kilkunastominutowej rozmowie z botem mogę zasugerować następujące usprawnienia:

* rysowanie wykresów ALE - bardziej odporne na korelacje między zmiennymi niż PDP,
* sensowna odpowiedź na pytanie `what can you do?`, `what plots can you show?` żeby użytkownik wiedział, jakimi narzędziami dysponuje,
* przyszło mi do głowy pytanie "jak zwiększyć szanse na przeżycie", można by dawać propozycje dla aktualnie wybranych danych np. przy użyciu LIME.