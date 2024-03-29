import FWCore.ParameterSet.Config as cms

from DQMServices.Components.DQMMessageLogger_cfi import *
from DQMServices.Components.DQMDcsInfo_cfi import *
from DQMServices.Components.DQMEventInfo_cff import *
from DQMServices.Components.DQMFastTimerService_cff import *

from DQMOffline.Ecal.ecal_dqm_source_offline_cff import *
from DQM.HcalMonitorModule.hcal_dqm_source_fileT0_cff import *
from DQM.SiStripMonitorClient.SiStripSourceConfigTier0_cff import *
from DQM.SiPixelCommon.SiPixelOfflineDQM_source_cff import *
from DQM.DTMonitorModule.dtDQMOfflineSources_cff import *
from DQM.RPCMonitorClient.RPCTier0Source_cff import *
from DQM.CSCMonitorModule.csc_dqm_sourceclient_offline_cff import *
from DQM.EcalPreshowerMonitorModule.es_dqm_source_offline_cff import *
from DQM.BeamMonitor.AlcaBeamMonitor_cff import *
from DQM.CastorMonitor.castor_dqm_sourceclient_offline_cff import *
from Validation.RecoTau.DQMSequences_cfi import *
from DQMOffline.Hcal.HcalDQMOfflineSequence_cff import *

DQMOfflinePreDPG = cms.Sequence( dqmEnvCommon *
                                 dqmDcsInfo *
                                 ecal_dqm_source_offline *
                                 hcalOfflineDQMSource *
                                 SiStripDQMTier0 *
                                 siPixelOfflineDQM_source *
                                 dtSources *
                                 rpcTier0Source *
                                 cscSources *
                                 es_dqm_source_offline *
                                 castorSources *
                                 HcalDQMOfflineSequence)

DQMOfflineDPG = cms.Sequence( DQMOfflinePreDPG *
                              DQMMessageLogger )

from DQMOffline.Muon.muonMonitors_cff import *
from DQMOffline.JetMET.jetMETDQMOfflineSource_cff import *
from DQMOffline.EGamma.egammaDQMOffline_cff import *
from DQMOffline.L1Trigger.L1TriggerDqmOffline_cff import *
from DQMOffline.Trigger.DQMOffline_Trigger_cff import *
from DQMOffline.RecoB.PrimaryVertexMonitor_cff import *
from DQMOffline.RecoB.dqmAnalyzer_cff import *
from DQM.Physics.DQMPhysics_cff import *
from Validation.RecoTau.DQMSequences_cfi import *


DQMOfflinePrePOG = cms.Sequence( muonMonitors *
                                 jetMETDQMOfflineSource *
                                 egammaDQMOffline *
                                 l1TriggerDqmOffline *
                                 triggerOfflineDQMSource *
                                 pvMonitor *
                                 prebTagSequence *
                                 bTagPlotsDATA *
                                 alcaBeamMonitor *
                                 dqmPhysics *
                                 produceDenoms *
                                 pfTauRunDQMValidation)

DQMOfflinePOG = cms.Sequence( DQMOfflinePrePOG *
                              DQMMessageLogger )

DQMOffline = cms.Sequence( DQMOfflinePreDPG *
                           DQMOfflinePrePOG *
                           DQMMessageLogger )

DQMOfflinePrePOGMC = cms.Sequence( pvMonitor *
                                   prebTagSequence *
                                   bTagPlotsDATA *
                                   dqmPhysics )

DQMOfflinePOGMC = cms.Sequence( DQMOfflinePrePOGMC *
                                DQMMessageLogger )
    
DQMOfflinePhysics = cms.Sequence( dqmPhysics )


DQMOfflineCommon = cms.Sequence( dqmEnvCommon *
                                 dqmDcsInfo *
                                 DQMMessageLogger *
                                 SiStripDQMTier0Common *
                                 siPixelOfflineDQM_source *
                                 l1TriggerDqmOffline *
                                 triggerOfflineDQMSource *
                                 alcaBeamMonitor *
                                 castorSources *
                                 dqmPhysics *
                                 pvMonitor *
                                 produceDenoms *
                                 pfTauRunDQMValidation 
                                )
DQMOfflineCommonSiStripZeroBias = cms.Sequence( dqmEnvCommon *
                                 dqmDcsInfo *
                                 DQMMessageLogger *
                                 SiStripDQMTier0MinBias *
                                 siPixelOfflineDQM_source *
                                 l1TriggerDqmOffline *
                                 triggerOfflineDQMSource *
                                 alcaBeamMonitor *
                                 castorSources *
                                 dqmPhysics *
                                 pvMonitor *
                                 produceDenoms *
                                 pfTauRunDQMValidation 
                                 )
DQMOfflineMuon = cms.Sequence( dtSources *
                               rpcTier0Source *
                               cscSources *
                               muonMonitors
                              )
DQMOfflineHcal = cms.Sequence( hcalOfflineDQMSource )

DQMOfflineEcal = cms.Sequence( ecal_dqm_source_offline *
                               es_dqm_source_offline
                             )
DQMOfflineJetMET = cms.Sequence( jetMETDQMOfflineSource )

DQMOfflineEGamma = cms.Sequence( egammaDQMOffline )

DQMOfflineBTag = cms.Sequence( prebTagSequence *
                               bTagPlotsDATA )
                                                                 

