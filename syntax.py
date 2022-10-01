import sys
import re
from PyQt5.QtWidgets import QApplication, QWidget, QPlainTextEdit, QVBoxLayout
import PyQt5.QtGui as QtGui
from PyQt5.QtGui import QFont, QFontDatabase, QColor, QSyntaxHighlighter, QTextCharFormat


class Highlighter(QSyntaxHighlighter):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._mapping = {}

    def add_mapping(self, pattern, pattern_format, boundaries=(0, 0)):
        self._mapping[pattern] = (pattern_format, boundaries)
    
    def highlightBlock(self, text_block):
        for pattern, (fmt, (a, b)) in self._mapping.items():
            for match in re.finditer(pattern, text_block):
                start, end = match.span()
                if a < 0: start = end + a
                else: start += a
                end -= b + start
                self.setFormat(start, end, fmt)


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setMinimumSize(1200, 800)
        self.setStyleSheet("""
        QPlainTextEdit{
            background-color: #202020;
            color: #ffffff;
        }
        """)

        self.layout = QVBoxLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.layout)

        self.highlighter = Highlighter()
        self.setupEditor()

        self.show()
    
    def setupEditor(self):
        self.editor = QPlainTextEdit()
        with open('calculator.py', 'r') as f:
            self.editor.setPlainText(f.read())
        self.highlighter.setDocument(self.editor.document())
        self.layout.addWidget(self.editor)
        self.load_syntax()
        self.editor.setFont(QFont('Consolas', 12))
        self.editor.setTabStopDistance(
            QtGui.QFontMetrics(self.editor.font()).horizontalAdvance(' ') * 4
        )
    
    def load_syntax(self):
        class_format = QTextCharFormat()
        class_format.setForeground(QColor('#00ffff'))
        class_format.setFontItalic(True)
        self.highlighter.add_mapping(r'[\t]*class [a-zA-Z]', class_format, (0, 2))

        lambda_format = QTextCharFormat()
        lambda_format.setForeground(QColor('#00ffff'))
        lambda_format.setFontItalic(True)
        self.highlighter.add_mapping(r'lambda(:| \w)', lambda_format, (0, 1))

        def_format = QTextCharFormat()
        def_format.setForeground(QColor('#00ffff'))
        def_format.setFontItalic(True)
        self.highlighter.add_mapping(r'def ', def_format, (0, 1))

        self_format = QTextCharFormat()
        self_format.setForeground(QColor('#ff8000'))
        self_format.setFontItalic(True)
        self.highlighter.add_mapping(r'self(\.|,|\))', self_format, (0, 1))

        number_format = QTextCharFormat()
        number_format.setForeground(QColor('#8000ff'))
        self.highlighter.add_mapping(r'( |\(|\+|\-|\*|/|=)([0-9]+(\.[0-9]+){0,1}|None|True|False)', number_format)

        bracket_format = QTextCharFormat()
        bracket_format.setForeground(QColor('#ff00ff'))
        self.highlighter.add_mapping(r'\(|\)|\[|\]|\{|\}', bracket_format)

        operators = QTextCharFormat()
        operators.setForeground(QColor('#ff0080'))
        self.highlighter.add_mapping(r'\+|\-|\*|/|=|<|>|\.\.\.', operators)

        string_format = QTextCharFormat()
        string_format.setForeground(QColor('#ffff40'))
        self.highlighter.add_mapping(r'(\'|\")+(.|\n)*(\'|\")+', string_format)

        call_function = QTextCharFormat()
        call_function.setForeground(QColor('#00ffff'))
        self.highlighter.add_mapping(r'\w+\(', call_function, (0, 1))

        definition = QTextCharFormat()
        definition.setForeground(QColor('#00ff00'))
        self.highlighter.add_mapping(r'def [a-zA-Z][a-zA-Z_]+\(', definition, (4, 1))

        class_ = QTextCharFormat()
        class_.setForeground(QColor('#00ff00'))
        self.highlighter.add_mapping(r'class [a-zA-Z]+\(', class_, (6, 1))

        keywords = QTextCharFormat()
        keywords.setForeground(QColor('#ff0080'))
        self.highlighter.add_mapping(r'(from|import|if|else|elif|global|with|match|not|for|while|try|except)( |:)', keywords, (0, 1))

        special_keywords = QTextCharFormat()
        special_keywords.setForeground(QColor('#ff0080'))
        self.highlighter.add_mapping(r' (in|as) ', special_keywords, (1, 1))

        kwargs = QTextCharFormat()
        kwargs.setForeground(QColor('#ff8000'))
        self.highlighter.add_mapping(r', \w+=', kwargs, (2, 1))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())