import cv2
import numpy as np


def metin_yazalim():
    resim = np.zeros((640, 720, 3),np.uint8)
    resim.fill(255)

    fontsacele = 1.0
    renk = (0, 0, 255)
    fontface = cv2.FONT_HERSHEY_COMPLEX
    cv2.FONT_HERSHEY_COMPLEX(resim, 'Savasan insanız hava araci', (25, 40), fontface, fontsacele, renk)
    fontface = cv2.FONT_HERSHEY_COMPLEX_SMALL
    cv2.FONT_HERSHEY_COMPLEX(resim, "Savasan insanız hava araci", (25, 80), fontface, fontsacele, renk)
    fontface = cv2.FONT_HERSHEY_DUPLEX
    cv2.FONT_HERSHEY_COMPLEX(resim, "Savasan insanız hava araci", (25, 120), fontface, fontsacele, renk)
    fontface = cv2.FONT_HERSHEY_PLAIN
    cv2.FONT_HERSHEY_COMPLEX(resim, "Savasan insanız hava araci", (25, 160), fontface, fontsacele, renk)
    fontface = cv2.FONT_HERSHEY_SCRIPT_COMPLEX
    cv2.FONT_HERSHEY_COMPLEX(resim, "Savasan insanız hava araci", (25, 200), fontface, fontsacele, renk)
    fontface = cv2.FONT_HERSHEY_SCRIPT_SIMPLEX
    cv2.FONT_HERSHEY_COMPLEX(resim, "Savasan insanız hava araci", (25, 240), fontface, fontsacele, renk)
    fontface = cv2.FONT_HERSHEY_SIMPLEX
    cv2.FONT_HERSHEY_COMPLEX(resim, "Savasan insanız hava araci", (25, 280), fontface, fontsacele, renk)
    fontface = cv2.FONT_HERSHEY_TRIPLEX
    cv2.FONT_HERSHEY_COMPLEX(resim, "Savasan insanız hava araci", (25, 320), fontface, fontsacele, renk)
    fontface = cv2.FONT_ITALIC
    cv2.FONT_HERSHEY_COMPLEX(resim, "Savasan insanız hava araci", (25, 340), fontface, fontsacele, renk)
    cv2.namedWindow("ornek")
    cv2.imshow('yazi örnekleri', resim)

    cv2.imwrite('ornek.jpg', resim)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def main():
    metin_yazalim()

if __name__=="__main__":

    main()
