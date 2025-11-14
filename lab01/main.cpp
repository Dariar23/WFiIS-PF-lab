#include <iostream>
//zad1
bool czy_jest(int* tab_wsk_poczatek, int rozmiar_tab, int liczba_szukana){
    if(rozmiar_tab==0){
        return false;
    }
    if(*tab_wsk_poczatek==liczba_szukana){
        return true;
    }
    return czy_jest(tab_wsk_poczatek + 1, rozmiar_tab - 1, liczba_szukana);
}
//zad2
typedef bool (*Predykat)(int);
bool czy_jest_pred(int* tab_wsk_poczatek, int rozmiar_tab, Predykat predykat ){
    if(predykat(*tab_wsk_poczatek)){
        return true;
    }
    if(rozmiar_tab==0){
        return false;
    }
   return czy_jest_pred(tab_wsk_poczatek+1,rozmiar_tab-1,predykat);
}
//zad4
double suma_ulamkow(double dokladnosc){
    double sum=0.0;
    int n=1;
    while(1.0/n>=dokladnosc){
        sum+=1.0/n;
        n++;
    }
    
    return sum;
}
double suma_ulamkow_rek(double dokladnosc, int n = 1, double sum = 0.0) {
    double next= 1.0/n;
    if (next < dokladnosc) {      
        return sum;
    }
    return suma_ulamkow_rek(dokladnosc, n + 1, sum + next); 
}

using namespace std;
int main(){
      int *tab_wsk_poczatek=new int[10];
    for( int i=0; i <10; i++){
        tab_wsk_poczatek[i]=i+1;
    }
czy_jest( tab_wsk_poczatek, 10, 5)?cout<<"true":cout<<"false";cout<<endl;  
czy_jest( tab_wsk_poczatek, 10, 0)?cout<<"true":cout<<"false";cout<<endl;  
czy_jest( tab_wsk_poczatek, 10, 12)?cout<<"true":cout<<"false";cout<<endl;    
czy_jest_pred(tab_wsk_poczatek, 10, [](int el){ return el >5; })?cout<<"true":cout<<"false";cout<<endl;  

//cout<<suma_ulamkow_rek(2.0);
printf("suma_ulamkow_rek=%.2f\n",suma_ulamkow_rek(0.01));
printf("suma_ulamkow=%.2f\n",suma_ulamkow(0.01));
delete[] tab_wsk_poczatek;
return 0;
}

