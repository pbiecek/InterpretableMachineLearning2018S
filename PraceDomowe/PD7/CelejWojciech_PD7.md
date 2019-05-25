## Wyjaśnialne Uczenie Maszynowe - PD7

### Wojciech Celej

### Czego bot nie zrozumiał?

* Po wybraniu ścieżki Jacka, i wpisaniu *What if 1st class?* pojawił się wykres Ceteris Paribus dla wieku, ale już po wpisaniu *What if Jack 1st class?* pojawił się oczekiwany wykres słupkowy CP dla Jacka i wszystkich klas.
* Po wpisaniu dowolnej komendy zawierającej słowo *plot*, np. *Lime plot for age and fare* pojawia się zawsze wykres CP dla wieku - oczekiwany komunikat o błędzie, braku możliwości narysowania takiego wykresu.
* Po wpisaniu *What if I had parents?* ponownie pojawia się wykres CP dla wieku - zdecydowanie za dużo go.
* Po wpisaniu *Change variables order in Brek Down* pojawia się komunikat *Click on the variable to see a detailed description* - brak możliwości zmiany kolejności zmiennych.

### Ulepszenia działania bota, w celu lepszego zrozumienia modelu

* Po wybraniu ścieżki Rose, po wpisaniu *Why had I survived?* zgodnie z oczekiwaniami pojawia się wykres Break Down, ciekawym udogodnieniem byłaby możliwość zdefiniowania kolejności dokładania zmiennych.
* Brak informacji, że Rose przeżyła dzięki Jackowi!
* Po wpisaniu *ale plot for fare* lub *pdp plot for fare* pojawia się ten sam wykres Ceteris Paribus dla zmiennej *fare* - dodanie możliwości rysowania powyższych wykresów
