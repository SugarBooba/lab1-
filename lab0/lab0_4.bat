echo 1
wc -m ./lab0/lanturn8/* &>> /tmp/s368982_log
echo 2
grep -rl . | grep /s 2>&1 | xargs ls -lt | head -4
echo 3
cat -n ./lab0/lanturn8/* 2>> /tmp/s368982_log | grep -vi ble
echo 4
wc -m ./lab0/hydreigon6/golem ./lab0/hydreigon6/tyrogue | head -2 | sort -r 2>/dev/null
echo 5
ls -R ./lab0/lanturn8 | sort -r | grep "."
echo 6
chmod u=rx ./lab0/vileplume2
ls -lcr ./lab0/vileplume2 2>&1