import time,sys

from surface_stats_collector import *
from helper import *

adb = SimpleAdb(sys.argv[2]) if len(sys.argv)>=3 else SimpleAdb()
collector=SurfaceStatsCollector(adb,
    forceLegacyMethod=False,
    layerName=sys.argv[1] if len(sys.argv)>=2 else 'SurfaceView')

collector.Start()

for i in range(1):
    time.sleep(1)
    results = collector.SampleResults()
    if not results:
        pass
    for r in results:
      if(r.name != None and r.name.startswith('frame_lengths')):
        print
        continue
      print r.name+': '+str(r.value)+' '+r.unit

collector.Stop()