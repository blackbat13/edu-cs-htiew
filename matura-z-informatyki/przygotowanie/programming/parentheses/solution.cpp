#include <iostream>
#include <fstream>
#include <vector>
#include <stack>
#include <algorithm>

using namespace std;

int exercise1();
vector<string> exercise2();
void exercise3();
void printVector(vector<string> tab);
bool compare(const string &a, const string &b);

int main()
{
    cout << "Exercise 1: " << exercise1() << endl;
    cout << "Exercise 2: " << endl;
    printVector(exercise2());
    cout << "Exercise 3: " << endl;
    exercise3();

    return 0;
}

int exercise1()
{
    vector<string> tab;
    string line;
    ifstream file("../../../../assets/parentheses.txt");
    while (file >> line && !file.eof())
    {
        tab.push_back(line);
    }

    file.close();

    int count = 0;
    for (auto &par : tab)
    {
        stack<char> st;
        bool ok = true;
        char top;
        for (auto &c : par)
        {
            if (c == '(' || c == '[' || c == '{')
            {
                st.push(c);
                continue;
            }

            if (st.empty())
            {
                ok = false;
                break;
            }

            top = st.top();
            if ((c == ')' && top != '(') || (c == ']' && top != '[') || (c == '}' && top != '{'))
            {
                ok = false;
                break;
            }

            st.pop();
        }

        if (ok && st.empty())
        {
            count++;
        }
    }

    return count;
}

vector<string> exercise2()
{
    vector<string> tab;
    string line;
    ifstream file("../../../../assets/parentheses.txt");
    while (file >> line && !file.eof())
    {
        tab.push_back(line);
    }

    file.close();

    sort(tab.begin(), tab.end(), compare);

    return tab;
}

void exercise3()
{
    vector<string> tab;
    string line;
    ifstream file("../../../../assets/parentheses.txt");
    while (file >> line && !file.eof())
    {
        tab.push_back(line);
    }

    file.close();

    for (auto &par : tab)
    {
        int max_opening_length = 0,
            max_closing_length = 0,
            current_opening_length = 0,
            current_closing_length = 0;
        for (auto &c : par)
        {
            if (c == '(' || c == '[' || c == '{')
            {
                current_closing_length = 0;
                current_opening_length++;
                max_opening_length = max(max_opening_length, current_opening_length);
            }
            else
            {
                current_opening_length = 0;
                current_closing_length++;
                max_closing_length = max(max_closing_length, current_closing_length);
            }
        }

        cout << max_opening_length << " " << max_closing_length << endl;
    }
}

void printVector(vector<string> tab)
{
    for (auto &el : tab)
    {
        cout << el << endl;
    }
}

bool compare(const string &a, const string &b)
{
    int round1 = 0, round2 = 0, square1 = 0, square2 = 0, curly1 = 0, curly2 = 0;
    for (auto &el : a)
    {
        if (el == '(' || el == ')')
        {
            round1++;
        }
        else if (el == '[' || el == ']')
        {
            square1++;
        }
        else
        {
            curly1++;
        }
    }

    for (auto &el : b)
    {
        if (el == '(' || el == ')')
        {
            round2++;
        }
        else if (el == '[' || el == ']')
        {
            square2++;
        }
        else
        {
            curly2++;
        }
    }

    if (round1 < round2)
    {
        return true;
    }
    else if (round1 > round2)
    {
        return false;
    }
    else if (square1 < square2)
    {
        return true;
    }
    else if (square1 > square2)
    {
        return false;
    }
    else
    {
        return curly1 < curly2;
    }
}