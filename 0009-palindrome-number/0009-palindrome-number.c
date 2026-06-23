bool isPalindrome(int x) {
    if(x<0) return false;
    long r=0,o=x;
    while(x!=0){
        int digit =x%10;
        r=r*10+digit;
        x/=10;
    }
    return (r==o);
    
}