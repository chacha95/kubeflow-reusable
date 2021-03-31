img_name=mnist
ver=1.5v

# train
docker build -t "${img_name}_train:$ver" ./train
docker tag "${img_name}_train:$ver" "ckwlsgur20/${img_name}_train:$ver"
docker push ckwlsgur20/"${img_name}_train:$ver"

# test
docker build -t "${img_name}_test:$ver" ./test
docker tag "${img_name}_test:$ver" "ckwlsgur20/${img_name}_test:$ver"
docker push ckwlsgur20/"${img_name}_test:$ver"