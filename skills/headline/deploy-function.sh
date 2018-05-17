#!/usr/bin/env bash
set -e
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# Run the build
${SCRIPT_DIR}/build-function.sh
${SCRIPT_DIR}/../cnn/build-function.sh
${SCRIPT_DIR}/../cnbc/build-function.sh

# Deploy our function to Cortex
cortex actions deploy nh/headline --code "${SCRIPT_DIR}/build/function.zip" --kind python:3
cortex actions deploy nh/cnn --code "${SCRIPT_DIR}/../cnn/build/function.zip" --kind python:3
cortex actions deploy nh/cnbc --code "${SCRIPT_DIR}/../cnbc/build/function.zip" --kind python:3
