def solution(n, lost, reserve):
    for l in sorted(lost):
        try:
            reserve.remove(l)
            lost.remove(l)
        except:
            pass

    copy_lost = lost.copy()
    for l in sorted(lost):
        if l - 1 in reserve or l + 1 in reserve:
            copy_lost.remove(l)
            try:
                reserve.remove(l - 1)
            except:
                reserve.remove(l + 1)
        else:
            pass

    return n - len(copy_lost)
