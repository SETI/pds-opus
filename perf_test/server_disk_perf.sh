#!/bin/sh
echo 1 > /proc/sys/vm/drop_caches
sleep 1
echo "*** DISK WRITE ***"
dd if=/dev/zero of=/tmp/ddtest.out bs=1G count=5 oflag=dsync
echo 1 > /proc/sys/vm/drop_caches
sleep 1
echo "*** DISK READ ***"
dd if=/tmp/ddtest.out of=/dev/null bs=1G count=5 oflag=dsync
rm /tmp/ddtest.out
