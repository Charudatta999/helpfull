#! /usr/bin/bash

FLAGS_PATTERN="i::o:r:h:"
# i - input path, o - oputput path to save graphs in , h - help/usgae
RES=""
OUT_PATH=""
IN_PATH=""

IP_FLAG=/bin/false
OP_FLAG=/bin/false
RES_FLAG=/bin/false

H_FLAG=/bin/false



input_path=`echo $1`
tmpfile=/tmp/`basename  $input_path | sed s/csv/dat/g `

if [ -z "$2" ];then
output_path=`echo $input_path | sed s/csv/png/g `
else
output_path=$2
fi

 nl -n ln $input_path | sed 's/,/ /g' > $tmpfile


  gnuplot -e "set title 'usage graph';
                 set term png; set xlabel 'time';set grid;
                 set ylabel 'usage'; set output '$output_path';
                 set boxwidth 0.2;
                 set style fill solid;
                 set xtics rotate;
                 set ytics font 'Times-Roman,50';set lmargin 50;
                 set terminal pngcairo size 15048,8440;
                 plot '$tmpfile'  using 1:3:xtic(2) with boxes"

rm -rf $tmpfile




function parse_args()
{
    # This function parses the arguments passed to the script and sets the variables
    
    while getopts $FLAGS_PATTERN FLAG
    do
        case $FLAG in
            i)
                input_path=$OPTARG
                IP_FLAG=/bin/true;;
            
            o)
                OUT_PATH=$OPTARG
                OP_FLAG=/bin/true;;
            
            r)
                RES=$OPTARG
                RES_FLAG=/bin/true;;
            
            h | *)
            usage
            exit 0;;
        esac
        
    done
}



function main(){
    parse_args "$@" #parsing arguments provided to script

    if [[ -z $OP_FLAG ]];
    then
        OUT_PATH=`pwd`
        echo " -o output Folder Path Not Specified, Using current directory: ${OUT_PATH}"
    fi
}
main "$@"
