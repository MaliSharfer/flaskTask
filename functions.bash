L=$1
R=$2

     greeting () {
       echo "mklkl"
       result=$2
       rs=`expr $result % 2`
       if [[ $1 -gt $2 ]]; then
         return 0 
       elif [[ $rs -eq 0 ]]; then
           echo "into if"
           echo $rs
           greeting $1 $( ( $result - 2 ) )
         else 
            greeting $1 $( ( $result - 1 ) )
       fi
       return 0
     }

greeting


