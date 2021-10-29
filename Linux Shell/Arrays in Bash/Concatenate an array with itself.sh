i=0
while read -r line || [[ -n $line ]]
do
  arr[$i]="$line"
  (( i+=1 ))
done

new_arr=("${arr[@]}" "${arr[@]}" "${arr[@]}")
echo ${new_arr[@]}
