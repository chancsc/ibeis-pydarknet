For more information on the original source code, see the [Darknet project website](http://pjreddie.com/darknet).

Note: this is a very old pydarknet but it's needed for ibeis project due to depreciated class, see:
https://github.com/Erotemic/ibeis/issues/86

It seems like this version of pydarknet, not able to compile with OpenCV 4.x, able to compile with OpenCV 3.4.20.

If machine have both OpenCV 4.x & 3.x installed, need to make changes to CMakeLists.txt

Update this line:

find_package (OpenCV REQUIRED ) -->
find_package (OpenCV 3.4.20 REQUIRED PATH /usr/local)
