




import gc

print("gc is enabled ? : ",gc.isenabled())
gc.disable()
print("gc is enabled ? : ",gc.isenabled())
gc.enable()
print("gc is enabled ? : ",gc.isenabled())
gc.disable()

gc.collect()

