class ATM {
public:
    vector<long long> notes;
    vector<long long> value;
    ATM() {
        notes.resize(5, 0);
        value.resize(5);
        value[0] = 20;
        value[1] = 50; 
        value[2] = 100;
        value[3] = 200;
        value[4] = 500;
    }
    
    void deposit(vector<int> banknotesCount) {
        for(int i=0; i<5; i++)
            notes[i] += banknotesCount[i];
    }
    
    vector<int> withdraw(int amount) {
        vector<int> ans(5, 0);
        for(int i=4; i>=0; i--) {
            ans[i] =  min(notes[i], amount/value[i]);
            amount -= ans[i]*value[i];
        }
        if(amount>0) return vector<int> (1,-1);
        for(int i=0; i<5; i++) notes[i] -= ans[i];
        return ans;
    }
};

/**
 * Your ATM object will be instantiated and called as such:
 * ATM* obj = new ATM();
 * obj->deposit(banknotesCount);
 * vector<int> param_2 = obj->withdraw(amount);
 */