#include <iostream>
#include <cstddef>
#include <queue>
#include <string>
#include <cstdlib>

using namespace std;	
class Node{
    public:
        int data;
        Node *left,*right;
        Node(int d){
            data=d;
            left=right=NULL;
        }
};
class Solution{
    public:
  		Node* insert(Node* root, int data){
            if(root==NULL){
                return new Node(data);
            }
            else{
                Node* cur;
                if(data<=root->data){
                    cur=insert(root->left,data);
                    root->left=cur;
                }
                else{
                   cur=insert(root->right,data);
                   root->right=cur;
                 }           
           return root;
           }
        }

	void levelOrder(Node * root){
        //Write your code here
        if (root == NULL)
            return;
        vector<int> bfs;
        queue<Node*> q;
        q.push(root);
        while (q.size() > 0) {
            Node* popped = q.front();
            q.pop();
            bfs.push_back(popped->data);
            if(popped->left != NULL)
                q.push(popped->left);
            if(popped->right != NULL)
                q.push(popped->right);
        }

        cout << bfs[0];
        for (int i = 1; i < bfs.size(); i++) {
            cout << " " << bfs[i];
        }
	}

};//End of Solution
int main(){
    Solution myTree;
    Node* root=NULL;
    int T,data;
    cin>>T;
    while(T-->0){
        cin>>data;
        root= myTree.insert(root,data);
    }
    myTree.levelOrder(root);
    return 0;
}