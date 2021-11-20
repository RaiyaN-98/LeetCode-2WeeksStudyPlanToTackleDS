class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        vector<int> ans;
        int i = 0, j = 0;
        for(i, j; i < m && j < n;){
            if(nums1[i] < nums2[j]){
                ans.push_back(nums1[i]);
                i++;
            }else{
                ans.push_back(nums2[j]);
                j++;
            }
        }
        for(i; i < m ; i++) ans.push_back(nums1[i]);
        for(j; j < n ; j++) ans.push_back(nums2[j]);
        nums1.clear();
        for(int x : ans) nums1.push_back(x);
    }
};
