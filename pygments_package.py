from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import HtmlFormatter

code = "print('Hello, World!')"

# Highlight code
highlighted = highlight(code, PythonLexer(), HtmlFormatter(full=True))
with open("highlighted_code.html", "w") as f:
    f.write(highlighted)
print(highlighted)  # This will be HTML with color styling

