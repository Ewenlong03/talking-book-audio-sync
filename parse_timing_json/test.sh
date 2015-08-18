# /bin/bash

SN=$1

RAW_DATA_PATH="../../rawdata/NCE03"
MP3_FILE_PATH="$RAW_DATA_PATH/III-$SN.mp3"
LRC_FILE_PATH="$RAW_DATA_PATH/III-$SN.lrc"
#echo $MP3_FILE_PATH

python align-mp3-txt.py $MP3_FILE_PATH $LRC_FILE_PATH
