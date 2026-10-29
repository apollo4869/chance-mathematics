"""Keep archival continuation furniture out of the continuous reader, not the source."""
import re

CLASS='source-continuation-header'

def suppress(soup):
    book=soup.select_one('#chapter-1')
    if book is None:return False
    if book.select_one('.'+CLASS):return False
    targets=[n for n in book.find_all(['h1','h2']) if re.fullmatch(
        r'第一章：一场没有结束的赌博（续）|Chapter 1: A Game of Chance Left Unfinished \(Continued\)',
        n.get_text(' ',strip=True))]
    assert len(targets)==1,'Chapter1 continuation furniture changed; inspect before suppressing'
    continued=targets[0];volume=continued.find_previous_sibling();title=volume.find_previous_sibling()
    assert volume.name=='p'and volume.get_text(' ',strip=True)in{'第一卷 · 偶然可以计算吗？','Volume I · Can Chance Be Calculated?'}
    assert title.get_text(' ',strip=True)in{'《偶然的数学》','The Mathematics of Chance'}
    following=continued.find_next(['h1','h2'])
    assert following and following.get_text(' ',strip=True).startswith('1.6 ')
    start=title.find_previous_sibling()
    if not start or start.name!='hr':start=title
    nodes=[];node=start
    while node is not None:
        nodes.append(node)
        if node is continued:break
        node=node.next_sibling
    assert nodes[-1]is continued
    assert all(not getattr(n,'name',None)or n in [start,title,volume,continued]for n in nodes)
    wrapper=soup.new_tag('div',attrs={'class':CLASS,'hidden':'','aria-hidden':'true','style':'display:none!important'})
    start.insert_before(wrapper)
    for node in nodes:wrapper.append(node.extract())
    return True

def restore(soup):
    """Undo only our presentation wrapper for exact independent source checks."""
    for n in list(soup.select('.'+CLASS)):n.unwrap()
    return soup
