geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]
def goose_filter(birds):
    filteredlst = []
    for i in birds:
        if i not in geese:
            filteredlst.append(i)
            
    return filteredlst