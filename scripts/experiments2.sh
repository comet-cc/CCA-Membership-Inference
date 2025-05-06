set -x
export PYTHONPATH=../:$PYTHONPATH

# Define multiple values for RATE and MODEL
#RATES=("1" "4" "8")  # Example rates, you can modify these as needed
RATES=("1")
#MODELS=("alexnet" "mobilenet")  # Example models, you can modify these as needed
#MODELS=("resnet18")
MODELS=("mobilenet")
#DATASETS=("downsampled-imagenet")
DATASETS=("celeba")
#DATASETS=("CIFAR100" "CIFAR10" "stl10")
# Loop through all datasets, models, and rates
for DATASET in  "${DATASETS[@]}"
do
  for RATE in "${RATES[@]}"
  do
    for MODEL in "${MODELS[@]}"
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
  done
done

