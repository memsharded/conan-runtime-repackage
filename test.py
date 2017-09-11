import os

os.system("cd say && conan export user/testing")
os.system("cd hello && conan export user/testing")
os.system("cd runtime && conan create user/testing --build=missing")