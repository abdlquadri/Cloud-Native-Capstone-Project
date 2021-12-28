#!/bin/bash -eu

set -e

protodir=../../pb

python -m grpc_tools.protoc -I$protodir --python_out=./protobuf/ --grpc_python_out=./protobuf $protodir/demo.proto
