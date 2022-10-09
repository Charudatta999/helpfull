location_path=$1
host_list=$2

memory_repo=
cpu_repo=



	nl -n ln data.csv | sed 's/,/ /g' > $location_path/$host_asset/plot-data/mem.dat


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


