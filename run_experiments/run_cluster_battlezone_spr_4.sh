#!/bin/bash

cd /bd_targaryen/users/jhu/spr/
source /bd_targaryen/users/jhu/anaconda3/bin/activate
conda activate spr

tag=rainbow
seed=4

echo "start running $tag with seed $seed"
python -m scripts.run --spr 0 --game battle_zone --momentum-tau 1.0 --seed $seed --tag $tag
