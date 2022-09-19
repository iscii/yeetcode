//!INCOMPLETE

#include <iostream>
#include <vector>
#include <map>

using namespace std;

class Solution {
public:
    bool isValid(string s) {
        //store each open bracket in a map if it doesn't exist. increment if it does
        //if closed bracket has no matching open bracket in map, return 0
        //if closed bracket has one, go next and remove from map
        //at end of traversal, if map is still populated, return 0
        //else return 1
        
        map<string, int> openbrackets;

        for(const char &ch : s){
            if(ch == "(" || ch == "[" || ch == "{"){
                if(!openbrackets[ch]){
                    openbrackets[ch] = 0;
                }
                openbrackets[ch]++;
            }
            if(ch == ")" || ch == "]" || ch == "}"){
                if(!openbrackets[ch]){
                    return 0;
                }
            }
        }
        for (auto const& [key, val] : openbrackets){
            if(val) return 0;
        }
        return 1;
    }
};

int main(){
    Solution s;
    cout << s.isValid("()[]{}");

    return 0;
}