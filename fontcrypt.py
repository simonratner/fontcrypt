from fontTools.ttLib import TTFont
import random

def gen_key(chars):
  permutation = list(chars)
  random.shuffle(permutation)
  return dict(zip(permutation, chars)), dict(zip(chars, permutation))

def gen_codebook(tt, decoder):
  # permute the font cmap tables
  subset = [dict((c, t.cmap[c]) for c in decoder.keys()) for t in tt['cmap'].tables]
  for i, t in enumerate(tt['cmap'].tables):
    for c in decoder.keys():
      t.cmap[c] = subset[i][decoder[c]]
  return tt

def tr(s, mapping):
  return "".join(map(chr, ((mapping[i] if i in mapping else i) for i in map(ord, s))))

if __name__ == "__main__":
  encoder, decoder = gen_key(set(range(33, 127)) - set([38, 60, 62]))

  import sys
  tt = TTFont(sys.argv[1])
  gen_codebook(tt, decoder).save(sys.argv[2])

  print "\n-- ENCODING KEY --\n" + "-".join("%02x%02x" % c for c in encoder.items())
  print "\n-- DECODING KEY --\n" + "-".join("%02x%02x" % c for c in decoder.items())

  print "\n" + tr("user@example.com", encoder)
