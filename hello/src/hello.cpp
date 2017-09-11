#include "hello.h"
#include "say.h"

void hello(){
    #ifdef NDEBUG
    say("Hello World Release!");
    #else
    say("Hello World Debug!");
    #endif
}
