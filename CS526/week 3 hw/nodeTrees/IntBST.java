package nodeTrees;

import java.util.ArrayList;
import java.util.List;

// binary search tree storing integers
public class IntBST extends NodeBinaryTree<Integer> {

	private int size = 0;
	
	public IntBST() {	}

	public int size() {
		return size;
	}

	public void setSize(int s) { size = s; }
	
	public boolean isEmpty() {
		return size() == 0;
	}

	/**
	 * Places element e at the root of an empty tree and returns its new Node.
	 *
	 * @param e the new element
	 * @return the Node of the new element
	 * @throws IllegalStateException if the tree is not empty
	 */

	public Node<Integer> addRoot(Integer e) throws IllegalStateException {
		if (size != 0)
			throw new IllegalStateException("Tree is not empty");
		root = createNode(e, null, null, null);
		size = 1;
		return root;
	}

	/**
	 * Print a binary tree horizontally Modified version of
	 * https://stackoverflow.com/questions/4965335/how-to-print-binary-tree-diagram
	 * Modified by Keith Gutfreund
	 * 
	 * @param n Node in tree to start printing from
	 */
	
	  public void print(Node<Integer> n){ print ("", n); }
	  
	  public void print(String prefix, Node<Integer> n){
		  if (n != null){
			  print(prefix + "       ", right(n));
			  System.out.println (prefix + ("|-- ") + n.getElement());
			  print(prefix + "       ", left(n));
		  }
	  }
	  
	  
	  public void inorderPrint(Node<Integer> n) {
		if (n == null)
			return;
		inorderPrint(n.getLeft());
		System.out.print(n.getElement() + "  ");
		inorderPrint(n.getRight());
	}

	
	public Iterable<Node<Integer>> children(Node<Integer> n) {
		List<Node<Integer>> snapshot = new ArrayList<>(2); // max capacity of 2 
		if (left(n) != null) 
			snapshot.add(left(n)); 
		if (right(n) != null)
			snapshot.add(right(n)); return snapshot; 
	}
	
	public int height(Node<Integer> n) throws IllegalArgumentException { 
		if (isExternal(n)) { return 0; } 
		int h = 0; // base case if p is external
		for (Node<Integer> c : children(n)) h = Math.max(h, height(c)); return h + 1; 
	}


	
	public static IntBST makeBinaryTree(int[] a){
		
		// complete this method
		return binaryTreeBuilder(a, 0, a.length -1);
	}

	public static IntBST binaryTreeBuilder(int[] a, int startIndex, int endIndex){
		IntBST tree = new IntBST();
		if(startIndex < endIndex){
			//System.out.println("startIndex = " + startIndex + " endIndex = "+ endIndex);
			//create a new tree
			//find the middle element of the array
			int middle = (endIndex - startIndex)/2;

			//middle = ... integer division
			int middleVal = a[middle];
			//add the node using the element from the middle
			tree.addRoot(middleVal);
			//build left side of the tree using recursion
			//makeBinaryTree(...)
			System.out.println("startIndex = " + startIndex + " endIndex = "+ endIndex+ " middleIndex = " + middle);
			IntBST left = binaryTreeBuilder(a, startIndex, middle);

			//build right side of the tree using recursion
			//makeBinaryTree(...)
			IntBST right = binaryTreeBuilder(a, middle+1, endIndex);

			//account for the size of the tree
			tree.setSize(tree.size + 1);
			//call attach to join the middle node as the root, let tree and right tree
			tree.attach(tree.root, left, right);
			return tree;
		}else if(startIndex == endIndex) {
			tree.addRoot(a[startIndex]);
			return tree;
		}
		return tree;
	}

}
