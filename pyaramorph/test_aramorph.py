import pprint

import pyaramorph

if __name__ == '__main__':
    analyzer = pyaramorph.Analyzer()

    pprint.pprint(analyzer.analyze_text("السيطرة"))
