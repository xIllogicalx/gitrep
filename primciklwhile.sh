#!/bin/bash

a=1
while [ $a -le 100 ]; do
echo "текущее а" $a  
b=$(shuf -i 1-100 -n 1)
echo "текущее б" $b
a=$(($a+$b))
if [ $b -ge 100 ]; then echo "последнее б" $b
fi
done

