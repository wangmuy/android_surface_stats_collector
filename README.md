adapt from aosp external/chromium_org/build/android/pylib/perf/surface_stats_collector.py

Usage:

```
python framerate_runner.py <LayerName> <phoneSerialId>
```

```<LayerName>``` is the name of the layer from the output of 'adb shell dumpsys SurfaceFlinger'

e.g: SurfaceView in '+ Layer 0xb794fd68 (SurfaceView)'

```<phoneSerialId>``` is the serial id of the connected device