from conans import ConanFile
from conans.tools import mkdir
import shutil


class RuntimeConan(ConanFile):
    name = "HelloRuntime"
    version = "0.1"
    build_requires = "Hello/0.1@user/testing"
    default_options = "Hello:shared=True", "Say:shared=True"
    settings = "os", "compiler", "build_type", "arch"
    
    def imports(self):
        self.copy("*", root_package="Hello")
        self.copy("*.dll", root_package="Say")

    def build(self):
        mkdir("pkg")
        shutil.copytree("include", "pkg/include")
        shutil.copytree("bin", "pkg/bin")
        shutil.copytree("lib", "pkg/lib")

    def package(self):
        self.copy("*", src="pkg")

    def package_info(self):
        self.cpp_info.libs = ["hello"]
