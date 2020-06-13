from django.core.paginator import *


def paginator(request, cont, onePageNum):
    pag = Paginator(cont, onePageNum)
    pages = request.GET.get('page')
    try:
        contexts = pag.page(pages)
    except PageNotAnInteger:
        contexts = pag.page(1)
    except EmptyPage:
        contexts = pag.page(Paginator.num_pages)
    n = contexts.number
    if n < 4:
        leftpage = range(1, n+1)
        rightpage = range(n+1, n+4)
    elif 4 <= n <= (pag.num_pages-3):
        leftpage = range(n-3, n)
        rightpage = range(n, n+4)
    elif n == (pag.num_pages-2):
        leftpage = range(n-3, n)
        rightpage = range(n, n+3)
    elif n == (pag.num_pages-1):
        leftpage = range(n-3, n)
        rightpage = range(n, n+2)
    else:
        leftpage = range(n-3, n)
        rightpage = pag.num_pages
    con = {'context': contexts, 'leftpage': leftpage, 'rightpage': rightpage}
    return con
