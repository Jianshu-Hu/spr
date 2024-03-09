#!/bin/bash

cd /bd_targaryen/users/jhu/spr
source /bd_targaryen/users/jhu/anaconda3/bin/activate
conda activate spr

tag=rainbow_epsilon_end_simhash_c05
seed=5

echo "start running $tag with seed $seed"
python -m scripts.run --repeat_type 1  --repeat_coefficient 0.5 --eps-steps 100000 --noisy-nets 0 --spr 0 --game alien --momentum-tau 1.0 --seed $seed --tag $tag
