import sys
import re

def optimize(s: str) -> str:
  i = s.find("\n-\n")
  ao = re.search("AudioOffset *: *([0-9-]*) *", s[:i])
  tpdf = re.search("TimingPointDensityFactor *: *([0-9.]*) *", s[:i])
  header = ("AudioOffset:{}".format(ao.groups()[0]) + 
            ("\nTimingPointDensityFactor:{}".format(tpdf.groups()[0]) if tpdf else "") + 
            "\n-\n")
  content = re.sub("(?<=[,-])0?([1-9]?[0-9]*\.(0*[1-9]+|[1-9]*))0*", lambda a: a.groups()[0], s[i+3:])
  content = re.sub("arctap\(", "at(", content)
  content = re.sub("\s", "", content)
  return header + content

def main(args):
  if len(args) != 3:
    print("Usage: aff_optimizer.py <input.aff> <output.aff>")
    return 1
  (_, fi, fo) = args
  with open(fi, mode='r') as i:
    aff = i.read()
    with open(fo, mode='w', newline='\n') as o:
      o.write(optimize(aff))
  return 0

if __name__ == "__main__":
  sys.exit(main(sys.argv))