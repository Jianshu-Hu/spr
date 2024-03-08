#!/bin/bash

cd /bd_targaryen/users/jhu/spr/
source /bd_targaryen/users/jhu/anaconda3/bin/activate
conda activate spr

tag=rainbow_simhash_repeat
seed=5

echo "start running $tag with seed $seed"
python -m scripts.run --repeat_type 1 --spr 0 --game battle_zone --momentum-tau 1.0 --seed $seed --tag $tag
