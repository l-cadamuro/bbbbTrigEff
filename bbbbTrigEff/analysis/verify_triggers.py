import ROOT
import collections
import sys 

year = 2018
filelistname = 'test_flist.txt'

if len(sys.argv) > 1:
    year = int (sys.argv[1])

if len(sys.argv) > 2:
    filelistname = sys.argv[2]

print "YEAR : ", year
print "File : ", filelistname

# triggers are structured as
# key -> name of the trigger
# value[0] -> list of seeds to be considered in OR
# value[1] -> min number of objects

triggers = collections.OrderedDict()
if year == 2016:

    triggers['HLT_QuadJet45_TripleBTagCSV_p087_v'] = (
        (['hltL1sQuadJetC50IorQuadJetC60IorHTT280IorHTT300IorHTT320IorTripleJet846848VBFIorTripleJet887256VBFIorTripleJet927664VBF', 'hltL1sQuadJetCIorTripleJetVBFIorHTT'], 1),
        (['hltQuadCentralJet45'],          4),
        (['hltQuadPFCentralJetLooseID45'], 4),
        (['hltBTagCaloCSVp087Triple'],     3),
    )

    triggers['HLT_DoubleJet90_Double30_TripleBTagCSV_p087_v'] = (
        (['hltL1sTripleJetVBFIorHTTIorDoubleJetCIorSingleJet'] ,  1),
        (['hltDoubleCentralJet90']                             ,  2),
        (['hltQuadCentralJet30']                               ,  4),
        (['hltDoublePFCentralJetLooseID90']                    ,  2),
        (['hltQuadPFCentralJetLooseID30']                      ,  4),
        (['hltBTagCaloCSVp087Triple']                          ,  2),
    )

elif year == 2017:
    
    triggers['HLT_HT300PT30_QuadJet_75_60_45_40_TripeCSV_p07_v'] = (
        (['hltL1sQuadJetC60IorHTT380IorHTT280QuadJetIorHTT300QuadJet']  ,  1),
        (['hltQuadCentralJet30']                                        ,  4),
        (['hltCaloJetsQuad30ForHt']                                     ,  0),   #not saved
        (['hltHtMhtCaloJetsQuadC30']                                    ,  0),   #not saved
        (['hltCaloQuadJet30HT300']                                      ,  1),
        (['hltBTagCaloCSVp05Double']                                    ,  2),
        (['hltPFCentralJetLooseIDQuad30']                               ,  4),
        (['hlt1PFCentralJetLooseID75']                                  ,  1),
        (['hlt2PFCentralJetLooseID60']                                  ,  2),
        (['hlt3PFCentralJetLooseID45']                                  ,  3),
        (['hlt4PFCentralJetLooseID40']                                  ,  4),
        (['hltPFCentralJetLooseIDQuad30forHt']                          ,  0),   #not saved
        (['hltHtMhtPFCentralJetsLooseIDQuadC30']                        ,  0),   #not saved
        (['hltPFCentralJetsLooseIDQuad30HT300']                         ,  1),
        (['hltBTagPFCSVp070Triple']                                     ,  3),
    )

    ## as above, this trigger was just renamed
    ## although note that this filter
    # (['hltL1sQuadJetC50to60IorHTT280to500IorHTT250to340QuadJet']     ,  1),
    ## was *NOT* used for part of RunC
    triggers['HLT_PFHT300PT30_QuadPFJet_75_60_45_40_TriplePFBTagCSV_3p0_v'] = (
        (['hltL1sQuadJetC60IorHTT380IorHTT280QuadJetIorHTT300QuadJet', 'hltL1sQuadJetC50to60IorHTT280to500IorHTT250to340QuadJet']   ,  1),
        (['hltQuadCentralJet30']                                         ,  4),
        (['hltCaloJetsQuad30ForHt']                                      ,  0),   #not saved
        (['hltHtMhtCaloJetsQuadC30']                                     ,  0),   #not saved
        (['hltCaloQuadJet30HT300']                                       ,  1),
        (['hltBTagCaloCSVp05Double']                                     ,  2),
        (['hltPFCentralJetLooseIDQuad30']                                ,  4),
        (['hlt1PFCentralJetLooseID75']                                   ,  1),
        (['hlt2PFCentralJetLooseID60']                                   ,  2),
        (['hlt3PFCentralJetLooseID45']                                   ,  3),
        (['hlt4PFCentralJetLooseID40']                                   ,  4),
        (['hltPFCentralJetLooseIDQuad30forHt']                           ,  0),   #not saved
        (['hltHtMhtPFCentralJetsLooseIDQuadC30']                         ,  0),   #not saved
        (['hltPFCentralJetsLooseIDQuad30HT300']                          ,  1),
        (['hltBTagPFCSVp070Triple']                                      ,  3),
    )

elif year == 2018:
    triggers['HLT_PFHT330PT30_QuadPFJet_75_60_45_40_TriplePFBTagDeepCSV_4p5_v'] = (
        (['hltL1sQuadJetC50to60IorHTT280to500IorHTT250to340QuadJet'],  1),
        (['hltQuadCentralJet30']                   , 4),
        (['hltCaloJetsQuad30ForHt']                , 0),  # not saved
        (['hltHtMhtCaloJetsQuadC30']               , 0),  # not saved
        (['hltCaloQuadJet30HT320']                 , 1),
        (['hltBTagCaloDeepCSVp17Double']           , 2),
        (['hltPFCentralJetLooseIDQuad30']          , 4),
        (['hlt1PFCentralJetLooseID75']             , 1),
        (['hlt2PFCentralJetLooseID60']             , 2),
        (['hlt3PFCentralJetLooseID45']             , 3),
        (['hlt4PFCentralJetLooseID40']             , 4),
        (['hltPFCentralJetLooseIDQuad30forHt']     , 0),  # not saved
        (['hltHtMhtPFCentralJetsLooseIDQuadC30']   , 0),  # not saved
        (['hltPFCentralJetsLooseIDQuad30HT330']    , 1),
        ## these in OR
        (['hltBTagPFDeepCSVp24Triple', 'hltBTagPFDeepCSV4p5Triple'] , 3),
    )


#################### open the input files

def parseInputFileList (fileName) :
    filelist = []
    with open (fileName) as fIn:
        for line in fIn:
            line = (line.split("#")[0]).strip()
            if line:
                filelist.append(line)
    return filelist

print '... running on file list', filelistname
files = parseInputFileList(filelistname)
print '... filelist contains', len(files), 'files'

ch = ROOT.TChain('checkTrg/trgObjTree')
for f in files:
    ch.Add(f)


### checking all triggers
results = collections.OrderedDict()
counts  = collections.OrderedDict()
for trgName, filterList in triggers.items():
    nEv = ch.GetEntries(
        '{trg} == 1'.format(trg=trgName)
    )
    counts[trgName]  = nEv
    results[trgName] = []
    for filterDesc in filterList:
        fltString = ' + '.join(filterDesc[0])
        print '({fltString}) < {nObj} && {trg} == 1'.format(fltString=fltString, nObj=filterDesc[1], trg=trgName)
        nEv = ch.GetEntries(
            '({fltString}) < {nObj} && {trg} == 1'.format(fltString=fltString, nObj=filterDesc[1], trg=trgName)
        )
        results[trgName].append(nEv)

errors = []
zerocount_errors = []
print "\n\n----------- SUMMARY -----------"
for idx, (trgName, values) in enumerate (results.items()):
    print '>>> ', trgName

    # tot counts
    count = counts[trgName]
    str_res = '[   OK]' if count > 0 else '[ERROR]'
    if count == 0:
        zerocount_errors.append((trgName, count))
    print '.. {res}  : counts = {count}'.format(res=str_res, count=count)
    print ".."

    ## filter check
    for istep in range(len(values)):
        result  = values[istep]
        str_res = '[   OK]' if result == 0 else '[ERROR]'
        if result != 0:
            errors.append((trgName, istep, result))
        print '.. {res}  : '.format(res=str_res), triggers[trgName][istep][0]
    print '\n'

if len(zerocount_errors) > 0:
    print '\n------ ERROR DETAILS [total counts] ------'
    for trgName, nerr in zerocount_errors:
        print '.. {trgName} >> {nerr} counts '.format(trgName=trgName, nerr=nerr)
    print ""

if len(errors) > 0:
    print '\n------ ERROR DETAILS [filters] ------'
    for trgName, istep, nerr in errors:
        print '.. {trgName}  >> {fil} >> {nerr} events '.format(trgName=trgName, fil=triggers[trgName][istep][0], nerr=nerr)
    print ""