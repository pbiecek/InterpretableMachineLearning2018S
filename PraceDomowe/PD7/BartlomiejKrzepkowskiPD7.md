## Praca Domowa nr 7
### 1. Czego bot nie zrozumiał, a powinien?

Spytałem się:
"Show me Pearson correlation between age and gender"
Dostałem:
CP plot dla wieku względem 17 lat.

Spytałem się:
"Let's say I was born in 1887. Did I have chance to survive?"
Dostałem:
CP plot dla klasy podróży względem klasy pierwszej z informacją, iż inna klasa mogłaby zwiększyć moje szanse na przeżycie.

Spytałem się:
"Would I have a better chance of surviving, having a bra or not having it?"
Dostałem:
CP plot dla wybranej klasy podróży, względem klasy pierwszej.
Hmm.. to ciekawe, może bot uznaje, że tylko pierwsza klasa miała przywilej nosić wtedy staniki.
Spytałem się:
"How class feature is related to bra?"
Dostałem:
Ten sam wykres

Spytałem się:
"Did I survive the course, not getting on board?"
Dostałem:
"Your chance of survival equals 0.4344. It's close to a toss of a coin!"
Widać przeznaczenia się nie oszuka.



### 2. Jakie nowe intencje bot mógłby rozpoznawać tak by lepiej przybliżyć sposób działania modelu, który przewiduje szansę przeżycia katastrofy na Tytaniku.

Powinien być bardziej surowy co do akceptacji zdań.
Powinien dopytywać się o definicje nieznanych słów, albo o ich źródło.
Bot powinien reagować na nagłą zmianę kontekstu w pytaniach, w celu utrzymania płynności konwersacji - ludzie nie skaczą w rozmowie z pojęcia na pojęcie.

Spytałem się:
"What is your accuracy score on test set from this dataset kaggle.com/c/titanic/data"
Dostałem:
https://en.wikipedia.org/wiki/Passengers_of_the_RMS_Titanic
Bot powinien przedstawiać powody dla których warto mu ufać, np poprzez zwrócenie wyniku dla dostarczonego mu zbioru testowego.