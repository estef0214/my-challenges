'''
Input:
A -> B -> C -> D -> E
          |
          F -> G -> H
                |
                I

Output:
A -> B -> C -> F -> G -> I -> H -> D -> E

-each node:
    -3 attributes: next pointer, other pointer, value
   ex of other pointer: C -> F

-input: modified linked list
-outpit: single linked list where all of the nodes other pointer are pointing to none

-dont copy, rearrange

method -> if other pointer -> list with other pointer
    return next pointer


base case:
if .next and .other -> none return node

->stored c.next
-
'''

def modifyList(modified_list):
    #recursive helper function that explores all branches of list
    def _exploreNodes(node)
        #base case is when we have gotten to an end of a branch
        if not node.next and not node.other:
            return node
        #save reference to nodes next node
        old_next = node.next
        #check if node has a reference to "other" node
        if node.other:
            #call recursive function to explore branch from other node which will return the last node in that branch
            last_node_of_branch = _exploreNodes(node.other)
            #link that last node to the next node of our current node
            last_node_of_branch.next = old_next
            #have current nodes next pointer set to its prev other
            node.next = node.other
            #reset other pointer to point to none
            node.other = None
        #call our recursive function on our current nodes original next node
        return _exploreNodes(old_next)

    #call my recursive function with head of input linked list
    _exploreNodes(modified_list)
    #return head of our modifiedlist
    return modified_list
