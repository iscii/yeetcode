/* 
    9/17/2022
    Runtime: 45 ms
    Memory Usage: 13 MB
 */

#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    bool isPalindrome(int x) {
        if(x < 0) return 0;
        vector<int> v, w;
        
        while(1){
            if(x<10){
                v.push_back(x%10);
                break;
            }
            v.push_back(x % 10);
            x = x/10;
        }
        
        for(int i=v.size()-1;i>=0;i--){
            w.push_back(v[i]);
        }
        
        return v==w;
    }
};

int main(){
    Solution s;
    cout << s.isPalindrome(121) << endl;
    cout << s.isPalindrome(123);
    
    return 0;
}