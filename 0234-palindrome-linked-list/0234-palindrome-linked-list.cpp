/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    bool isPalindrome(ListNode* head) {
        ListNode* slow = head;
        ListNode* fast = head->next;
        while(fast && fast->next){ //use pointer to search to find the mid point
            slow = slow->next;
            fast = fast->next->next;
        } //explaination: bcs the fast step is 2x that of the slow ste, if the fast end at nullptr, the slow one is right at the middle
        ListNode* prev = nullptr;
        ListNode* curr = slow->next; //start at the second half of the list 
        while(curr){
            ListNode* next = curr->next;
            curr->next = prev;
            prev = curr;
            curr = next; //swap the other half
        }
        while(prev){ //compare the first to the second half
            if(prev->val != head->val){ //value did not match
                return false;
            }
            prev = prev->next;
            head = head->next;
        }
        return true;
    }
};