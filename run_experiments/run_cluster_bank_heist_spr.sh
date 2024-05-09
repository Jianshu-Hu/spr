#!/bin/bash

cd /bd_targaryen/users/jhu/spr
source /bd_targaryen/users/jhu/anaconda3/bin/activate
conda activate spr

tag=spr_auto_et
aug=$1
seed=$2

echo "start running $tag with seed $seed"
python -m scripts.run --augmentation $aug --spr 1 --game bank_heist --momentum-tau 1.0 --seed $seed --tag $tag
