!pip install weasyprint
!pip install tracery


import tracery
from tracery.modifiers import base_english
import markdown
import random
from weasyprint import HTML, CSS
from weasyprint.fonts import FontConfiguration


rules = {
    "startUpName": ["Jonathan", "Eva", "Tim"],
    "verb": ["run", "walk", "jump", "squat", "swim", "throw", "eat", "puke", "fart", "watch"],
    "adjective": ["beautiful", "handsome", "charminng", "distinguished", "happy", "rocky", "ugly", "horrible",
                  "disgusting", "delicious"],
    "noun": ["cake", "dog", "frog", "water", "cucumber", "umbrella", "toliet", "lamp", "lasagna", "football"],
    "color": ["pink", "teal", "brown", "forest green", "lavender", "gold", "silver", "white", "black", "tan"],
    "plural_noun": ["grasses", "lakes", "fishes", "cows", "shoes", "runners", "farts", "trees", "salamanders",
                    "turtles"],
    "body": ["arm", "knee", "toe", "hip", "nose", "mouth", "forehead", "chin", "neck", "head"],
    "body_plural": ["fingers", "wrists", "ankles", "eyebrows", "eyes", "ears", "toes", "nostrils", "nipples", "arms"],
    "verb_ing": ["eating", "breathing", "sleeping", "showering", "bouncing", "throwing", "jogging", "limping",
                 "sitting", "leaping"],
    "silly_word": ["lollipop", "kayak", "bumfuzzle", "collywobbles", "lollygag", "snickerdoodle", "nitwit", "hooter",
                   "tinkle", "waddle"],
    "place": ["Europe", "New Zealand", "The great wall of China", "Rocky Mountains", "Greenland", "Eifel tower",
              "Maine", "New York", "Mississippi River", "Mexico"],
    "book": [
        "I am truly #adjective# for disrupting yesterday's class on the native customs of the #noun#\n tribes of (the) #place#. It was rude of me to burst out #verb_ing# when you explained that the tribal chief\n wore a/n #color#-feathered headpiece in the shape of a wingned #noun# on his #body#. Any decision to #verb# in a circle with my #body_plural#\n outstretchedwhile chanting #silly_word#! #silly_word#! was very inappropriate-even though I was only trying to mimic the #adjective#\n native dance. I understand there's a time and a place for that kind of #noun# and your class was not it. I know that you #verb# very hard as a teacher\n and deserve respect for teaching me and my fellow #plural_noun# every day. I hope you accept my sincere #noun# and believe I will never excerise such #adjective# judgement again.\n\nSincerely,\n\n#startUpName#\n\n"],
    "origin": """

\# My Tracery Book

#book#


    """
}

grammar = tracery.Grammar(rules)
grammar.add_modifiers(base_english)

novel = grammar.flatten("#origin#")



novel_html = markdown.markdown(novel)
# print(novel_html)
font_config = FontConfiguration()
html = HTML(string=novel_html)
css = CSS(string="""
@import url('https://fonts.googleapis.com/css2?family=Merriweather:wght@300&display=swap');
body {font-family: "Merriweather"}
""", font_config=font_config)
html.write_pdf('/content/novel.pdf',stylesheets=[css],font_config=font_config)