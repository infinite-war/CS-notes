## notes
```
# 一个下载PA所需库的脚本，适用于Ubuntu22.04

# init_tool
apt-get install -y build-essential    # build-essential packages, include binary utilities, gcc, make, and so on
apt-get install -y man                # on-line reference manual
apt-get install -y gcc-doc            # on-line reference manual for gcc
apt-get install -y gdb                # GNU debugger
apt-get install -y git                # revision control system
apt-get install -y libreadline-dev    # a library used later
apt-get install -y libsdl2-dev        # a library used later
apt-get install -y llvm llvm-dev      # llvm project, which contains libraries used later

# pa0
apt-get install -y yacc
apt-get install -y bison
apt-get install -y flex
```

+ pa0中两次init.sh的执行会修改rc文件，默认修改~/.bashrc


```
bash init.sh nemu
bash init.sh abstract-machine
```