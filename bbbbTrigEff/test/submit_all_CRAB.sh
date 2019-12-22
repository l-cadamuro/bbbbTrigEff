#### 2016 datasets
# /SingleMuon/Run2016B-17Jul2018_ver1-v1/MINIAOD
# /SingleMuon/Run2016B-17Jul2018_ver2-v1/MINIAOD
# /SingleMuon/Run2016C-17Jul2018-v1/MINIAOD
# /SingleMuon/Run2016D-17Jul2018-v1/MINIAOD
# /SingleMuon/Run2016E-17Jul2018-v1/MINIAOD
# /SingleMuon/Run2016F-17Jul2018-v1/MINIAOD
# /SingleMuon/Run2016G-17Jul2018-v1/MINIAOD
# /SingleMuon/Run2016H-17Jul2018-v1/MINIAOD

#### 2017 datasets
# /SingleMuon/Run2017B-31Mar2018-v1/MINIAOD
# /SingleMuon/Run2017C-31Mar2018-v1/MINIAOD
# /SingleMuon/Run2017D-31Mar2018-v1/MINIAOD
# /SingleMuon/Run2017E-31Mar2018-v1/MINIAOD
# /SingleMuon/Run2017F-31Mar2018-v1/MINIAOD

#### 2018 datasets
# /SingleMuon/Run2018A-17Sep2018-v2/MINIAOD
# /SingleMuon/Run2018B-17Sep2018-v1/MINIAOD
# /SingleMuon/Run2018C-17Sep2018-v1/MINIAOD
# /SingleMuon/Run2018D-22Jan2019-v2/MINIAOD


TAG="fix2017"

###########################################################
#### 2016

# echo ".... launching 2016 ...."

# for DSET in \
# /SingleMuon/Run2016B-17Jul2018_ver1-v1/MINIAOD \
# /SingleMuon/Run2016B-17Jul2018_ver2-v1/MINIAOD \
# /SingleMuon/Run2016C-17Jul2018-v1/MINIAOD \
# /SingleMuon/Run2016D-17Jul2018-v1/MINIAOD \
# /SingleMuon/Run2016E-17Jul2018-v1/MINIAOD \
# /SingleMuon/Run2016F-17Jul2018-v1/MINIAOD \
# /SingleMuon/Run2016G-17Jul2018-v1/MINIAOD \
# /SingleMuon/Run2016H-17Jul2018-v1/MINIAOD ; do \

# REQNAME=${DSET}
# REQNAME=`echo "${DSET}" | tr - _`
# REQNAME=${REQNAME#"/"}
# REQNAME=${REQNAME%"/MINIAOD"}
# REQNAME=`echo ${REQNAME} | sed 's/\//_/'`
# REQNAME=${REQNAME}_${TAG}
# echo $REQNAME

# crab submit -c crab_cfg_2016.py \
#     General.requestName=${REQNAME} \
#     Data.outputDatasetTag=${REQNAME} \
#     Data.inputDataset=${DSET} \
#     Data.lumiMask="jsons/Cert_271036-284044_13TeV_23Sep2016ReReco_Collisions16_JSON.txt" \
#     JobType.psetName="analyze.py"
# done



# ###########################################################
# #### 2017

echo ".... launching 2017 ...."

for DSET in \
/SingleMuon/Run2017B-31Mar2018-v1/MINIAOD \
/SingleMuon/Run2017C-31Mar2018-v1/MINIAOD \
/SingleMuon/Run2017D-31Mar2018-v1/MINIAOD \
/SingleMuon/Run2017E-31Mar2018-v1/MINIAOD \
/SingleMuon/Run2017F-31Mar2018-v1/MINIAOD ; do \

REQNAME=${DSET}
REQNAME=`echo "${DSET}" | tr - _`
REQNAME=${REQNAME#"/"}
REQNAME=${REQNAME%"/MINIAOD"}
REQNAME=`echo ${REQNAME} | sed 's/\//_/'`
REQNAME=${REQNAME}_${TAG}
echo $REQNAME

crab submit -c crab_cfg_2017.py \
    General.requestName=${REQNAME} \
    Data.outputDatasetTag=${REQNAME} \
    Data.inputDataset=${DSET} \
    Data.lumiMask="jsons/Cert_294927-306462_13TeV_EOY2017ReReco_Collisions17_JSON.txt" \
    JobType.psetName="analyze.py"
done



###########################################################
#### 2018

# echo ".... launching 2018 ...."

# for DSET in \
# /SingleMuon/Run2018A-17Sep2018-v2/MINIAOD \
# /SingleMuon/Run2018B-17Sep2018-v1/MINIAOD \
# /SingleMuon/Run2018C-17Sep2018-v1/MINIAOD \
# /SingleMuon/Run2018D-22Jan2019-v2/MINIAOD ; do \

# REQNAME=${DSET}
# REQNAME=`echo "${DSET}" | tr - _`
# REQNAME=${REQNAME#"/"}
# REQNAME=${REQNAME%"/MINIAOD"}
# REQNAME=`echo ${REQNAME} | sed 's/\//_/'`
# REQNAME=${REQNAME}_${TAG}
# echo $REQNAME

# crab submit -c crab_cfg_2018.py \
#     General.requestName=${REQNAME} \
#     Data.outputDatasetTag=${REQNAME} \
#     Data.inputDataset=${DSET} \
#     Data.lumiMask="jsons/Cert_314472-325175_13TeV_17SeptEarlyReReco2018ABC_PromptEraD_Collisions18_JSON.txt" \
#     JobType.psetName="analyze.py"
# done