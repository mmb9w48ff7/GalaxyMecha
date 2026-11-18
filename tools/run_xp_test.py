import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); import luart
os.chdir(os.path.dirname(HERE)); st = luart.new()
code = '''package.path="scripts/?.lua;scripts/?/init.lua;"..package.path
local f,err=loadfile("tools/mock_xp_test.lua"); if not f then print("LOADERR",err) return end
local ok,e=xpcall(f, debug.traceback); if not ok then print("RUNTIME ERROR:\\n"..tostring(e)) end'''
print(luart.dostring(st, code))
