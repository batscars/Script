respath="/zhangbin/fddb/dynamic-result/"
parm="0.500000"
semi_parm="0.302000 0.303000 0.304000 0.306000 0.307000"
for pro in $parm
do
  for semi_pro in $semi_parm
  do
    resname="1.000000_"$pro"_"$semi_pro"_"
    echo $resname
    detfile=${respath}${resname}"out.txt"
    echo $detfile
    rocfile=${resname}"DiscROC.txt"
    cd /raid/zhangzhaofeng/npd_code/detection
    wait 
    ./nickle fddb_normalize 1.0 $pro $semi_pro 
    wait  
    cd /raid/zhangzhaofeng/fddb/evaluation_dynamic
    wait 
    ./evaluate -d ${detfile} -r ${resname}
    wait
    cp ${rocfile} /raid/zhangzhaofeng/npd_code/normalization/evaluate_res/add_index
    wait
  done
done
 
