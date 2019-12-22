#ifndef TRGFILTERPRINTER_CC
#define TRGFILTERPRINTER_CC

#include "FWCore/Framework/interface/EDAnalyzer.h"
#include "FWCore/Utilities/interface/InputTag.h"
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDProducer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/Framework/interface/ESHandle.h"
#include "FWCore/Framework/interface/EventSetup.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"
#include "FWCore/ServiceRegistry/interface/Service.h"

#include "DataFormats/Common/interface/Handle.h"
#include "DataFormats/Math/interface/LorentzVector.h"
#include "DataFormats/Common/interface/TriggerResults.h"

#include "DataFormats/HLTReco/interface/TriggerObject.h"
#include "DataFormats/PatCandidates/interface/TriggerObjectStandAlone.h"

#include "HLTrigger/HLTcore/interface/HLTConfigProvider.h"

#include "TTree.h"

#include <iostream>
#include <vector>
#include <string>
#include <unordered_map>

using namespace edm;
// using namespace l1t;
using namespace reco;
using namespace std;

// class filter_counter {
//     public:
//         filter_counter(std::vector<std::string> filterlist, int nmax=6);
//         ~filter_counter();
//         void feed(string filtername);
//     private:
//         std::vector<std::string> filternames_;
//         std::vector<std::vector<int> > filtercounts_; // filtercounts_[iname][incounts] 
//         int nmax_;
// };

// filter_counter::filter_counter(std::vector<std::string> filterlist, int nmax=6)
// {
//     nmax_ = nmax;
//     filternames_ = filterlist;
//     filtercounts_.resize(filternames_.size());
//     for (size_t ifilter = 0; ifilter < filternames_.size(); ++ifilter)
//     {
//         filternames_.at(ifilter) = std::vector<int>(nmax_, 0);
//     }
// }



class trgFilterPrinter : public edm::EDAnalyzer {
    public:
        explicit trgFilterPrinter(const edm::ParameterSet&);
        virtual ~trgFilterPrinter(){};

    private:
        //----edm control---
        virtual void beginJob();
        virtual void beginRun(edm::Run const&, edm::EventSetup const&);
        virtual void analyze(const edm::Event&, const edm::EventSetup&);
        virtual void endJob();
        virtual void endRun(edm::Run const&, edm::EventSetup const&){};

        void reset();
        bool getOR();

        static std::vector<string> remove_duplicates(std::vector<string> vIn);

        bool verbose_;

        const edm::EDGetTokenT< pat::TriggerObjectStandAloneCollection > triggerObjectsToken_;
        const edm::EDGetTokenT< edm::TriggerResults >                    triggerBitsToken_;

        HLTConfigProvider hltConfig_;
        edm::InputTag trgprocessName_;

        std::unordered_map <string, int> trgs_of_interest_; // maps the trg name to the idx of the HLT vector
        std::vector<string>    trgs_of_interest_names_; // the keys of the above
        std::vector<long long> trgs_of_interest_counts_; // the counts of the above
        long long tot_evts_;

        std::vector<string> filters_of_interest_names_;

        // and the associated filters - counts stored in a TTree
        TTree *tree_;

        // branches to save in the output
        std::vector<int> trg_pass_; // one int (0/1) for every trigger of interest
        std::vector<int> filter_count_; // one int to count num objects that pass a certain filer

        unsigned long long int event_;
        int       run_;
        int       lumi_;

};


trgFilterPrinter::trgFilterPrinter(const edm::ParameterSet& iConfig):
    triggerObjectsToken_ (consumes< pat::TriggerObjectStandAloneCollection >  (iConfig.getParameter<edm::InputTag>("triggerObjects"))),
    triggerBitsToken_    (consumes< edm::TriggerResults >                     (iConfig.getParameter<edm::InputTag>("triggerResults")))
{
    trgprocessName_            = iConfig.getParameter<edm::InputTag>("triggerResults");
    trgs_of_interest_names_    = iConfig.getParameter<std::vector<string>> ("triggerList");
    filters_of_interest_names_ = iConfig.getParameter<std::vector<string>> ("filterList");

    // remove possible duplicates
    trgs_of_interest_names_    = remove_duplicates(trgs_of_interest_names_);
    filters_of_interest_names_ = remove_duplicates(filters_of_interest_names_);

    verbose_ = iConfig.getParameter<bool>("verbose");

    // loop through all the names
    for (auto s : trgs_of_interest_names_)
    {
        trgs_of_interest_[s] = -1; // invalid ref
        trgs_of_interest_counts_.push_back(0); // 0 counts at startup
    }

    tot_evts_ = 0;
}

std::vector<string> trgFilterPrinter::remove_duplicates(std::vector<string> vIn)
{
    std::vector<string> vOut;
    for (string s : vIn)
    {
        if (std::find(vOut.begin(), vOut.end(), s) == vOut.end())
            vOut.push_back(s);
        else
            cout << "[INFO] : " << s << " found as duplicated and removed" << endl;
    }
    return vOut;
}

void trgFilterPrinter::beginJob()
{
    edm::Service<TFileService> fs;
    tree_ = fs -> make<TTree>("trgObjTree", "trgObjTree");

    tree_->Branch("event", &event_);
    tree_->Branch("run",   &run_);
    tree_->Branch("lumi",  &lumi_);


    trg_pass_.resize(trgs_of_interest_names_.size()); // one counter per trigger
    filter_count_.resize(filters_of_interest_names_.size()); // one counter per filters

    // set the branches in the tree
    for (size_t it = 0; it < trgs_of_interest_names_.size(); ++it)
    {
        string bname = trgs_of_interest_names_.at(it);
        cout << ".... new branch (TRG) : " << bname << endl;
        tree_->Branch(bname.c_str(), &(trg_pass_.at(it)));
    }

    for (size_t iflt = 0; iflt < filters_of_interest_names_.size(); ++iflt)
    {
        string bname = filters_of_interest_names_.at(iflt);
        cout << ".... new branch (FILTER): " << bname << endl;
        tree_->Branch(bname.c_str(), &(filter_count_.at(iflt)));
    }
}

void trgFilterPrinter::reset()
{
    for (size_t i = 0; i < trg_pass_.size(); ++i)
        trg_pass_.at(i) = 0;

    for (size_t i = 0; i < filter_count_.size(); ++i)
        filter_count_.at(i) = 0;
}

bool trgFilterPrinter::getOR()
{
    for (auto c : trg_pass_)
    {
        if (c > 0)
            return true;
    }
    return false;
}

void trgFilterPrinter::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{
    reset(); // all counters of the output tree set to 0

    event_ = iEvent.id().event();
    run_   = iEvent.id().run();
    lumi_  = iEvent.luminosityBlock();

    tot_evts_ += 1;

    edm::Handle<pat::TriggerObjectStandAloneCollection> triggerObjectsH;
    iEvent.getByToken(triggerObjectsToken_, triggerObjectsH);  
    const pat::TriggerObjectStandAloneCollection& triggerObjects = (*triggerObjectsH.product());

    edm::Handle<edm::TriggerResults> triggerBitsH;
    iEvent.getByToken(triggerBitsToken_, triggerBitsH);
    const edm::TriggerNames &trg_names = iEvent.triggerNames(*triggerBitsH);

    // std::string my_HLT = "HLT_PFHT330PT30_QuadPFJet_75_60_45_40_TriplePFBTagDeepCSV_4p5_v";
    // cout << " --- size of triggerBitsH is " << triggerBitsH->size() << endl; // same size as the full list printed below

    // ------------------------------
    // check the trigger pass/fail

    for (size_t itrg = 0; itrg < trgs_of_interest_names_.size(); ++itrg)
    {
        string name = trgs_of_interest_names_.at(itrg);
        int hlt_idx = trgs_of_interest_[name];
        bool pass = false;
        if (hlt_idx >= 0)
            pass = triggerBitsH->accept(hlt_idx);

        // update counts
        if (pass){
            trgs_of_interest_counts_.at(itrg) += 1;
            trg_pass_.at(itrg) = 1; // flag this event as passed
        }
    }

    // ------------------------------
    // check the trigger objects count

    for (size_t idxto = 0; idxto < triggerObjects.size(); ++idxto)
    {
        pat::TriggerObjectStandAlone obj = triggerObjects.at(idxto);
        obj.unpackPathNames(trg_names);
        obj.unpackFilterLabels(iEvent, *triggerBitsH);

        // std::vector<std::string> pathNamesAll  = obj.pathNames(false);
        // std::vector<std::string> pathNamesLast = obj.pathNames(true);

        // cout << "========= pathNamesAll ========= " << endl;
        // for (auto pn : pathNamesAll)
        //     cout << " ++ " << pn << endl;

        // cout << endl;
        // cout << "========= pathNamesLast ========= " << endl;
        // for (auto pn : pathNamesLast)
        //     cout << " ++ " << pn << endl;

        for (size_t ifilter = 0; ifilter < filters_of_interest_names_.size(); ++ifilter)
        {
            string fname = filters_of_interest_names_.at(ifilter);
            if (obj.hasFilterLabel(fname.c_str()))
                filter_count_.at(ifilter) += 1;
        }
    }

    if (getOR())
        tree_->Fill(); // only save info for events that passed a trigger

}

void trgFilterPrinter::beginRun(edm::Run const& iRun, edm::EventSetup const& iSetup){

    bool changedConfig = false;
 
    if(!hltConfig_.init(iRun, iSetup, trgprocessName_.process(), changedConfig)){
        edm::LogError("HLTMatchingFilter") << "Initialization of HLTConfigProvider failed!!"; 
        return;
    }
    else
    {
        // clear the trgs_of_interest_ map
        for (auto it = trgs_of_interest_.begin(); it != trgs_of_interest_.end(); it++ ){
            it->second = -1;
        }

        if (verbose_){
            cout << "=== Marked a change in the HLT menu . Run " << iRun.run() << endl;
            cout << "== Here are all the triggers in this run" << endl;
        }
        for(size_t j = 0; j < hltConfig_.triggerNames().size(); j++)
        {
            string pathName = hltConfig_.triggerNames()[j];
            if (verbose_) cout << j << " .... : " << pathName << endl;

            // does this trigger match the desired name?
            for (auto tname : trgs_of_interest_names_){
                if (pathName.find(tname) != std::string::npos)
                {
                    int old_idx = trgs_of_interest_.at(tname);
                    if (old_idx >= 0) // shouldn't be a valid one
                    {
                        edm::LogError("trgFilterPrinter") << "Double match for desired trg name found " << old_idx; 
                    }
                    trgs_of_interest_.at(tname) = j;
                    if (verbose_) cout << "  ^^^ flagged as interesting " << endl;
                }
            }
        } 
    }
}

void trgFilterPrinter::endJob()
{
    cout << "-------------- here is the count summary ------------- " << endl; 
    cout << "... TOTAL processed : " << tot_evts_ << endl;
    for (size_t itrg = 0; itrg < trgs_of_interest_names_.size(); ++itrg)
    {
        auto name   = trgs_of_interest_names_.at(itrg);
        auto counts = trgs_of_interest_counts_.at(itrg);
        cout << "..... " << name << "   : " << counts << endl;
    }
}


#include <FWCore/Framework/interface/MakerMacros.h>
DEFINE_FWK_MODULE(trgFilterPrinter);

#endif