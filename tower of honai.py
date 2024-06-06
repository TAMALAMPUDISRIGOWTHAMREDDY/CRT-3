def disc(n,source,extra,destination):
    if n==1:
        print("move first disc from ",source,"to ",destination)
        return
    disc(n-1,source,destination,extra)
    print("Move", n, "th disc from", source, "to", destination)
    disc(n-1,extra,source,destination)
disc(4,"source","extraspace","destination")
    
