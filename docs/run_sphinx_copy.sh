# set -euox pipefail
set -euo pipefail

proj_src=octoprobe

for proj_target in tentacle testbed_tutorial usbhubctl
do
    for sub_dir in _static _templates
    do
        dir_src=~/work_octoprobe_${proj_src}/docs/${sub_dir}
        dir_target=~/work_octoprobe_${proj_target}/docs/${sub_dir}
        rm -rf $dir_target
        cp -r $dir_src $dir_target
    done

    for filename in conf.py run_sphinx_copy.sh run_sphinx_upload.sh
    do
        cp -r ~/work_octoprobe_${proj_src}/docs/${filename} ~/work_octoprobe_${proj_target}/docs/
    done
done