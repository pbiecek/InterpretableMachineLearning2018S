## Czego bot nie zrozumiał

Ogółem wydje się, że bot potrafi rysować jedynie breakdown plot i CP plot, więc wszystkie pytania o predykcje stara się zakwalifikować jako jedno z tych dwóch.

Np. na pytanie *What plots can you make?* model rysuje CP dla losowej zmiennej.

Nie można dowiedzieć się jaki ogólnie wpływ mają zmienne na -predykcje (nie tylko w tym konkretnym przyapdkku) i na pytania tego rodzaju bot odpowiada jednym z dwóch dostepnych mu wykresów.

Na pytanie *Compare Jack and Rose* odpowiedzią był jakiś wykres CP dla wieku 8, co sugeruje zupełny brak zrozumienia pytania.

## Jakie nowe intencje mógłby przewidywać

Przede wszystkim przydałyby się również wyjaśnienia całego modelu, a nie tylko konkretnych przyapdków.

Ciekawe mogłoby być porównanie dwóch osób ze sobą.

## Techniczne uwagi

Trudno zmienia się parametry, a te numeryczne zapisują się jako stringi i psują predykcje (nie znalazłam jak to ustawić poprawnie).

Też powiększone wykresy nadal są małe.
