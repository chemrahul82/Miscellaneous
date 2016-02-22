"""
Combine the sample_somatic.tsv files for for all radiogenomics samples to create a master spreadsheet
Author: Rahul K. Das
02/19/2016

"""

import os
import xlsxwriter
import csv
import subprocess
projDir = '/rawdata/projects/Radiogenomics/'
wb = xlsxwriter.Workbook('Radiogenomics_Somatic_02192016.xlsx')

sampleDirs = sorted([d for d in os.listdir(projDir) if (os.path.isdir(os.path.join(projDir, d)) and "pair_" in d)])

for i in range(len(sampleDirs)):
	if os.path.exists(os.path.join(projDir, sampleDirs[i], 'QC')):
 		qcDirs= [d for d in os.listdir(os.path.join(projDir, sampleDirs[i], 'QC')) if os.path.isdir(os.path.join(projDir, sampleDirs[i], 'QC', d))]
		for jdir in qcDirs:
			#find the most likely QC directory for finding somatic.tsv
			if (os.path.exists(os.path.join(projDir, sampleDirs[i], 'QC', jdir, 'Somatic_Variants', 'annovar_tmp')))\
				and ("High_String" not in jdir):
				#print sampleDirs[i]
				
				#make sure the number of somatic variants in the csv file are same to that in the final tsv file; if not something
				#wrong has happened during post-processing/annotations
				
				csvfile =  os.path.join(projDir, sampleDirs[i], 'QC', jdir, 'Somatic_Variants','somatic.csv')
				#csv_row_count = subprocess.check_output("wc -l < %s" %csvfile, shell=True)
				
				tsvfile = os.path.join(projDir, sampleDirs[i], 'QC', jdir, 'Somatic_Variants','%s_somatic.tsv' %sampleDirs[i])
				tsv_reader = csv.reader(open(tsvfile, 'rb'), delimiter='\t')
				#tsv_row_count = subprocess.check_output("wc -l < %s" %tsvfile, shell=True)	
				#
				#print csv_row_count, tsv_row_count
				#if csv_row_count+1 > tsv_row_count:
				#	if csv_row_count == 2:
				#	  	print "potential duplicate variants in %s" %sampleDirs[i]
				#	else:
				#		print "somatic vatiants got mistakenly discarded in %s" %sampleDirs[i]
				

				ws = wb.add_worksheet('%s' %sampleDirs[i])
				# Read the row data from the TSV file and write it to the XLSX file.
				for row, data in enumerate(tsv_reader):
					#print row
					ws.write_row(row, 0, data)

	
wb.close()
