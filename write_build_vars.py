import os

CI_PROJECT_NAME = os.getenv('CI_PROJECT_NAME')
CI_PIPELINE_ID = os.getenv('CI_PIPELINE_ID')
CI_COMMIT_TAG = os.getenv('CI_COMMIT_TAG')
CI_COMMIT_BRANCH = os.getenv('CI_COMMIT_BRANCH')
CI_DEFAULT_BRANCH = os.getenv('CI_DEFAULT_BRANCH')
CI_PROD_BRANCH = os.getenv('CI_PROD_BRANCH')

BUILD_IMAGE_TAG = ""

# 有打標籤的
if CI_COMMIT_TAG is not None:
    BUILD_IMAGE_TAG = CI_COMMIT_TAG
elif CI_COMMIT_BRANCH == CI_DEFAULT_BRANCH:
    BUILD_IMAGE_TAG = 'RC.' + CI_PIPELINE_ID
elif CI_COMMIT_BRANCH == CI_PROD_BRANCH:
    BUILD_IMAGE_TAG = 'stable.' + CI_PIPELINE_ID
else:
    BUILD_IMAGE_TAG = 'beta.' + CI_PIPELINE_ID

#print('BUILD_IMAGE_TAG=' + os.getenv('BUILD_IMAGE_TAG'))

f = open('build_vars.sh', 'w')
f.writelines("#!/bin/bash\n")
f.writelines("export BUILD_IMAGE_NAME=" + CI_PROJECT_NAME + "\n")
f.writelines("export BUILD_IMAGE_TAG=" + BUILD_IMAGE_TAG + "\n")
f.close()

build_env = open('build_vars.env', 'w')
build_env.writelines("BUILD_IMAGE_NAME=" + CI_PROJECT_NAME + "\n")
build_env.writelines("BUILD_IMAGE_TAG=" + BUILD_IMAGE_TAG + "\n")
build_env.close()
