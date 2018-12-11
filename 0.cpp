#include<bits/stdc++.h>
using namespace std;
int main(){
int a,b;
cin>>a>>b;
long long int t=0;
int zz;
int g=a;
int vv=0;
int bb=0;
int kkk=1000;
while(t<10000000){int m;
    t++;

    if(bb!=0){kkk =kkk-b;
    cout<<'2'<<endl;
    if((g+vv)%2==0){m= (g+vv)/2;}
    else{m = (g+1+vv)/2;}
    if(m != g){kkk--;
    cout<<'1'<<" "<<m<<endl;
    }else{cout<<'3'<<" "<<g<<endl;
    break;}}
    else if(bb==0){
        if((g+vv)%2==0){m= (g+vv)/2;}
    else{m = (g+1+vv)/2;}
    kkk--;
    cout<<'1'<<" "<<m<<endl;
    }
    int kk;
    cin>>kk;
    if(kk == -1){break;}
    if(kkk<0){
        break;
    }
    if(kk==1 && bb==0){
        if(m-vv == 1){if(kkk>=b){cout<<'2'<<endl;}
        cout<<'3'<<" "<<m<<endl;
        break;}
    }else if(kk==0 && bb==1){if(g-m == 1){
    cout<<'3'<<" "<<g<<endl;
    break;}
    }
    if(kk==0){vv=m;
    g=g;}else if(kk=1){
    g=m;
    vv=vv;}
    bb=kk;
}
}
