def steadyGene(gene):
    minlens = len(gene)
     
    hcnt = {}
    hcnt['A'] = 0
    hcnt['G'] = 0
    hcnt['C'] = 0
    hcnt['T'] = 0
     
    expected = len(gene) // 4
     
    for g in gene:
        hcnt[g] += 1
     
    for x in hcnt:
        hcnt[x] = max(0, hcnt[x] - expected)
     
    if hcnt['A'] == 0 and hcnt['G'] == 0 and hcnt['C'] == 0 and hcnt['T'] == 0:
        return 0
     
    cnt = dict()
    cnt['A'] = 0
    cnt['G'] = 0
    cnt['C'] = 0
    cnt['T'] = 0
     
    tail = 0
    head = 0
     
    while head != len(gene):
        cnt[gene[head]] += 1
        if cnt['A'] >= hcnt['A'] and cnt['C'] >= hcnt['C'] and cnt['G'] >= hcnt['G'] and cnt['T'] >= hcnt['T']:
            minlens = min(minlens, head-tail+1)
            while cnt[gene[tail]] > hcnt[gene[tail]]:
                cnt[gene[tail]] -= 1
                tail += 1
                minlens = min(minlens, head-tail+1)
             
             
        head += 1
     
    return minlens