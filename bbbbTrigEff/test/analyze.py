# define basic process
import FWCore.ParameterSet.Config as cms
import FWCore.ParameterSet.VarParsing as VarParsing
import os

process = cms.Process("checkTrg")

# import standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')

process.load('Configuration.StandardSequences.EndOfProcess_cff')

options = VarParsing.VarParsing ('analysis')
options.inputFiles = []

options.register ('year',
                  2018, # default value
                  VarParsing.VarParsing.multiplicity.singleton, # singleton or list
                  VarParsing.VarParsing.varType.int,            # string, int, or float
                  "Year of the data taking")
options.register ('isData',
                  1, # default value
                  VarParsing.VarParsing.multiplicity.singleton, # singleton or list
                  VarParsing.VarParsing.varType.int,            # string, int, or float
                  "Is this real data (0 or 1)")
options.register ('onCRAB',
                  0, # default value
                  VarParsing.VarParsing.multiplicity.singleton, # singleton or list
                  VarParsing.VarParsing.varType.int,            # string, int, or float
                  "Set to 1 if running on CRAB")

options.parseArguments()

### switches 
is_data = False if options.isData == 0 else True
year    = options.year

print '... running for the year : ', year
print '... is this data ?       : ', is_data

# input
process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(100000)
)

if options.inputFiles:
    Source_Files = cms.untracked.vstring(options.inputFiles)
else:
    Source_Files = cms.untracked.vstring(
        '/store/data/Run2018A/SingleMuon/MINIAOD/17Sep2018-v2/00000/11697BCC-C4AB-204B-91A9-87F952F9F2C6.root',
    )

process.source = cms.Source("PoolSource",
    fileNames = Source_Files
)

## no need to use this on CRAB (onCRAB == 1), it will take care of handling the JSON filter
if is_data and options.onCRAB == 0:
    print '.... configuring manually the JSON filter for the year', year
    if year == 2016:
        jsonfile = 'jsons/Cert_271036-284044_13TeV_23Sep2016ReReco_Collisions16_JSON.txt'
    elif year == 2017:
        jsonfile = 'jsons/Cert_294927-306462_13TeV_EOY2017ReReco_Collisions17_JSON.txt'
    elif year == 2018:
        jsonfile = 'jsons/Cert_314472-325175_13TeV_17SeptEarlyReReco2018ABC_PromptEraD_Collisions18_JSON.txt'

    ## restrict the lumi sections
    import FWCore.PythonUtilities.LumiList as LumiList
    myLumis = LumiList.LumiList(filename = jsonfile).getCMSSWString().split(',')
    process.source.lumisToProcess = cms.untracked.VLuminosityBlockRange()
    process.source.lumisToProcess.extend(myLumis)

process.TFileService = cms.Service('TFileService',
    fileName = cms.string('trigger_obj_tree.root')
)

process.checkTrg = cms.EDAnalyzer("trgFilterPrinter",
    triggerObjects = cms.InputTag("slimmedPatTrigger"),
    triggerResults = cms.InputTag("TriggerResults", "", "HLT"),
    triggerList = cms.vstring(),
    filterList  = cms.vstring(),
    verbose     = cms.bool(False),
)

## will update the trigger and filter list
from bbbbTrigEff.bbbbTrigEff.customize_trg_config import *

if year == 2016:
    customize_trg_config_2016(process)
elif year == 2017:
    customize_trg_config_2017(process)
elif year == 2018:
    customize_trg_config_2018(process)
else:
    raise RuntimeError("year not valid")

process.torun = cms.Path(
    process.checkTrg
)

process.schedule = cms.Schedule(process.torun)


##### screen output stuff
process.options = cms.untracked.PSet(
    wantSummary = cms.untracked.bool(True),
)

# Silence output
process.load("FWCore.MessageService.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = 1000
