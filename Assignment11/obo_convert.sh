#!/bin/sh

infile="goslim_plant.obo"
outfile="TEST_goslim_plant.terms.txt"

egrep '^\[Term\]|^\[Typedef\]|^id: |^name: |^namespace: |^def: ' $infile | sed 's/\[Term\]/||/g' | sed 's/\[Typedef\]/==/g'  | sed 's/id: /--/g' | sed 's/name: /--/g' | sed 's/def: /--/g' | sed 's/namespace: /--/g' | sed ':a;N;$!ba;s/\n//g' | sed 's/||/\n/g' | sed 's/==/\n==/g' | sed 's/--/\t/g' | grep -v '^==' | sed 's/^\t//'  > $outfile

#Extract lines that start with fields desired
#step1=$(egrep '^\[Term\]|^\[Typedef\]|^id: |^name: |^namespace: |^def: ' $infile)

#Replace any instance of '[Term]' with placeholder '||'
#step2=$(echo "$step1" | sed 's/\[Term\]/||/g')

# Replace any instance of '[Typedef]' with placeholder '=='
#step3=$(echo "$step2" | sed 's/\[Typedef\]/==/g')

# Replace field prefixes with placeholder '--'
#step4=$(echo "$step3" | sed 's/id: /--/g' )
#step5=$(echo "$step4" | sed 's/name: /--/g')
#step6=$(echo "$step5" | sed 's/def: /--/g')
#step7=$(echo "$step6" | sed 's/namespace: /--/g')

# Add new line characters between each record
#step8=$(echo "$step7" | sed ':a;N;$!ba;s/\n//g')

# Replace any '||' placeholders with newline char
#step9=$(echo "$step8" | sed 's/||/\n/g')

#add a newline char to the '==' placeholder
#step10=$(echo "$step9" | sed 's/==/\n==/g')

#replace '--' placeholder with tab char
#step11=$(echo "$step10" | sed 's/--/\t/g')

#grep only lines beginning with '==' (will not have records with a Typedef and not a Type)
#step12=$(echo "$step11" | grep -v '^==')


#step13=$(echo "$step12" | sed 's/^\t//')

#$step13 >> $outfile