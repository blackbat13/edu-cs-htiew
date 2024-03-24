# Liczby Fibonacciego

## Opis problemu

Ciąg Fibonacciego to ciąg, w którym dwa pierwsze elementy mają wartość $$1$$, a każdy kolejny element stanowi sumę dwóch poprzednich.

Pierwszych dziesięć kolejnych liczb Fibonacciego to: $$1, 1, 2, 3, 5, 8, 13, 21, 34, 55$$.

### Specyfikacja

#### Dane

* $$n$$ - liczba naturalna, $$n>0$$.

#### Wynik

* $$n$$-ta liczba Fibonacciego.

### Przykład

#### Dane

```
n := 10
```

**Wynik**: $$55$$ 

## Rozwiązanie rekurencyjne

$$
Fib(n) =  \begin{cases} 
      1 & n \leq 2 \\
      Fib(n - 1) + Fib(n - 2) & n > 2 \\
   \end{cases}
$$

### Pseudokod

```
funkcja Fib(n):
    1. Jeżeli n <= 2, to:
        2. Zwróć 1
    3. Zwróć Fib(n - 1) + Fib(n - 2)
```

### Schemat blokowy

```mermaid
%%{init: {"flowchart": {"curve": "linear"}, "theme": "neutral"} }%%
flowchart TD
	START(["Fib(n)"]) --> K1{n <= 2}
	K1 -- PRAWDA --> K2[/Zwróć 1/]
	K2 --> STOP([STOP])
	K1 -- FAŁSZ --> K3[/"Zwróć Fib(n - 1) + Fib(n - 2)"/]
	K3 --> STOP
```

## Rozwiązanie iteracyjne

### Pseudokod

```
funkcja Fib(n):
    1. f1 := 1
    2. f2 := 1
    3. Od i := 3 do n + 1, wykonuj:
        4. f3 := f1 + f2
        5. f1 := f2
        6. f2 := f3
    7. Zwróć f2
```

### Schemat blokowy

```mermaid
%%{init: {"flowchart": {"curve": "linear"}, "theme": "neutral"} }%%
flowchart TD
	START(["Fib(n)"]) --> K1[f1 := 1\nf2 := 1\ni := 3]
	K1 --> K3{i <= n + 1}
	K3 -- PRAWDA --> K4[f3 := f1 + f2\nf1 := f2\nf2 := f3\ni := i +1]
	K4 --> K3
	K3 -- FAŁSZ --> K7[/Zwróć f2/]
	K7 --> STOP([STOP])
```

## Implementacja

### C++

{% content-ref url="../../programming/c++/algorithms/integers/fibonacci-numbers.md" %}
[fibonacci-numbers.md](../../programming/c++/algorithms/integers/fibonacci-numbers.md)
{% endcontent-ref %}

### Python

{% content-ref url="../../programming/python/algorithms/integers/fibonacci-numbers.md" %}
[fibonacci-numbers.md](../../programming/python/algorithms/integers/fibonacci-numbers.md)
{% endcontent-ref %}

## Implementacja - pozostałe

### Haskell

{% content-ref url="../../programming/haskell/algorithms/integers/fibonacci-numbers.md" %}
[fibonacci-numbers.md](../../programming/haskell/algorithms/integers/fibonacci-numbers.md)
{% endcontent-ref %}
