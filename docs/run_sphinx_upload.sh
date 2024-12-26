# set -euox pipefail
set -euo pipefail

./run_sphinx_copy.sh

# for project in octoprobe tentacle testbed_showcase usbhubctl
for project in octoprobe tentacle testbed_showcase testbed_micropython
do
    docs_dir=~/work_octoprobe_${project}/docs
    html_dir=${docs_dir}/_build/html
    if [ -d "$docs_dir" ]; then
        echo "Directory upload: $html_dir"
        make -C $docs_dir clean
        make -C $docs_dir html
        tar cf - -C $html_dir  --transform "s,^\.,${project}," . | ssh www-data@www.maerki.com tar xf - -C /home/www/htdocs/octoprobe
    else
        echo "Directory does not exist: $docs_dir"
    fi
done