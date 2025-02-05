from xml.dom.minidom import ProcessingInstruction
from colour_print import

def banner_text(text:str = " ",screen_width:int = 80) -> None:
    """
    Centers and banners text in cutomized width
    :param text: The string to print.
        An asterisk (*) will result in a row of asterisks.
        The default will print a blank line, with a ** border at
        the left and right edges.
    :param screen_width: determines the width of the screen,
    removes lines longer... The overall width to print within
        (including the 4 spaces for the ** either side).
    :raises ValueError: if the supplied string is too long to fit.
    """
    if len(text) > screen_width-4:
       raise ValueError("String {0} is larger then specified width {1}"
                        .format(text, screen_width)) #how to make a a program crash.. different types of errors
    if text =="*":
        print("*" * screen_width)
    else:
        output_string = "**{0}**".format(text.center(screen_width-4))
        print(output_string)

width=70 #forskellige måder at binde en varialbe til se også linje 4
banner_text(BLUE,"*",70)
banner_text("Because I love and I love and I love and I love you only (only)",70)
banner_text("Because I need and I need and I need and I need you more, yeah",70)
banner_text(screen_width=70)
banner_text("You know I run and I run and I run and I run",70)
banner_text("Fly, we can fly in the sky in the night",70)
banner_text("Hold me in your arms, in your love and your light",70)
banner_text("*",70)
#banner_text("I'm on your wave right now (I need you more), wave, I'm on your wave right now (I need you more) yeah, wave",width)