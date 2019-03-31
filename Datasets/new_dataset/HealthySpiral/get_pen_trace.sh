for filename in *.jpg; 
do 
	file=$(echo $filename | cut -d'.' -f1); 
	./extractPen $file > ./filtered/$filename; 
done
