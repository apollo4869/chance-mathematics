"""Presentation-only chapter provenance: quiet draft label, end-of-chapter notes."""
import re

def draft_label(en=False):
    return '<span class="chapter-draft-label">'+('Working draft' if en else '工作稿')+'</span>'

def chapter_notes(origin, metadata, links, en=False):
    return ('<section class="chapter-publication" data-chapter-publication="footer" aria-label="'
            +('Chapter information' if en else '章节资料')+'"><nav class="chapter-reference-links" aria-label="'
            +('Chapter versions and citation' if en else '章节版本与引用')+'">'+links+'</nav>'
            '<details class="chapter-edition"><summary>'+('Version & verification information' if en else '版本与校验信息')
            +'</summary><p class="chapter-origin">'+origin+'</p>'+metadata+'</details></section>')

def relocate_existing(page, en=False):
    """Upgrade an existing reading page without reparsing its mathematical DOM.

    Return the exact added fragments so callers can verify that removing them
    recovers every other byte of the original page, with only the old bar moved.
    """
    if 'data-chapter-publication="footer"' in page:
        return page, None
    pattern=r'<details\b[^>]*class="chapter-edition"[^>]*>[\s\S]*?</details>'
    matches=list(re.finditer(pattern,page));assert len(matches)==1, len(matches)
    match=matches[0];old=match[0]
    summary=re.search(r'<summary\b[^>]*>([\s\S]*?)</summary>',old);assert summary
    body=old[summary.end():-len('</details>')]
    anchors=re.findall(r'<a\b[^>]*>[\s\S]*?</a>',body);assert len(anchors)==2
    metadata=body
    for anchor in anchors: metadata=metadata.replace(anchor,'',1)
    metadata=metadata.rstrip(' \t\r\n·')
    notes=chapter_notes(summary[1],metadata,' '.join(anchors),en)
    without=page[:match.start()]+page[match.end():]
    footer=re.search(r'<footer\b[^>]*class="publication-footer"',without);assert footer
    result=without[:footer.start()]+notes+without[footer.start():]
    controls=re.search(r'<div\b[^>]*class="reader-mode-buttons"[^>]*>',result);assert controls
    badge=draft_label(en)
    result=result[:controls.end()]+badge+result[controls.end():]
    assert result.replace(notes,'',1).replace(badge,'',1)==without
    return result,dict(old_bar=old,notes=notes,badge=badge,without_old_bar=without)
