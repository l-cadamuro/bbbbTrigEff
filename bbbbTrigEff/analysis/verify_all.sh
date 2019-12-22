# for d in \
#     SingleMuon_Run2016B_17Jul2018_ver2_v1 \
#     SingleMuon_Run2016C_17Jul2018_v1 \
#     SingleMuon_Run2016D_17Jul2018_v1 \
#     SingleMuon_Run2016E_17Jul2018_v1 \
#     SingleMuon_Run2016F_17Jul2018_v1 \
#     SingleMuon_Run2016G_17Jul2018_v1 \
#     SingleMuon_Run2016H_17Jul2018_v1 ; do \
# echo $d
# python verify_triggers.py 2016 ../filelist/${d}.txt; done

for d in \
    SingleMuon_Run2017B_31Mar2018_v1 \
    SingleMuon_Run2017C_31Mar2018_v1 \
    SingleMuon_Run2017D_31Mar2018_v1 \
    SingleMuon_Run2017E_31Mar2018_v1 \
    SingleMuon_Run2017F_31Mar2018_v1 ; do \
echo $d
python verify_triggers.py 2017 ../filelist/${d}.txt; done

# for d in \
#     SingleMuon_Run2018A_17Sep2018_v2_v2 \
#     SingleMuon_Run2018B_17Sep2018_v1_v2 \
#     SingleMuon_Run2018C_17Sep2018_v1_v2 \
#     SingleMuon_Run2018D_22Jan2019_v2_v2 ; do \
# echo $d
# python verify_triggers.py 2018 ../filelist/${d}.txt; done