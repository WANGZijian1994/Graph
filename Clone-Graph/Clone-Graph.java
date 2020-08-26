/*
// Definition for a Node.
class Node {
    public int val;
    public List<Node> neighbors;
    
    public Node() {
        val = 0;
        neighbors = new ArrayList<Node>();
    }
    
    public Node(int _val) {
        val = _val;
        neighbors = new ArrayList<Node>();
    }
    
    public Node(int _val, ArrayList<Node> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
}
*/

class Solution {
    
    private Map<Integer,Node>m = new HashMap<Integer,Node>();
    
    public Node cloneGraph(Node node) {
        if(node==null){return null;}
        if(m.containsKey(node.val)){return m.get(node.val);}
        m.put(node.val,new Node(node.val,new ArrayList<Node>()));
        Node clone = m.get(node.val);
        for(int i = 0;i < node.neighbors.size();i++){
            clone.neighbors.add(cloneGraph(node.neighbors.get(i)));
        }
        return clone;
    }
}
