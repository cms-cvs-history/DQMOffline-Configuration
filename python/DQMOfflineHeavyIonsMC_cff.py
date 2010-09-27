import FWCore.ParameterSet.Config as cms

from DQMOffline.Configuration.DQMOfflineHeavyIons_cff import *

siStripFEDCheck.RawDataTag = 'rawDataCollector'
siStripFEDMonitor.RawDataTag = 'rawDataCollector'
SiPixelHLTSource.RawInput = 'rawDataCollector'
dqmCSCClient.InputObjects = 'rawDataCollector'
ecalBarrelHltTask.FEDRawDataCollection = 'rawDataCollector'
ecalBarrelSelectiveReadoutTask.FEDRawDataCollection = 'rawDataCollector'
ecalBarrelRawDataTask.FEDRawDataCollection = 'rawDataCollector'
ecalEndcapHltTask.FEDRawDataCollection = 'rawDataCollector'
ecalEndcapSelectiveReadoutTask.FEDRawDataCollection = 'rawDataCollector'
ecalEndcapRawDataTask.FEDRawDataCollection = 'rawDataCollector'
dtDataIntegrityUnpacker.inputLabel = 'rawDataCollector'
hcalMonitor.FEDRawDataCollection = 'rawDataCollector'
hcalDetDiagNoiseMonitor.RawDataLabel = 'rawDataCollector'
hcalRawDataMonitor.FEDRawDataCollection = 'rawDataCollector'
#l1tfed.rawTag = 'rawDataCollector'  # not needed until trigger DQM is enabled
ecalPreshowerFEDIntegrityTask.FEDRawDataCollection = 'rawDataCollector'
ecalPreshowerRawDataTask.FEDRawDataCollection = 'rawDataCollector'

