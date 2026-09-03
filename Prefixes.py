class Prefix:
    def definition(Term):
        Term = Term.lower()
        WordA = {("no", "not", "without", "away from", "negative"): "a-",
                 ("away from", "negative", "absent"): "ab-",
                 ("in front of", "before"): "ante-",
                 ("counteracting", "effective against", "opposing", "opposite"): "anti-",
                 ("no", "not", "without"): "an-",
                 ("separate", "derivation from"): "ap-"}
        
        WordB = {("two", "twice", "double"): "bi-",
                  "short":"brachy-",
                  "slow": "brady-"}
        
        WordC = {("together", "with"): ["co-", "com-", "con-"],
                 ("against", "counter", "opposite"): "contra-"}
        
        WordD = {("lack of", "from", "not", "removal"): "de-",
                  "half": "demi-",
                 ("two", "twice", "double"): "di-",
                 ("bad", "disordered", "painful"): "dys-"}
        
        WordE = { "outside": ["ecto-", "exo-"],
                  "inside": "endo-",
                 ("inside", "within"): "intra-",
                 ("upon", "above", "beside"): "epi-",
                 ("good", "normal", "well", "easy"):"eu-",
                 ("outside of", "beyond", "in addition to"): "extra-"}
        
        WordF = {}

        WordG = {}

        WordH = { "other, different": ["hetero-"],
                  "same": "homo-",
                  "half": "hemi-",
                 ("above", "excessive"): "hyper-",
                 ("below", "deficient"): "hypo-"}

        WordI = {("below", "beneath"): "infra-",
                  "between": "inter-",
                 ("inside", "within"): "intra-",
                 ("equal", "same"): "iso-"}
        
        WordJ = {}

        WordK = {}

        WordL = {}

        WordM = {("large", "long"): "macro-",
                 ("bad", "poor"): "mal-",
                 ("large", "great"): ["mega-", "megalo-"],
                  "small": "micro-",
                 ("many", "much"): "multi-"}

        WordN = {"new": "neo-",
                 "not": "non-"}
        
        WordO = {("straight", "correct", "normal"): "ortho-"}

        WordP = { "all, entire": ["pan-"],
                 ("beside", "near", "abnormal", "involving"): "para-",
                 ("around", "surrounding"): "peri-",
                 ("many", "much"): "poly-",
                 ("after", "behind"): "post-",
                 ("before", "in front of"): "pre-",
                 ("before", "in front of", "promoting"): "pro-",
                  "false": "pseudo-"}
        
        WordQ = {}

        WordR = {("again", "back"): "re-",
                 ("behind", "backward"): "retro-"}

        WordS = {("under", "below"): "sub-",
                 ("above", "excessive"): "super-",
                 ("above", "over"): "supra-",
                 ("together", "with"): ["syn-", "sym-"]}

        WordT = {("fast", "rapid"): "tachy-",
                 ("across", "through"): "trans-",
                 ("three"): "tri-"}

        WordU = {("beyond", "excessive"): "ultra-",
                "one": "uni-"}
        
        WordV = {}

        WordW = {}

        WordX = {("foreign", "strange"): "xeno-"}

        WordY = {}

        WordZ = {}
        

        # Merge all letter dicts into one mapping
        merged = {}
        for d in (WordA, WordB, WordC, WordD, WordE, WordF, WordG, WordH,
                  WordI, WordJ, WordK, WordL, WordM, WordN, WordO, WordP,
                  WordQ, WordR, WordS, WordT, WordU, WordV, WordW, WordX,
                  WordY, WordZ):
            merged.update(d)

        # Build normalized lookup indexes (meaning -> prefixes, prefix -> meanings)
        meaning_to_prefix = {}
        prefix_to_meaning = {}

        def normalize_meanings(key):
            if isinstance(key, tuple):
                return [k.strip().lower() for k in key]
            if isinstance(key, str) and ',' in key:
                return [k.strip().lower() for k in key.split(',')]
            return [str(key).strip().lower()]

        def normalize_prefixes(val):
            if isinstance(val, list):
                return [str(v).strip().lower() for v in val]
            return [str(val).strip().lower()]

        for key, val in merged.items():
            meanings = normalize_meanings(key)
            prefixes = normalize_prefixes(val)
            for m in meanings:
                meaning_to_prefix.setdefault(m, []).extend(prefixes)
            for p in prefixes:
                prefix_to_meaning.setdefault(p, []).extend(meanings)

        # Lookup (fast, single pass)
        if Term in meaning_to_prefix:
            res = meaning_to_prefix[Term]
            print(f"{Term} Prefix is {res}")
            return res[0] if len(res) == 1 else res
        if Term in prefix_to_meaning:
            res = prefix_to_meaning[Term]
            print(f"{Term} is the Prefix of {res}")
            return res[0] if len(res) == 1 else res

        raise KeyError(f"'{Term}' is not considered a Prefix")
    