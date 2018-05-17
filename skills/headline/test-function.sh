#!/usr/bin/env bash
set -e
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

cortex actions invoke nh/headline --params-file "${SCRIPT_DIR}/test/test_req.json"
#cortex actions invoke nh/cnn --params-file "${SCRIPT_DIR}/test/test_req.json"
#cortex actions invoke nh/cnbc --params-file "${SCRIPT_DIR}/test/test_req.json"