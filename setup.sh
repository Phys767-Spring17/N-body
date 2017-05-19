export_book() {
    export PYTHONPATH=:`pwd`/book
    if [ $? -eq 0 ]; then
        echo -e "\n\t book has been exported to PYTHONPATH"
        echo -e "\n\t \$PYTHONPATH=$PYTHONPATH\n"
    else
        echo -e "\n\t book has not been exported to PYTHONPATH"
        echo -e "\n\t $PYTHONPATH\n"
    fi
}

export_book
