#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
using namespace std;

vector<string> trojki;
vector<int> ileTrojek;
vector<string> zad2;
int litery[27];

void generujTrojki() {
    string znaki = "ABC";
    for(int i = 0; i < 3; i++) {
        for(int j = 0; j < 3; j++) {
            if(i == j) {
                continue;
            }
            for(int k = 0; k < 3; k++) {
                if(k == j || k == i) {
                    continue;
                }

                string t = "";
                t += znaki[i];
                t += znaki[j];
                t += znaki[k];

                trojki.push_back(t);
            }
        }
    }
}

bool czyAnagramy(string a, string b) {
    sort(a.begin(), a.end());
    sort(b.begin(), b.end());
    return a == b;
}

// Zwraca ile razy test zawarty jest w tekst
int zawiera(string tekst, string test) {
	int wynik = 0;
	for (int i = 0; i < tekst.size() - test.size() + 1; i++) {
		// Dla ka¿dego mo¿liwego pocz¹tkowego po³o¿enia wyrazu test w tekst
		bool ok = true; // Zak³adamy ¿e test zawiera siê w tekst i zaczyna siê w miejscu i
		// Bêdziemy szukaæ dowodu na to, ¿e tak nie jest
		for (int j = 0; j < test.size(); ++j) {
			if (tekst[i + j] != test[j]) { // Porównujemy kolejne litery tekst i test
				ok = false; // Je¿eli znajdziemy ró¿nicê, to zapamiêtujemy to i wychodzimy z pêtli
				break;
			}
		}

		if (ok) { // Je¿eli nie znaleŸliœmy ró¿nicy, to znaczy ¿e test zawiera siê w tekst
			wynik++;
		}
	}

	return wynik;
}

bool sprawdzTrojki(string a) {
    bool wynik = false;
    for(int i = 0; i < trojki.size(); ++i) {
		int ileRazy = zawiera(a, trojki[i]);
		ileTrojek[i] += ileRazy;
		if (ileRazy > 1) {
			wynik = true;
		}
    }

    return wynik;
}

void zliczLitery(string a) {
    for(int i = 0; i < a.length(); ++i) {
        litery[a[i] - 'A']++;
    }
};

int maxLitery() {
    int max = litery[0];
    int maxi=0;
    for(int i = 1; i < 26; ++i) {
        if(max < litery[i]) {
            max = litery[i];
            maxi=i;
        }
    }

    int ile = 0;
    for(int i = 0; i < 26; ++i) {
        if(litery[i] == max) {
            ile++;
        }
    }

    if(ile > 1) {
        return -1;
    }

    return maxi;
}

int minLitery() {
    int min = litery[0];
    int mini=0;
    for(int i = 1; i < 26; ++i) {
        if(min > litery[i] && litery[i] > 0) {
            min = litery[i];
            mini=i;
        }
    }

    int ile = 0;
    for(int i = 0; i < 26; ++i) {
        if(litery[i] == min) {
            ile++;
        }
    }

    if(ile > 1) {
        return -1;
    }

    return mini;
}

int main() {
    ifstream wejscie("hasla.txt");
    generujTrojki();
    ileTrojek = vector<int>(trojki.size(), 0);
    int ileAnagramow = 0;
    for(int i = 0; i < 1000; ++i) {
        string haslo1, haslo2;
        wejscie >> haslo1 >> haslo2;
        if(czyAnagramy(haslo1, haslo2)) {
            ileAnagramow++;
        }
        if(sprawdzTrojki(haslo1)) {
            zad2.push_back(haslo1);
        }
        if(sprawdzTrojki(haslo2)) {
            zad2.push_back(haslo2);
        }

        zliczLitery(haslo1);
        zliczLitery(haslo2);
    }

    wejscie.close();

    cout << "Zad1\n" << ileAnagramow << endl;
    cout << "Zad2" << endl;
    for (int i = 0; i < zad2.size(); ++i) {
        cout << zad2[i] << endl;
    }
    cout << endl;
    for(int i = 0; i < ileTrojek.size(); ++i) {
        cout << trojki[i] << " - " << ileTrojek[i] << endl;
    }
    cout << endl;
    cout << "Zad3" << endl;
    int maxL = maxLitery();
    int minL = minLitery();
    if(maxL == -1) {
        cout << "Brak litery wystepujacej najczesciej" << endl;
    } else {
        cout << "Litera wystepujaca najczesciej " << char('A' + maxL) << endl;
    }

    if(minL == -1) {
        cout << "Brak litery wystepujacej najrzadziej" << endl;
    } else {
        cout << "Litera wystepujaca najrzadziej " << ('A' + minL) << endl;
    }
    return 0;
}