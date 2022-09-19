/* 
    9/17/2022
    Runtime: 16 ms
    Memory Usage: 12.1 MB
*/

#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    //better ones will hold the position of the string and compare substrings instead of holding the substring itself
    string longestCommonPrefix(vector<string>& strs) {
        string str = "";
        
        for(const auto ch : strs[0]){
            str += ch;
            for(int j=1;j<strs.size();j++){
                if(strs[j].substr(0, str.length()) != str)
                    return str.substr(0, str.length()-1);
            }
            
        }
        return str;
    }
};

int main(){
    Solution s;
    vector<string> strs = {"flower", "flow", "flight"};
    cout << s.longestCommonPrefix(strs) << endl;
    return 0;
}