# -*- coding: utf-8 -*-
"""把决策仪表盘 markdown 报告转成自包含 HTML（内联 CSS），方便手机/浏览器预览。用完即删。"""
import sys, os, datetime
import markdown2

MD_PATH = sys.argv[1] if len(sys.argv) > 1 else '/workspace/reports/report_20260726.md'
HTML_PATH = sys.argv[2] if len(sys.argv) > 2 else '/workspace/reports/report_20260726.html'

with open(MD_PATH, 'r', encoding='utf-8') as f:
    md_text = f.read()

html_body = markdown2.markdown(
    md_text,
    extras=['tables', 'fenced-code-blocks', 'cuddled-lists', 'break-on-newline', 'strike', 'task_list']
)

CSS = """
* { box-sizing: border-box; }
body {
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", "PingFang SC", "Hiragino Sans GB", "Microsoft YaHei", sans-serif;
  max-width: 880px; margin: 0 auto; padding: 20px 16px 60px;
  color: #1f2329; background: #f7f7f9; line-height: 1.7; font-size: 15px;
}
h1 { font-size: 22px; color: #1a1a1a; border-bottom: 2px solid #165dff; padding-bottom: 10px; margin-top: 8px; }
h2 { font-size: 18px; color: #165dff; margin-top: 28px; padding: 6px 0 6px 12px; border-left: 4px solid #165dff; background: #eef3ff; }
h3 { font-size: 16px; color: #1a1a1a; margin-top: 22px; padding-bottom: 4px; border-bottom: 1px dashed #c9cdd4; }
h4 { font-size: 15px; color: #4e5969; margin-top: 16px; }
p { margin: 8px 0; }
blockquote {
  margin: 12px 0; padding: 8px 14px; background: #fff8e6;
  border-left: 4px solid #ffb400; color: #4e2d00; border-radius: 4px;
}
table {
  border-collapse: collapse; width: 100%; margin: 12px 0; font-size: 14px;
  background: #fff; box-shadow: 0 1px 3px rgba(0,0,0,0.04);
}
th, td { border: 1px solid #e5e6eb; padding: 8px 10px; text-align: left; }
th { background: #f2f3f5; color: #1a1a1a; font-weight: 600; }
tr:nth-child(even) td { background: #fafbfc; }
code { background: #f2f3f5; padding: 2px 5px; border-radius: 3px; font-size: 13px; color: #d63384; }
pre { background: #1a1a1a; color: #f0f0f0; padding: 14px; border-radius: 6px; overflow-x: auto; }
pre code { background: transparent; color: inherit; padding: 0; }
ul, ol { padding-left: 22px; }
li { margin: 4px 0; }
hr { border: none; border-top: 1px solid #e5e6eb; margin: 24px 0; }
em { color: #86909c; font-size: 13px; }
strong { color: #1a1a1a; }
/* 信号 emoji 行高亮 */
h2 + p, h2 + blockquote { background: #fff; padding: 10px 14px; border-radius: 6px; box-shadow: 0 1px 3px rgba(0,0,0,0.04); }
/* 表格滚动适配手机 */
@media (max-width: 640px) {
  body { padding: 12px 10px 40px; font-size: 14px; }
  table { font-size: 12px; display: block; overflow-x: auto; white-space: nowrap; }
  th, td { padding: 6px 8px; }
  h1 { font-size: 19px; }
  h2 { font-size: 16px; }
  h3 { font-size: 15px; }
}
"""

html = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>决策仪表盘 - 内蒙一机(600967) - {datetime.date.today()}</title>
<style>{CSS}</style>
</head>
<body>
{html_body}
</body>
</html>
"""

with open(HTML_PATH, 'w', encoding='utf-8') as f:
    f.write(html)

size = os.path.getsize(HTML_PATH)
print(f'HTML saved: {HTML_PATH} ({size} bytes)')
