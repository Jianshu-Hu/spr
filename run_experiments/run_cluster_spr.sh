#!/bin/bash

cd /bd_targaryen/users/jhu/spr
source /bd_targaryen/users/jhu/anaconda3/bin/activate
conda activate spr

tag=$1
game=$2
aug=$3
seed=$4

echo "start running $tag with seed $seed"
python -m scripts.run --augmentation $aug --spr 1 --game $game --momentum-tau 1.0 --seed $seed --tag $tag
