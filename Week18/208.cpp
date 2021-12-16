struct Node{
    Node* contain[26];
    bool is_end;
    Node(){
        is_end=false;
        for(int i=0; i<26; i++){
            contain[i]=NULL;    
        }
    }
};
class Trie {
public:
    Node* root=new Node();
    Trie() {
        
    }
    
    void insert(string word) {
        Node* current=root;
        for(int i=0; i<word.size(); i++){
            int pos=word[i]-'a';
            if(current->contain[pos]==NULL){
                current->contain[pos]= new Node();
            }
            current=current->contain[pos];
        }
        current->is_end=true;
    }
    
    bool search(string word) {
        Node* current=root;
        for(int i=0; i<word.size(); i++){
            int pos=word[i]-'a';
            if(current->contain[pos]==NULL){
                return false;
            }
            current=current->contain[pos];
        }
        return current->is_end==true;
    }
    
    bool startsWith(string prefix) {
        Node* current=root;
        for(int i=0; i<prefix.size(); i++){
            int pos=prefix[i]-'a';
            if(current->contain[pos]==NULL){
                return false;
            }
            current=current->contain[pos];
        }
        return true;
    }
};

/**
 * Your Trie object will be instantiated and called as such:
 * Trie* obj = new Trie();
 * obj->insert(word);
 * bool param_2 = obj->search(word);
 * bool param_3 = obj->startsWith(prefix);
 */
