class Bitset {
public:
    string bit = "";
    string rev = "";
    int count1 = 0;
    int flipp = 0;
    int n;
    
    Bitset(int size) {
        for(int i=0; i<size; i++) {
            bit += '0';
            rev += '1';
        }
        n = size;
    }
    
    void fix(int idx) {
        if(flipp%2==0) {
            if(bit[idx] == '0') count1++;
            bit[idx] = '1';
            rev[idx] = '0';
        } else {
            // if flipped, we need to fix rev and unfix bit at idx
            // count1 is 1 bits in bit not rev
            if(bit[idx] == '1') count1--;
            bit[idx] = '0';
            rev[idx] = '1';
        }
    }
    
    void unfix(int idx) {
        if(flipp%2==0)
        {
            if(bit[idx] == '1') count1--;
            bit[idx] = '0';
            rev[idx] = '1';
        } else {
            // if flipped, we need to unfix rev and fix bit at idx
            if(bit[idx] == '0') count1++;
            bit[idx] = '1';
            rev[idx] = '0';
        }
    }
    
    void flip() {
        flipp++;
    }
    
    bool all() {
        //if flipped count 1's in rev i.e., n-count1
        int temp = (flipp%2)? (n-count1) : count1;
        if(temp == n) return true;
        return false;
    }
    
    bool one() {
        //if flipped count 1's in rev i.e., n-count1
        int temp = (flipp%2) ? (n-count1) : count1;
        if(temp) return true;
        return false;
    }
    
    int count() {
        if(flipp%2) return n-count1;
        return count1;
    }
    
    string toString() {
        return flipp%2 ? rev : bit;
    }
};