#!/bin/bash

cd /bd_targaryen/users/jhu/spr
source /bd_targaryen/users/jhu/anaconda3/bin/activate
conda activate spr

tag=spr_epsilon_zeta
seed=4

echo "start running $tag with seed $seed"
python -m scripts.run --repeat_type 3  --repeat_coefficient 1 --eps-steps 100000 --noisy-nets 0 --spr 1 --game pong --momentum-tau 1.0 --seed $seed --tag $tag
