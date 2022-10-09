location_path=$1
host_list=$2

memory_repo=/root/Akshata/Excel/mem_details.csv
cpu_repo=/root/Akshata/Excel/cpu_details.csv

while read host_asset;do
	Max_CPU=0
	Min_CPU=0
	Average_CPU=0
	echo $host_asset
	host_asset=`echo $host_asset| tr -d '\r'`
    mkdir -p $location_path/$host_asset/plot-data
	
	cpu_filename=$location_path/$host_asset/plot-data/cpu_time_and_usage_edr.csv
	read_byte_file_name=$location_path/$host_asset/plot-data/read_byte.csv
	write_byte_file_name=$location_path/$host_asset/plot-data/write_byte.csv
	resident_memory_filename=$location_path/$host_asset/plot-data/rss_time_and_usage_edr.csv


	nl -n ln resident_memory_filename | sed 's/,/ /g' > $location_path/$host_asset/plot-data/mem.dat


	gnuplot -e "set title 'usage graph';
	set term png; set xlabel 'time';set grid;
	set ylabel 'usage'; set output 'rss_memory.png';
	set boxwidth 0.2;
	set style fill solid;
	set xtics rotate;
	set ytics font 'Times-Roman,50';set lmargin 50;
	set terminal pngcairo size 15048,8440;
	plot '$location_path/$host_asset/plot-data/mem.dat'  using 1:3:xtic(2) with boxes"
	rm -rf $location_path/$host_asset/plot-data/mem.dat
done < $host_list

