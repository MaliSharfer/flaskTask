echo $1
echo $2
touch $1.bash
touch $2.bash
mkdir newFolder
mv $1.bash newFolder/$1.bash
mv $2.bash newFolder/$2.bash
ls newFolder
set -n