#!/bin/bash

cd /bigdata/users/jhu/spr/
source /bigdata/users/jhu/anaconda3/bin/activate
conda activate spr

tag=spr_jump_0
seed=4

echo "start running $tag with seed $seed"
python -m scripts.run --jumps 0 --game pong --momentum-tau 1.0 --seed $seed --tag $tag
