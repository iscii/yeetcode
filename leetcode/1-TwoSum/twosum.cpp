/* 
    9/17/2022
    Runtime: 854 ms
    Memory Usage: 10.2 MB
 */
#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> v;
        for(int i=0;i<nums.size();i++){
            for(int j=(i+1);j<nums.size();j++){
                if(nums[i] + nums[j] == target){
                    v = {i, j};
                    break;
                }
            }
        }
        return v;
    }
};

int main(){
    vector<int> arr = {2,7,11,15};
    Solution s;
    for (auto i: s.twoSum(arr, 9))
        cout << i << ' ';
        
    return 0;
}

