#!/usr/bin/env bash
set -e
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# test the skills using test jsons
cortex actions invoke nh/headline --params-file "${SCRIPT_DIR}/test/test_espn.json"
cortex actions invoke nh/headline --params-file "${SCRIPT_DIR}/test/test_cnn.json"
cortex actions invoke nh/headline --params-file "${SCRIPT_DIR}/test/test_cnbc.json"