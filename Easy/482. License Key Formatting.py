def licenseKeyFormatting(s, k):
    s = s.replace("-", "").upper()[::-1]
    return '-'.join(s[i:i+k] for i in range(0, len(s), k))[::-1]

