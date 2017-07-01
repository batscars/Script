import os

respath = "/zhangbin/fddb/dynamic-result/"
parm = ["0.500000"]
semi_parm = ["0.302000", "0.303000", "0.304000", "0.306000", "0.307000"]

for pro in parm:
  for semi_pro in semi_parm:
    resname = "1.000000_" + pro + "_" + semi_pro + "_"
    detfile = respath + resname + "out.txt"
    rocfile = resname + "DiscROC.txt"
    os.chdir("/zhangbin/npd_code/detection")
    os.system("./nickle fddb_normalize 1.0 %s %s"%(pro, semi_pro)) 
    os.chdir("/zhangbin/fddb/evaluation_dynamic")
    os.system("./evaluate -d %s -r %s"%(detfile, resname))
    os.system("cp %s /zhangbin/npd_code/normalization/evaluate_res/add_index"%rocfile)
 