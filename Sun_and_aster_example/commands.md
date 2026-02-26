cd /mnt/c/users/Павел/desktop/SWIFT/SWIFT
./autogen.sh
./configure --with-gravity=with-multi-softening
make
cd /mnt/c/users/Павел/desktop/SWIFT/SWIFT/examples/GravityTests/Work_example
../../../swift --self-gravity --threads=4 config.yml 2>&1 | tee output.log
../../../swift --with-hydro=planetary --with-equation-of-state=planetary --threads=4 config.yml 2>&1 | tee output.log
