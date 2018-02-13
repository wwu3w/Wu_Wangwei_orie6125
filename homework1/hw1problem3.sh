filename='namefilelist'
filelines=`cat $filename`

for line in $filelines ; do
	newline=`echo $line | sed 's/.txt//;'` 
	sed -E -i 's/[ \t]+/,/1' $line
	sed -E -i 's/[ \t]+/-/1' $line
	sed -E -i 's/.$/ /' $line
	sed -E -i 's/[ \t]+$//' $line
	newline2=`echo $newline | sed 's/taqtrade//;'` 
	sed -E -i "s/$/,$newline2/" $line
done
