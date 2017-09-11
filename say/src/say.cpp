#include <iostream>
#include <string>
#include "say.h"

void say(const std::string& str){
    #ifdef NDEBUG
    std::cout << "Release: "<< str << std::endl;
    #else
    std::cout << "Debug: "<< str << std::endl;
    #endif
}
