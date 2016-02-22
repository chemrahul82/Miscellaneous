"""
re run TVC on all radiogenomics samples using the latest settings and also get full annovar annotations
Author: Rahul K. Das
Date: 02/19/2016
How to run: nohup python -u radiogenomics_TVC_rerun.py <startidx for sample list> >endidx for sample list> > <nohup_1.out> 2>&1 &

"""


import os
#import time
projDir = '/rawdata/projects/Radiogenomics/'
#sample directories
sampleDirs = sorted([d for d in os.listdir(projDir) if (os.path.isdir(os.path.join(projDir, d)) and "pair_" in d)])
#print (sampleDirs)
#time.sleep(60)
def tvc_rerun(start, end):
	for i in range(start,end):
		print "Started TVC Rerun for %s" %sampleDirs[i]
		if os.path.exists(os.path.join(projDir, sampleDirs[i], 'QC')):
 			qcDirs= [d for d in os.listdir(os.path.join(projDir, sampleDirs[i], 'QC')) if os.path.isdir(os.path.join(projDir, sampleDirs[i], 'QC', d))]
			for jdir in qcDirs:
				#delete High_String directories
				if "High_String" in jdir:
					hsDir = os.path.join(projDir, sampleDirs[i], 'QC', jdir)
					os.system('rm -rf %s' %hsDir)
	
		#remove old sge.log files
		sge = os.path.join(projDir, sampleDirs[i], 'sge.log')
		os.system('rm %s' %sge)

		#rerun TVC
		sample_json = os.path.join(projDir, sampleDirs[i], '%s.json' %sampleDirs[i])
		os.system('/rawdata/scripts/TRI_Scripts/QC/QC_sample.py -j %s -C' %sample_json) 
	return	

if __name__ == "__main__":
	start = sys.argv[1]
	end = sys.argv[2]
	tvc_rerun(start, end)
