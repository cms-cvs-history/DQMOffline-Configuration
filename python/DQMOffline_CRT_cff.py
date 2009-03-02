import FWCore.ParameterSet.Config as cms

siStripCertificationInfo = cms.EDFilter("SiStripCertificationInfo")
siPixelCertification = cms.EDFilter("SiPixelCertification")
from DQM.EcalEndcapMonitorTasks.EEDataCertificationTask_cfi import *
from DQM.EcalBarrelMonitorTasks.EBDataCertificationTask_cfi import *
from DQM.HcalMonitorClient.HcalDataCertification_cfi import *
from DQM.DTMonitorClient.dtDQMOfflineCertification_cff import *

crt_dqmoffline = cms.Sequence(siStripCertificationInfo*siPixelCertification*ecalEndcapDataCertificationTask*ecalBarrelDataCertificationTask*hcalDataCertification*dtCertificationSummary)

