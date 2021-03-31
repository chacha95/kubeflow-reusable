img_name=mnist
ver=1.7v

# train
docker build -t "${img_name}:$ver" .
docker tag "${img_name}:$ver" "ckwlsgur20/${img_name}:$ver"
docker push ckwlsgur20/"${img_name}:$ver"