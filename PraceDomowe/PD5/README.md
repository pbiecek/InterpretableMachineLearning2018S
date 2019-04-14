# Praca domowa 5

Czas na realizację: do najbliższych zajęć z wykładem 26 kwietnia EOD

## Wprowadzenie:

Wykorzystujemy te same dane i ten sam model co podczas PD1 (czyli https://data.stanford.edu/hcmst2017)
Dane są zapisane w formacie Staty (dta). Do R można je wczytać np. pakietem `haven`, do pythona np `read_stata`.

## Zadanie:

1. Odtwórz **przynajmneij dwa modele** przewidujące czy dana osoba jest zamężna na podstawie wybranych zmiennych. Można wybrać dowolne zmienne objaśniające przy czym powinny być przynajmniej 2 ilościowe (lub przynajmniej uporządkowane) i 2 jakościowe. 
W kolumnie `S1` jest informacja czy dana osoba jest zamężna. Można zbudować dowolne modele, sugeruję modele znacznie różnicące się strukturą.

2. Dla każdej zmiennej występującej w którymkolwiek modelu policz ważność zmiennej używając techniki spadek funkcji loss po perturbacjach.

3. Porównaj dwa wybrane modele. Czy jest zmienna która zachowuje sie w nich inaczej? 

4. Wybierz zmienną najbardziej różniącą porównywane modele i narysuj dla niej krzywe PDP lub ALEplot. Skomentuj skąd biorą się różnice pomiędzy krzywymi PDP. Czy wynikają one z ogeaniczeń wybranych modeli czy z czegoś innego.

5. Do katalogu https://github.com/pbiecek/InterpretableMachineLearning2018S/tree/master/PraceDomowe/PD5 wgraj raport knitr lub jupiter notebook z wynikami punktów 1-5. 

## Uwagi dodatkowe

Zgłoszona praca domowa powinna dotyczyć innych zmiennych niż wcześniej zgłoszone prace innych osób. Czyli nie można zgłosić pracy opartej o zmienne, które wybrał już ktoś inny. Liczy się kolejność zgłoszeń na GitHub.
