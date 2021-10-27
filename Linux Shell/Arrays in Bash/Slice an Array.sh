i=0
while read line
do
  arr[$i]=$line
  (( i+=1 ))
done

echo ${arr[@]:3:5}
