#!/bin/bash

cd /bd_targaryen/users/jhu/spr/
source /bd_targaryen/users/jhu/anaconda3/bin/activate
conda activate spr

tag=spr
seed=5

echo "start running $tag with seed $seed"
python -m scripts.run --repeat_type 0 --repeat_coefficient 0.3 --spr 1 --game alien --momentum-tau 1.0 --seed $seed --tag $tag
