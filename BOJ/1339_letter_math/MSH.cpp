/*
1. Greedy
2. Searched for usage of scanf char array with fixed size
3. First attempt: greedily assign bigger numbers to alphabets of higher orders within the digits -> failed for below case
10
ABB
BB
BB
BB
BB
BB
BB
BB
BB
BB
answer: 1790, my first attempt: 1780
4. Second attempt: calculate the sum of weight for each alphabet
*/
#include <iostream>
#include <string>
#include <vector>
#include <queue>
#include <algorithm>
#include <map>
#include <set>
#include <cmath>

#define MAX_LENGTH 8

using namespace std;

struct Alphabet {
	char letter;
	int weight;
};

bool descending_weight (Alphabet a, Alphabet b) {
	return a.weight > b.weight;
}

vector<int> convert_strings_to_decimal (vector<string> &strings, map<char, int> &alphabet_to_num) {
	vector<int> answer;
	for (int i = 0; i < strings.size(); i++) {
		string s = strings[i];
		string decimal = "";
		for (int j = 0; j < s.length(); j++) {
			int curr_num = alphabet_to_num[s[j]];
			decimal += to_string(curr_num);
		}
		answer.push_back(stoi(decimal));
	}
	return answer;
}

int main () {

	// handle inputs
	int N;
	scanf("%d\n", &N);
	vector<string> strings;
	// remember where each letter occurs
	map<char, vector<int>> letter_occurrence_map;
	int longest_length = 0;
	for (int i = 0; i < N; i++) {
		char tmp[MAX_LENGTH + 1];
		scanf("%s", tmp);
		string s = tmp;
		if (s.length() > longest_length) { longest_length = s.length(); }
		strings.push_back(s);
		for (int j = 0; j < s.length(); j++) {
			int pos = s.length() - 1 - j;
			letter_occurrence_map[s[j]].push_back(pos);
		}
	}

	// FIFO for remaining numbers in descending order
	queue<int> available_numbers;
	for (int i = 9; i >= 0; i--) { available_numbers.push(i); }

	// calculate sum of weight of each letter's occurrence
	map<char, int> letter_weight_map;
	map<char, vector<int>>::iterator it;
	for (it = letter_occurrence_map.begin(); it != letter_occurrence_map.end(); it++) {
		vector<int> occurence = it->second;
		int weight = 0;
		for (int i = 0; i < occurence.size(); i++) {
			weight += pow(10, occurence[i]);
		}
		letter_weight_map[it->first] = weight;
	}

	// save each alphabet featured with letter and weight
	vector<Alphabet> alphabets;
	map<char, int>::iterator it2;
	int idx = 0;
	for (it2 = letter_weight_map.begin(); it2 != letter_weight_map.end(); it2++) {
		alphabets.push_back(Alphabet());
		alphabets[idx].letter = it2->first;
		alphabets[idx++].weight = it2->second;
	}

	// sort alphabets in descending order of weight
	sort(alphabets.begin(), alphabets.end(), descending_weight);

	// assign available numbers to each alphabet
	map<char, int> alphabet_to_num;
	for (int i = 0; i < alphabets.size(); i++) {
		alphabet_to_num[alphabets[i].letter] = available_numbers.front();
		available_numbers.pop();
	}

	// convert strings to decimal using map
	vector<int> decimals = convert_strings_to_decimal (strings, alphabet_to_num);
	int answer = 0;
	for (int i = 0; i < decimals.size(); i++) {
		answer += decimals[i];
	}

	printf("%d\n", answer);

	return 0;
}
