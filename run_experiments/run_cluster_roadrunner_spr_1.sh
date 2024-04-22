#!/bin/bash

cd /bd_targaryen/users/jhu/spr
source /bd_targaryen/users/jhu/anaconda3/bin/activate
conda activate spr

tag=spr_frame_skip_2_simhash_repeat_c05
seed=1

echo "start running $tag with seed $seed"
python -m scripts.run --repeat_type 1 --repeat_coefficient 0.5 --spr 1 --game road_runner --momentum-tau 1.0 --seed $seed --tag $tag
