tag=$1
outfile=$2

if [ -z "$tag" ] ; then
    echo "... please provide a tag name"
    echo "... usage: source makeFileList.sh tag outfile"
    return
fi

if [ -z "$outfile" ] ; then
    echo "... please provide a output file name"
    echo "... usage: source makeFileList.sh tag outfile"
    return
fi

BASE=/eos/uscms/store/user/lcadamur/bbbbTrgEff/SingleMuon
LASTFLRD=$(ls ${BASE}/${tag}/ | sort -V | tail -n 1)
echo ${BASE}/${tag}/$LASTFLRD
NFLDR=`ls -1d ${BASE}/${tag}/$LASTFLRD | wc -l`
FLDTOUSE=`ls -1d ${BASE}/${tag}/$LASTFLRD/*`
# echo $NFLDR
if [ "$NFLDR" != "1" ] ; then
    echo ""
    echo "!!!! [WARNING] !!!!! Too many subfolders for ${tag} : ( ${BASE}/${tag}/$LASTFLRD ) "
    echo ""
fi

ls -v ${FLDTOUSE}/*.root > ${outfile}

## now replace with the server
sed -i.bak -e 's+/eos/uscms+root://cmsxrootd.fnal.gov/+g' ${outfile}
rm ${outfile}.bak