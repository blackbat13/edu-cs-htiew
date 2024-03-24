# Znajdowanie lidera w zbiorze

## Opis problemu

{% content-ref url="../../../../algorithms/searching/majority.md" %}
[majority.md](../../../../algorithms/searching/majority.md)
{% endcontent-ref %}

## Implementacja

{% code overflow="wrap" lineNumbers="true" %}
```python
function majority(array)
    counter = 0
    currentCandidate = 0

    for el in array
        if counter == 0
            currentCandidate = el
            counter = 1
        elseif el == currentCandidate
            counter += 1
        else
            counter -= 1
        end
    end

    if count(x -> x == currentCandidate, array) > length(array) / 2
        return currentCandidate
    else
        return -1
    end
end


array = [1, 2, 5, 5, 7, 5, 5, 10, 5, 5]

println(majority(array))
```
{% endcode %}
