/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
        ListNode* a = headA; //intialize 2 ptr
        ListNode* b = headB;
        while(a != b){ //continue until both ptr of 2 list intersect
            if(a != nullptr){
                a = a->next; //if a did not end => redirect it to the next one of a
            }
            else{
                a = headB; //if the ptr a ended => redirect it to head of list b
            }
            if(b != nullptr){
                b = b->next; //same with b
            }
            else{
                b = headA;
            }
        }
        return a; //you can return b since both are the same
    }
};