




# add SDL2 as submodule
git submodule add -b SDL2 https://github.com/libsdl-org/SDL.git

# install SDL library
mkdir build
cd build
 ../configure --prefix $PWD/../lib
 make
 make install