img_name=mnist_local
ver=0.1

# train
docker build -t "${img_name}:$ver" .
docker tag "${img_name}:$ver" "ckwlsgur20/${img_name}:$ver"
docker push ckwlsgur20/"${img_name}:$ver"