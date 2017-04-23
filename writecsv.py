import csv

with open("asthma_discharges_12_14.csv", "w", newline ='') as fi:
	writer = csv.writer(fi, delimiter=",")
	data = [['ZIP Code', 'Discharges', 'Discharge Rate'],
		['10301','367','30.2'],
		['10302','168','28.8'],
		['10303','281','34.8'],
		['10304','399','31.3'],
		['10305','216','17.2'],
		['10306','259','15.5'],
		['10307','44','10.2'],
		['10308','75','9.0'],
		['10309','95','9.2'],
		['10310','212','28.3'],
		['10312','206','11.7'],
		['10314','317','12.3'],
		['11004','50','12.6'],
		['11005','13','15.1'],
		['11101','228','26.7'],
		['11102','257','24.0'],
		['11103','100','8.9'],
		['11104','108','12.8'],
		['11105','155','14.2'],	
		['11106','248','20.6'],
		['11109','0','0'],
		['11354','218','12.5'],
		['11355','252','9.7'],
		['11356','92','12.4'],
		['11357','91','7.5'],
		['11358','97','8.4'],
		['11359','0','0'],
		['11360','63','11.0'],
		['11361','92','10.4'],
		['11362','36','6.4'],
		['11363','20','9.2'],
		['11364','86','8.0'],
		['11365','133','10.3'],
		['11366','36','8.4'],
		['11367','210','16.6'],
		['11368','623','18.0'],
		['11369','191','16.5'],
		['11370','147','16.3'],
		['11372','262','12.8'],
		['11373','363','11.5'],
		['11374','167','12.4'],
		['11375','221',	'10.5'],
		['11377','361',	'13.2'],
		['11378','125','11.8'],
		['11379','154',	'14.1'],
		['11385','601',	'19.9'],
		['11411','109','19.9'],
		['11412','275',	'26.0'],
		['11413','259','21.9'],
		['11414','127','15.9'],
		['11415','93','15.6'],
		['11416','180','23.5'],
		['11417','169','19.0'],
		['11418','217','19.6'],
		['11419','250','17.7'],
		['11420','264','19.0'],
		['11421','214','17.6'],
		['11422','194','20.2'],
		['11423','167','18.8'],
		['11426','65','11.3'],
		['11427','148','21.3'],
		['11428','103','17.7'],
		['11429','168','22.1'],
		['11430','0','0'],
		['11432','345','18.0'],
		['11433','324','31.3'],
		['11434','511','28.0'],
		['11435','320','19.5'],
		['11436','153','27.5'],
		['11691','558','29.8'],
		['11692','158','26.2'],
		['11693','94','24.8'],
		['11694','91','14.3'],
		['11697','13','10.5']]
	writer.writerows(data)
