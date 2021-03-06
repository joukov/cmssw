import FWCore.ParameterSet.Config as cms

process = cms.Process("TEST")
process.load("CondCore.DBCommon.CondDBCommon_cfi")
process.CondDBCommon.connect = 'sqlite_file:keys.db'
# process.CondDBCommon.DBParameters.messageLevel = cms.untracked.int32(3)

process.source = cms.Source("EmptyIOVSource",
                            lastValue = cms.uint64(1),
                            timetype = cms.string('runnumber'),
                            firstValue = cms.uint64(1),
                            interval = cms.uint64(1)
                            )

process.PoolDBOutputService = cms.Service("PoolDBOutputService",
                                          process.CondDBCommon,
                                          timetype = cms.untracked.string('runnumber'),
                                          outOfOrder = cms.untracked.bool(True),
                                          toPut = cms.VPSet( cms.PSet( record = cms.string('confcont'),
                                                                       tag = cms.string('KeyTest'),
                                                                       timetype = cms.untracked.string('hash'),
                                                                       outOfOrder = cms.untracked.bool(True)
                                                                       ),
                                                             cms.PSet( record = cms.string('confiov'),
                                                                       tag = cms.string('ConfTest'),
                                                                       timetype = cms.untracked.string('runnumber'),
                                                                       outOfOrder = cms.untracked.bool(False)
                                                                       )
                                                             )
                                          )

process.mytest = cms.EDAnalyzer("writeKeyed")

process.p = cms.Path(process.mytest)

