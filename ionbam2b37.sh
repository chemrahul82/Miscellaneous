#convert contigs of ion torrent bam files to b37 format
#ion torrent uses b37 human reference, but appends "chr" infront of contig numbers
#this creates compatibility issue with GATK tools
#Rahul K. Das
#Feb 2016

#input and converted bam absolute paths
input_bam=''
converted_bam=''

printf "converting contig conventions\n"
samtools view -H ${input.bam} \
| sed -e 's/SN:chr\([0-9XY]\)/SN:\1/' -e 's/SN:chrM/SN:MT/' \
| samtools reheader - ${input.bam} > ${converted.bam}

printf "creating bam idx file\n"
samtools index ${converted.bam}
