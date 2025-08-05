/*CodeAcademy Exercise: Whale Talk
Takes a phrase like "turpentine and turtles" and translate it into its “whale talk” equivalent, "uueeieeauuee".

There are a few simple rules for translating text to whale language:

There are no consonants. Only vowels excluding the letter y.
The u‘s and e‘s are extra long, so we must double them.
Once we have converted text to the whale language, the result is sung slowly, as is custom in the ocean.

Write a whale.cpp program that accomplishes this translation using loops and vectors.
*/
#include <iostream>
#include <vector>
#include <string>

int main() {

  // Whale, whale, whale.
  // What have we got here?
  std::string input= "turpentine and turtles";
  std::vector<char> vowels = {'a', 'e', 'i', 'o', 'u'};

  std::vector<char> result;
  for(int i = 0; i < input.size(); i++){
    for(int j = 0; j < vowels.size(); j++){
      if(input[i] == vowels[j]){
        result.push_back(input[i]);
        if(vowels[j] == 'e' || vowels[j] == 'u'){
          result.push_back(vowels[j]);
        }
      }
    }
  }
  for(int c = 0; c < result.size(); c++){
    std::cout << result[c];
  }
  std::cout << "\n";
}
