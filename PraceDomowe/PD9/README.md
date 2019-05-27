# Praca domowa 9

Czas na realizację: do najbliższych zajęć z wykładem 31 maja EOD

## Wprowadzenie:

Praca domowa jest kontynuacją laboratorium, które jest poświęcone metodzie Concept Drift opartej na Intersection Distance i krzywe PDP/ALE.

Na zbiorze danych hyperplanes sprawdzimy czy w automatyczny sposób można wykryć dryf/zmianę w zmiennych lub modelu.

## Zadanie:

1. Na stronie https://github.com/vlosing/driftDatasets znajduje się kolekcja zbiorów danych (rzeczywistych i syntetycznych) związanych z dryfem.
Należy pobrać z niej zbiór `hyperplane` (lub dowolny inny).

2. Szukamy zmian pomiędzy pierwszymi 10% zbioru danych i ostatnimi 10% zbioru danych. W tym celu należy zbudować model (np. regresji logistycznej) na obu częściach danych. Wyznaczyć rozkłady zmiennych i policzyć odległosci pomiędzy odpowiedziami modelu na obu zbiorach danych.

3. Dla dwóch wybranych podzbiorów policz: (A) Intersection distance dla każdej zmiennej (V1-V10) ze zbioru danych. (B) Intersection distance dla reszt z obu modeli. (C) Pole pomiędzy krzywymi PDP dla obu modeli.

4. Do katalogu https://github.com/pbiecek/InterpretableMachineLearning2018S/tree/master/PraceDomowe/PD9 wgraj plik jupiter lub markdown (plus html/pdf) z zapisem powyższych kroków oraz podsumowaniem co i jak bardzo zmieniło się pomiędzy tymi dwoma krokami.
