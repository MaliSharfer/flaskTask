case "$1" in
       (gif)
         echo 'It is gif!'
         ;;
       (jpg)
         echo 'It is jpg!'
         ;;
       (png)
         echo "It is png!" && exit 1
       ;;
       (*)
         echo "$1 is not an image"
       ;;
     esac