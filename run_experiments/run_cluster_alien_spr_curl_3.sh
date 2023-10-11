#!/bin/bash

cd /bigdata/users/jhu/spr/
source /bigdata/users/jhu/anaconda3/bin/activate
conda activate spr

tag=spr_CURL_normalized
seed=3

echo "start running $tag with seed $seed"
python -m scripts.run --spr_loss_type CURL_norm --jumps 5 --game alien --momentum-tau 1.0 --seed $seed --tag $tag
