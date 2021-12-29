#!/bin/bash -eu

set -e

protodir=../../pb

python -m grpc_tools.protoc -I$protodir --python_out=./ --grpc_python_out=./ $protodir/demo.proto
