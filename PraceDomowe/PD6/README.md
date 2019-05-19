# Praca domowa 6

Czas na realizację: do najbliższych zajęć z wykładem 17 maja EOD

## Wprowadzenie:

Wykorzystujemy te same dane i ten sam model co podczas PD1 (czyli https://data.stanford.edu/hcmst2017)
Dane są zapisane w formacie Staty (dta). Do R można je wczytać np. pakietem `haven`, do pythona np `read_stata`.

## Zadanie:

1. Odtwórz model przewidujące czy dana osoba jest zamężna na podstawie wybranych zmiennych. Można wybrać dowolne zmienne objaśniające przy czym powinny być przynajmniej 2 ilościowe (lub przynajmniej uporządkowane) i 2 jakościowe. 
W kolumnie `S1` jest informacja czy dana osoba jest zamężna.

2. Wyznacz reszty dla tego modelu na zbiorze danych uczących.

3. Narysuj wykres kropkowy pokazujący zależność pomiędzy resztą (y - hat y) a wynikiem modelu (hat y). Dodaj krzywą lokalnego trendu (np. loess lub gam) i sprawdź czy różni się od funkcji stale równej zero. [Przykładowy wykres diagnostyczny](https://i.stack.imgur.com/7gT6g.jpg) (lewy górny)

4. Narysuj wykres kropkowy pokazujący zależność pomiędzy resztą (y - hat y) a wybraną zmienną zależną. Dodaj krzywą lokalnego trendu (np. loess lub gam) i sprawdź czy różni się od funkcji stale równej zero.

5. Dla każdej obserwacji policz [wartości Cooka](https://en.wikipedia.org/wiki/Cook%27s_distance) o ile zmieniłyby się predykcje modelu gdyby model uczyć na danych bez obserwacji i (miara wpływowości obserwacji i).

6. Do katalogu https://github.com/pbiecek/InterpretableMachineLearning2018S/tree/master/PraceDomowe/PD6 wgraj raport knitr lub jupiter notebook z wynikami punktów 1-5. 

## Uwagi dodatkowe

Zgłoszona praca domowa powinna dotyczyć innych zmiennych niż wcześniej zgłoszone prace innych osób. Czyli nie można zgłosić pracy opartej o zmienne, które wybrał już ktoś inny. Liczy się kolejność zgłoszeń na GitHub.
