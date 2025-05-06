#!/bin/bash
set -x
export PYTHONPATH=../:$PYTHONPATH

MODEL=alexnet
for DATASET in CIFAR10 stl10 CIFAR100
do
python3 mem_attack.py $DATASET $MODEL \
-d 0 \
-o results/membership/$DATASET-$MODEL \
--victim_dir results/victim/$DATASET-$MODEL \
-e 100 \
--lr 1e-2 \
--pretrained
done
