
factorial()
{
       
    if [ $1 -gt $2 ]; then
       return
    fi
    if [[ $(( $1 % 2 )) -eq 0 ]]; then
        echo $1
        factorial $(($1 + 2)) $2
    else
        factorial $(($1 + 1)) $2
    fi
}
main(){
   echo $FUNCNAME
   factorial $1 $2

}
main $1 $2
