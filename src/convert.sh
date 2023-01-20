#!/bin/bash

convert_euv () {
    fc=`cat $1`
    #remove preamble
    core=${fc##*Artikel 1$'\n'}
    #remove subtitles from Articles
    core=`grep -v  "(ex-Artikel " <<< $core`
    echo $core
}

a=$(convert_euv "../legaldocs/euv_de.txt")
echo $a
