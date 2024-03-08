#!/bin/bash

cd /bd_targaryen/users/jhu/spr/
source /bd_targaryen/users/jhu/anaconda3/bin/activate
conda activate spr

tag=rainbow_simhash_repeat_c05
seed=4

echo "start running $tag with seed $seed"
python -m scripts.run --repeat_type 1 --spr 0 --game alien --momentum-tau 1.0 --seed $seed --tag $tag
