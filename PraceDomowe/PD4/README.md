# Praca domowa 4

Czas na realizację: do najbliższych zajęć z wykładem 12 kwietnia EOD

## Wprowadzenie:

Wykorzystujemy te same dane i ten sam model co podczas PD1 (czyli https://data.stanford.edu/hcmst2017)
Dane są zapisane w formacie Staty (dta). Do R można je wczytać np. pakietem `haven`, do pythona np `read_stata`.

## Zadanie:

1. Odtwórz model `f` przewidujący czy dana osoba jest zamężna na podstawie wybranych zmiennych. Można wybrać dowolne zmienne objaśniające przy czym powinny być przynajmniej 2 ilościowe (lub przynajmniej uporządkowane) i 2 jakościowe. W kolumnie `S1` jest informacja czy dana osoba jest zamężna. Można zbudować dowolny model, sugeruję xgboost lub las losowy.

2. Dla wybranej obserwacji `x` wygeneruj zbiór danych `z` dla N (np. N=1000) obserwacji podobnych (np. perturbując wybrane zmienne).

3. Wyznacz predykcje dla modelu `f` na zbiorze danych `z`.

4. Dopasuj model białej skrzynki `g` (np. drzewo lub regresja liniowa) do predykcji dla zbioru `z` uwzględniając podobieństwo obserwacji z `z` do `x` (ważona regresja lub ważone drzdwo).

5. Narysuj lub wypisz znaleziony model `g`. Zastanów się jak zinterpretować wyjaśnienia otrzymane tą metodą. Jeżeli to możliwe to porównaj z wyjaśneiniami z PD3.

6. Do katalogu https://github.com/pbiecek/InterpretableMachineLearning2018S/tree/master/PraceDomowe/PD4 wgraj raport knitr lub jupiter notebook z wynikami punktów 1-5. 

## Uwagi dodatkowe

Zgłoszona praca domowa powinna dotyczyć innych zmiennych niż wcześniej zgłoszone prace innych osób. Czyli nie można zgłosić pracy opartej o zmienne, które wybrał już ktoś inny. Liczy się kolejność zgłoszeń na GitHub.


