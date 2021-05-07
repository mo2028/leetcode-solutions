class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        
        vector<int> indices;
        for(int i = 0; i < nums.size(); i++)
        {
            //[3,5,1,4,7]
            int first = nums.at(i);
            for(int j = i+1; j < nums.size(); j++)
            {
                if((first + nums.at(j)) == target )
                {
                    indices.push_back(i);
                    indices.push_back(j);
                    
                    
                }
            }
        }
        return indices;
    }
    
};