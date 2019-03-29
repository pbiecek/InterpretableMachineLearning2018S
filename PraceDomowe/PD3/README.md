# Praca domowa 3

Czas na realizację: do najbliższych zajęć z wykładem 29 marca EOD

## Wprowadzenie:

Wykorzystujemy te same dane i ten sam model co podczas PD1 (czyli https://data.stanford.edu/hcmst2017)
Dane są zapisane w formacie Staty (dta). Do R można je wczytać np. pakietem `haven`, do pythona np `read_stata`.

## Zadanie:

1. Odtwórz model przewidujący czy dana osoba jest zamężna na podstawie wybranych zmiennych. Można wybrać dowolne zmienne objaśniające przy czym powinny być przynajmniej 2 ilościowe (lub przynajmniej uporządkowane) i 2 jakościowe. W kolumnie `S1` jest informacja czy dana osoba jest zamężna. Można zbudować dowolny model, sugeruję xgboost lub las losowy.

2. Dla wybranej obserwacji i ustalonej kolejności zmiennych wyznacz zmianę w średniej odpowiedzi modelu (zgodnie z ćwiczeniem z laboratorium).

3. Porównaj dwie kolejności warunkowania. Czy efekty zmiennych różnią się między sobą.

4. Do katalogu https://github.com/pbiecek/InterpretableMachineLearning2018S/tree/master/PraceDomowe/PD3 wgraj raport knitr lub jupiter notebook z wynikami punktów 1-3. 

## Uwagi dodatkowe

Zgłoszona praca domowa powinna dotyczyć innych zmiennych niż wcześniej zgłoszone prace innych osób. Czyli nie można zgłosić pracy opartej o zmienne, które wybrał już ktoś inny. Liczy się kolejność zgłoszeń na GitHub.


