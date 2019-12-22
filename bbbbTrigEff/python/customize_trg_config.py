import FWCore.ParameterSet.Config as cms

def customize_trg_config_2016(process):
    process.checkTrg.triggerList = cms.vstring(
        'HLT_QuadJet45_TripleBTagCSV_v',
        'HLT_DoubleJet90_Double30_TripleBTagCSV_v',
    )

    process.checkTrg.filterList = cms.vstring(
        #### HLT_QuadJet45_TripleBTagCSV_v
        ## the two below in OR
        'hltL1sQuadJetC50IorQuadJetC60IorHTT280IorHTT300IorHTT320IorTripleJet846848VBFIorTripleJet887256VBFIorTripleJet927664VBF',
        'hltL1sQuadJetCIorTripleJetVBFIorHTT',  # 1
        #
        'hltQuadCentralJet45',          # 4
        'hltQuadPFCentralJetLooseID45', # 4
        'hltBTagCaloCSVp087Triple',     # 3
        ###
        ### HLT_DoubleJet90_Double30_TripleBTagCSV_v
        'hltL1sTripleJetVBFIorHTTIorDoubleJetCIorSingleJet', #  1
        'hltDoubleCentralJet90',                             #  2
        'hltQuadCentralJet30',                               #  4
        'hltDoublePFCentralJetLooseID90',                    #  2
        'hltQuadPFCentralJetLooseID30',                      #  4
        'hltBTagCaloCSVp087Triple',                          #  2           
    )

def customize_trg_config_2017(process):
    process.checkTrg.triggerList = cms.vstring(
        'HLT_HT300PT30_QuadJet_75_60_45_40_TripeCSV_p07_v',
        'HLT_PFHT300PT30_QuadPFJet_75_60_45_40_TriplePFBTagCSV_3p0_v',
    )

    process.checkTrg.filterList = cms.vstring(
        'hltL1sQuadJetC60IorHTT380IorHTT280QuadJetIorHTT300QuadJet',  #  1
        'hltL1sQuadJetC50to60IorHTT280to500IorHTT250to340QuadJet',    #  1, replaces the above sometimes
        'hltQuadCentralJet30',                                        #  4
        'hltCaloJetsQuad30ForHt',                                     #  not saved
        'hltHtMhtCaloJetsQuadC30',                                    #  not saved
        'hltCaloQuadJet30HT300',                                      #  1
        'hltBTagCaloCSVp05Double',                                    #  2
        'hltPFCentralJetLooseIDQuad30',                               #  4
        'hlt1PFCentralJetLooseID75',                                  #  1
        'hlt2PFCentralJetLooseID60',                                  #  2
        'hlt3PFCentralJetLooseID45',                                  #  3
        'hlt4PFCentralJetLooseID40',                                  #  4
        'hltPFCentralJetLooseIDQuad30forHt',                          #  not saved
        'hltHtMhtPFCentralJetsLooseIDQuadC30',                        #  not saved
        'hltPFCentralJetsLooseIDQuad30HT300',                         #   1
        'hltBTagPFCSVp070Triple',                                     #  3
    )


def customize_trg_config_2018(process):
    print "... trigger configuration customised for the year 2018"

    process.checkTrg.triggerList = cms.vstring(
        'HLT_PFHT330PT30_QuadPFJet_75_60_45_40_TriplePFBTagDeepCSV_4p5_v'
    )

    process.checkTrg.filterList = cms.vstring(
        'hltL1sQuadJetC50to60IorHTT280to500IorHTT250to340QuadJet',  #  1
        'hltQuadCentralJet30',                  #  4
        'hltCaloJetsQuad30ForHt',               #  not saved
        'hltHtMhtCaloJetsQuadC30',              #  not saved
        'hltCaloQuadJet30HT320',                #  1
        'hltBTagCaloDeepCSVp17Double',          #  2
        'hltPFCentralJetLooseIDQuad30',         #  4
        'hlt1PFCentralJetLooseID75',            #  1
        'hlt2PFCentralJetLooseID60',            #  2
        'hlt3PFCentralJetLooseID45',            #  3
        'hlt4PFCentralJetLooseID40',            #  4
        'hltPFCentralJetLooseIDQuad30forHt',    #  not saved
        'hltHtMhtPFCentralJetsLooseIDQuadC30',  #  not saved
        'hltPFCentralJetsLooseIDQuad30HT330',   #   1
        ## these in OR
        'hltBTagPFDeepCSVp24Triple',
        'hltBTagPFDeepCSV4p5Triple', # 3
    )
