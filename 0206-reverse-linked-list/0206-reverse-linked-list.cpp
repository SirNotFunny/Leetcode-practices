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
    ListNode* reverseList(ListNode* head) {
        ListNode* curr = head;
        ListNode* prev = nullptr;
        ListNode* next = new ListNode();
        while(curr){ //traverse through the entire list
            next = curr->next; //store next ptr
            curr->next = prev; //reverse the current node's next pointer 
            prev = curr; //move ptr to one position ahead
            curr = next;
        } // prev - curr - next => swap ptr 
        return prev;
    }
};