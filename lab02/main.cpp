#include <iostream>
#include <string>
#include <vector>
#include "LazyFunctionalVector.h"
using namespace lfv;
int main() {
    //„celinka ma kota pies myszka chomik ”
    std::string arr[6] = {"celinka", "ma", "kota", "pies", "myszka", "chomik"};
    auto words = lazy_view(arr, 6);

    //wylicz ilość znaków zawartych we wszystkich słowach dłuższych niż 3 (filter, map, sum)
     auto ans_1=words.filter(F(_.length()>=4)).map(F(_.length())).sum();
     std::cout<<ans_1<<std::endl;
     
    //znajdź najkrótsze słowo (min)
    auto ans_2=words.min(F(_.length())).get();
    std::cout << ans_2.value_or("brak dannych")<< std::endl;

    //najkrótsze słowo na literę ‘c’ (filter, min)
    auto ans_3=words.filter(F(_[0]=='c')).min(F(_.length())).get();
    std::cout << ans_3.value_or("brak dannych")<< std::endl;

    //wszystkie słowa na ‘m’ złączone w jedno słowo (filter, accumulate)
    std::string string_ans="";
    std::string ans_4=words.filter(F(_[0]=='m')).accumulate( []( std::string total, std::string el){ return total+el; }, string_ans);
    std::cout<<ans_4<<std::endl;


    //sprawdź czy wśród słów wszystkie zawierają literą ‘a’ (filter, all)

    bool ans_5 = words.all(F(_.find('a') != std::string::npos));
    std::cout << ans_5 << std::endl;


    //sprawdź czy jakieś słowo ma długość mniejsza niż 3 (filter, contains
    bool ans_6 = words.contains(F(_.length() < 3));
    std::cout<<ans_6;
    


    return 0;
}
