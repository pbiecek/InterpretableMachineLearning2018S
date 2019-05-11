# Praca domowa 8

Czas na realizację: do najbliższych zajęć z wykładem 24 maja EOD

## Wprowadzenie:

Praca domowa jest kontynuacją laboratorium, które jest poświęcone metodzie Surrogate Assisted Feature Extraction for Model Learning.

Na wybranym zbiorze danych sprawdzimy czy w automatyczny sposób można zbudować interpretowalny model.

## Zadanie:

1. Pod adresem https://www.openml.org znaleźć można repozytorium wielu zbiorów danych. Należy wybrać jeden, dotyczący problemu regresyjnego dla zbioru danych, które nie zawierają brakujących wartości.

2. Dla wybranego zbioru danych (po podziale na uczący i testowy) należy wytrenować dwa elastyczne modele. Dowolne, np. catboost i random forest.

3. Dla lepszego z tych dwóch modeli, należy wykorzystać techniki typu Partial Dependence Plots / ALE aby przekształcić automatycznie oryginalną zmienną na nową kategoryczną zmienną. Przekształcić należy i zmienne ciągłe i dyskretne.

4. Na nowym zbiorze danych, wzbogaconym o te nowe zmienne należy zbudować prosty model np regresji liniowej.

5. Należy porównać skuteczność na zbiorze testowym trzech grup modeli: dwóch wybranych czarnych skrzynek. Modelu regresji wytrenowanego na danych bez transformacji. Modelu wytrenowanego na danych po transformacji.

6. Do katalogu https://github.com/pbiecek/InterpretableMachineLearning2018S/tree/master/PraceDomowe/PD8 wgraj plik jupiter lub markdown (plus html/pdf) z zapisem powyższych kroków oraz podsumowaniem, który z tych czterech modeli ma lepszy wynik i o ile lepszy.

## Uwagi dodatkowe

Nie spodziewam się, że dla dwóch różnych osób powtórzy się wybór zbioru danych i złożonych modeli (wybór w punktach 1 i 2).

