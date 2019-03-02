# Praca domowa 1

Czas na realizację: do 8 marca EOD

## Wprowadzenie:

Flowingdata opisał kilka dni temu ciekawe dane dotyczące stabilności związków (HCMST: How Couples Meet and Stay Together)
https://flowingdata.com/2019/02/26/probability-you-will-break-up-with-your-partner/

Dane wykorzystane w badaniu są dostępne tutaj:
https://data.stanford.edu/hcmst2017

Dane są zapisane w formacie Staty (dta). Do R można je wczytać np. pakietem `haven`, do pythona np `read_stata`.

Opis badania znajduje się tutaj: https://data.stanford.edu/hcmst

Opis zmiennych w zbiorze danych znajduje się tutaj: https://stacks.stanford.edu/file/druid:vt073cc9067/HCMST_2017_fresh_Codeboodk_v1.1a.pdf

## Zadanie:

1. Wczytaj dane z badania `HCMST`.

2. Zbuduj model przewidujący czy dana osoba jest zamężna na podstawie wybranych zmiennych. Można wybrać dowolne zmienne objaśniające przy czym powinny być przynajmniej 2 ilościowe (lub przynajmniej uporządkowane) i 2 jakościowe. W kolumnie `S1` jest informacja czy dana osoba jest zamężna. Można zbudować dowolny model, sugeruję xgboost lub las losowy.

3. Dla wybranej osoby narysuj profile Ceteris Paribus dla przynajmniej 2 zmiennych ciągłych.

4. Do katalogu https://github.com/pbiecek/InterpretableMachineLearning2018S/tree/master/PraceDomowe/PD1 wgraj raport knitr lub jupiter notebook z wynikami punktów 1-3. 

## Uwagi dodatkowe

Zgłoszona praca domowa powinna dotyczyć innych zmiennych niż wcześniej zgłoszone prace innych osób. Czyli nie można zgłosić pracy opartej o zmienne, które wybrał już ktoś inny. Liczy się kolejność zgłoszeń na GitHub.


