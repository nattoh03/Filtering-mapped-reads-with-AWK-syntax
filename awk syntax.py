########### AWK SYNTAX  ###############
## pwd
/home/nattohz/
## ls 
## get into the correct folder
cd ./practical_folder/awk
## ls 
## ensure you have a file e.g. gene features format file ( with extension .gff) such as anopheles.gff
## run the commands as follows for each function indicated

#### 1
#### awk syntax to identify number of columns a file has, this prints 9 fields separated by a tab
awk -F "\t" '{print NF}' anopheles.gff

#### 2a
#### extract columns based on a field from a file, e.g. all entries for chromosome 2 only
awk -F "\t" '$1=="chr2" {print $0}' anopheles.gff

#### 2b
#### combine extraction of columns based on a field from a file, e.g. all entries for column 1 and 3 
awk -F "\t" '$1=="chr2" && $3="gene"' anopheles.gff

#### 3
#### extract various fields from a file 
awk -F "\t" '{print $1, $3, $6, $9}' anopheles.gff
## observation, the output above is not in tab delimited, hence use OFS

#### 4
#### extract various fields from a file and retain its tab delimited format 
awk -F "\t" 'BEGIN{OFS="\t"}{print $1, $3, $6, $9}' anopheles.gff

#### 5
#### print out rows and not columns, the command print chrom2 plus all rows with genes in column 3
awk -F "\t" '$1=="chr2" || $3=="gene"' anopheles.gff

#### 6
#### Filter the output based on certain threshold
awk -F "\t" '$1=="chr2" && $3=="gene" && $4<1100' anopheles.gff

#### 7
#### Filter to obtain the length of repeats in a file, NB: this is not a bed file
awk -F "\t" '$3=="repeat" {print $5-$4+1}' anopheles.gff
awk -F "\t" '$4=="repeat" {print $3-$2}' anopheles.bed ## for a bed file

#### 8
#### Filter to obtain the total length of repeats in a file
awk -F "\t" 'BEGIN{sum=0} $3=="repeat" {sum=sum+ $5-$4+1} END {print sum}' anopheles.gff

#### 9
#### obtain the means of genes
awk -F "\t" 'BEGIN{sum=0; count=0} $3=="gene" {sum=+$6; count ++} END {print sum/count}' anopheles.gff
