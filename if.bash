if [[ 0 -gt $1 || $1 -gt 24 ]]; then
    echo "error!"
elif [[ 12 -gt $1  ]]; then
    echo "good morning!"
elif [[ $1 -ge 12 &&  18 -gt $1 ]]; then
    echo "good afternoon!"
else
    echo "good evening!"
fi

