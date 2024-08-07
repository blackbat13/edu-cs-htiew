# Zadanie 1 - rozwiązanie

## Drzewo kodów

```mermaid
%%{init: {"flowchart": {"curve": "linear"}, "theme": "neutral"} }%%
flowchart TD
	n25((18)) --0--> n23((8))
	n25((18)) --1--> n24((10))
	n24((10)) --0--> n21((4))
	n24((10)) --1--> n22((6))
	n22((6)) --0--> n2(("3|e"))
	n22((6)) --1--> n18((3))
	n18((3)) --0--> n10(("1|i"))
	n18((3)) --1--> n9(("2|o"))
	n21((4)) --0--> n16((2))
	n21((4)) --1--> n17((2))
	n17((2)) --0--> n7(("1|d"))
	n17((2)) --1--> n8(("1|r"))
	n16((2)) --0--> n5(("1|l"))
	n16((2)) --1--> n6(("1|g"))
	n23((8)) --0--> n19((4))
	n23((8)) --1--> n20((4))
	n20((4)) --0--> n14((2))
	n20((4)) --1--> n15((2))
	n15((2)) --0--> n3(("1|n"))
	n15((2)) --1--> n4(("1|p"))
	n14((2)) --0--> n0(("1|s"))
	n14((2)) --1--> n1(("1|k"))
	n19((4)) --0--> n11(("2|_"))
	n19((4)) --1--> n12(("2|w"))
```

## Tabela kodów

|  znak  |     kod    |
| :-: | :------: |
| _ | 000 |
| d | 1010 |
| e | 110 |
| g | 1001 |
| i | 1110 |
| k | 0101 |
| l | 1000 |
| n | 0110 |
| o | 1111 |
| p | 0111 |
| r | 1011 |
| s | 0100 |
| w | 001 |

## Zakodowany tekst

```
01010110111100110001101010100111000011100100000011111110011101011
```

## Stopień kompresji

$45.14\%$
