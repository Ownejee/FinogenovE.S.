// Press Shift twice to open the Search Everywhere dialog and type `show whitespaces`,
// then press Enter. You can now see whitespace characters in your code.
public class LinckedList {

    private Node head;

    public LinkedList() {
        head = null;
    }

    public class Node {
        public int data;
        public Node next;

        public Node(int data){
            this.data = data;
            next = null;
        }
    }
    public void add(int data) {
        Node nweNode = new Node(data);
        Node currentNode = head;

        if (head = null) {
            head = newNode;
        } else {
            while (currentNode.next != null) {
                currentNode = currentNode.next;
            }
            currentNode.next = newNode;
        }
    }

    public void remove(int data){
        Node currentNode = head;
        Node previousNode = null;

        while (currentNode.next != null) {

            if (currentNode.data == data) {
                if (currentNode == head) {
                    head = currentNode.next;
                } else {
                    previousNode.next = currentNode.next;
                }
            }

            previousNode = currentNode;
            currentNode = currentNode.next;
        }
    }
}