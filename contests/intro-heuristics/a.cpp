#include<iostream>
#include<cmath>
#include<stdlib.h>
using namespace std;

int D;
int cl[26];
int sl[400][26];

int scores(int tl[]) {
    int s = 0;
    int last[26];
    for(int i=0;i<26;i++){
        last[i] = 0;
    }
    for(int d=0;d<D;d++){
        int t = tl[d] - 1;
        last[t] = d+1;

        int ss = sl[d][t];
        for(int i=0;i<26;i++){
            int c = cl[i];
            ss -= c*(d+1-last[i]);
        }
        s += ss;
    }
    return s;
}

int main(){
    cin>>D;
    for(int i=0;i<26;i++){
        cin>>cl[i];
    }
    for(int i=0;i<D;i++){
        for(int j=0;j<26;j++){
            cin>>sl[i][j];
        }
    }
    double beta = 1.0;

    int tl[400];
    for(int i=0;i<400;i++){
        tl[i] = rand()%26+1;
    }
    int s = scores(tl);
    for(int i=0;i<10000;i++){
        int d = rand()%D+1;
        int x = tl[d-1];

        int e[26];
        for(int j=0;j<26;j++){
            int q = j+1;
            int x = tl[d-1];
            tl[d-1] = q;
            e[j] = scores(tl);
            tl[d-1] = x;
        }

        double esum = 0.0;
        double es[26];
        for(int j=0;j<26;j++) {
            es[j] = -log(e[j])/beta;
            esum += exp(es[j]);
        }
        double p = rand()/RAND_MAX;
        double ps = 0.0;
        for(int j=0;j<26;j++){
            ps += es[j]/esum;
            if(ps>p){
                tl[d-1] = j+1;
                break;
            }
        }

    }

    for(int i=0;i<D;i++){
        cout<<tl[i]<<endl;
    }
    return 0;
}