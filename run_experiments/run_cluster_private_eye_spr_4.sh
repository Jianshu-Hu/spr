#!/bin/bash

cd /bd_targaryen/users/jhu/spr
source /bd_targaryen/users/jhu/anaconda3/bin/activate
conda activate spr

tag=spr_simhash_repeat_c01
seed=4

echo "start running $tag with seed $seed"
python -m scripts.run --repeat_type 1  --repeat_coefficient 0.1 --eps-steps 2001 --noisy-nets 1 --spr 1 --game private_eye --momentum-tau 1.0 --seed $seed --tag $tag
