from linkedlist import Node, LinkedList

llist = LinkedList()
llist.head = Node("Seshanba")
llist.push("Dushanba")
llist.insertAfter(llist.head.next, "Chorshanba")
llist.append("Payshanba")
llist.push("Yakshanba")
llist.deleteNode("Yakshanba")
llist.printList()