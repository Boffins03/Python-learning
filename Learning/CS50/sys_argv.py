import sys
if len(sys.argv)<2:
    sys.exit("Too fev argument")
elif len(sys.argv)>2:    
    sys.exit("Too many argument")

print("Hello ",sys.argv[1])
