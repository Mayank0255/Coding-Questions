def reverseLinkedList(head):
    prevP, currP = None, head
	while currP is not None:
		nextP = currP.next
		currP.next = prevP
		prevP = currP
		currP = nextP
	return prevP
