#pragma once

#include <string>

#ifdef WIN32
  #define SAY_EXPORT __declspec(dllexport)
#else
  #define SAY_EXPORT
#endif

SAY_EXPORT void say(const std::string& str);
