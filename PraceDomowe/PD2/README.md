# Praca domowa 2

Czas na realizację: do 22 marca EOD

## Wprowadzenie:

Wykorzystujemy te same dane i ten sam model co podczas PD1 (czyli https://data.stanford.edu/hcmst2017)
Dane są zapisane w formacie Staty (dta). Do R można je wczytać np. pakietem `haven`, do pythona np `read_stata`.

## Zadanie:

1. Odtwórz model przewidujący czy dana osoba jest zamężna na podstawie wybranych zmiennych. Można wybrać dowolne zmienne objaśniające przy czym powinny być przynajmniej 2 ilościowe (lub przynajmniej uporządkowane) i 2 jakościowe. W kolumnie `S1` jest informacja czy dana osoba jest zamężna. Można zbudować dowolny model, sugeruję xgboost lub las losowy.

2. Dla wybranych zmiennych (najlepiej tych które były użyte w PD1) porównaj profile Ceteris Paribus z przynajmniej jednym innym rodzajem liczenia odpowiedzi modelu (Accumulated Local Effects lub Marginal Effects lub Local Conditional Expectations).

3. Czy profile CP różni się od profilu biorącego pod uwagę korelacje? Spróbuj wyjaśnić uzyskane wyniki.

4. Do katalogu https://github.com/pbiecek/InterpretableMachineLearning2018S/tree/master/PraceDomowe/PD2 wgraj raport knitr lub jupiter notebook z wynikami punktów 1-3. 

## Uwagi dodatkowe

Zgłoszona praca domowa powinna dotyczyć innych zmiennych niż wcześniej zgłoszone prace innych osób. Czyli nie można zgłosić pracy opartej o zmienne, które wybrał już ktoś inny. Liczy się kolejność zgłoszeń na GitHub.


