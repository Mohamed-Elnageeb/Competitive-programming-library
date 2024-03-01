def dvis(g,v) : 
    global step , finish 
    # total = 0  
    q = [v] 
    while q : 
        step += 1 
        v = q[-1] 
        if color[v] : 
            v = q.pop()
            if color[v] == 1 :   
                color[v] = 2 
                finish[v] = step 
        else:
            color[v] = 1 
            # total += 1 
            # time_discovered[v] = step 
            if v in g :
                for ch in g[v] : 
                    if not color[ch] : 
                        q.append(ch)

def dfs1(g) : 
    global step ,color ,finish 
    step = 0 
    color = {}
    for n,ch in g.items() : 
        color[n] = 0 
        for k in ch : 
            color[k] = 0 
    finish = {}
    for i in g : 
        if not color[i] : 
            dvis(g,i) 
    order = sorted( finish.keys() , key =lambda x : finish[x] )
    return order  

def dfs2(rev_g,v,vis) : 
    vis.add(v) 
    q = [v]
    s = [v]  
    while q : 
        n = q.pop() 
        if n in rev_g : 
            for ch in rev_g[n] : 
                if ch not in vis : 
                    vis.add(ch) 
                    q.append(ch) 
                    s.append(ch) 
    return s
    

def kosaraju(g) : 
    global vis 
    order = (dfs1(g))[::-1]
    rev_g = {} 
    for node,ch in g.items() : 
        for i in ch : 
            try: 
                rev_g[i].append(node) 
            except : 
                rev_g[i] = [node] 
    vis = set() 
    scc = [] 
    for v in order : 
        if v not in vis : 
            scc.append(dfs2(rev_g,v,vis) )
    return scc

# n,m = list(map(int,input().split())) 
# g = {} 
# for i in range(m) :
#     u,v = list(map(int,input().split())) 
#     try : 
#         g[u].append(v) 
#     except:
#         g[u] = [v] 
# print(kosaeaju(g))


