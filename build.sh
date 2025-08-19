#!/bin/bash

CURRENT_DIR=`pwd`
BUILD_TYPE=Release
BUILD_DIR=${CURRENT_DIR}/build
INSTALL_DIR=${CURRENT_DIR}/Release

rm -rf ${BUILD_DIR}
mkdir -p ${BUILD_DIR}
cd ${BUILD_DIR}
cmake -DCMAKE_INSTALL_PREFIX=${INSTALL_DIR} -DCMAKE_BUILD_TYPE=${BUILD_TYPE} ..
make -j`nproc`
make install
