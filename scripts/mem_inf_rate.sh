set -x
export PYTHONPATH=../:$PYTHONPATH

RATE="1"
MODEL=alexnet
for DATASET in CIFAR10 CIFAR100 stl10
do

python3 mem_attack.py $DATASET $MODEL \
-d 0 \
-o results/membership/$DATASET-$MODEL-$RATE \
--victim_dir results/victim/$DATASET-$MODEL-$RATE \
-e 100 \
--lr 1e-2 \
--rate $RATE \
--pretrained 

done
