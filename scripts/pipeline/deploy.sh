#!/bin/bash
# This script runs deployments to a given 'stage'
#
# The 'stage' is extracted from the pipeline name
#
# EXAMPLE
#
#     deploy_dev -> run deployment to DEV environment
#
# USAGE
#
# The script is usually called in the pipeline.
#
# If you want to call this script manually, make sure to provide
# the required ENV variables:
#
#    GO_PIPELINE_NAME=<pipeline_name> bash scripts/pipeline/deploy.sh
set -euo pipefail

# Set default values
CI=${CI:-true}
TEST_MODE=${TEST_MODE:-false}
GO_REVISION=${GO_PIPELINE_LABEL:-master}
ANSIBLE_EXTRA_OPTIONS=""

# Make variables available in ansible playbook
export CI

# INFO we always use lowercase filenames
GO_PIPELINE_NAME=$(echo "${GO_PIPELINE_NAME}" | tr '[:upper:]' '[:lower:]')
# INFO convert 'prefix_group_component_action_where' => 'where'
STAGE=$(echo "${GO_PIPELINE_NAME}" | awk 'BEGIN {FS="_"}{print $(NF)}')

# if [ "${STAGE}" == "live" ]; then
#   echo "INFO The stage ${STAGE} is not available yet."
#   exit 0
# else
#   echo "INFO Run deployment on ${STAGE} ..."
# fi

if [ "$TEST_MODE" == true ]; then
  # Override ansible parameters to disable the deployment in test mode
  ANSIBLE_EXTRA_OPTIONS="--inventory=app-${STAGE}, -c local --list-tasks"
fi

echo "INFO Run deployment on ${STAGE} ..."
# shellcheck disable=SC2086
ansible-playbook ansible/deployments.yml --limit "app-${STAGE}" \
                                        --inventory=ansible/hosts \
                                        --extra-vars=app_env="${STAGE}" \
                                        --extra-vars=app_revision="${GO_REVISION}" \
                                        --user sis-deployer \
                                        --verbose \
                                        ${ANSIBLE_EXTRA_OPTIONS}
