# import statements
import eel
from asfr.classes import ASFR

# initializing eel
eel.init("../web")

# creating asfr object
asfr = ASFR()


@eel.expose
def load() -> None:
    """
    Loading images that we are going to encode
    Decorated function (Callable from javascript side)
    :return: None
    """
    # calling image_loader method
    asfr.image_loader()


@eel.expose
def encode() -> None:
    """
    Encoding images
    Decorated function (Callable from javascript side)
    :return: None
    """
    # calling encoder method
    asfr.encoder()


@eel.expose
def save() -> None:
    """
    Saving generated encodes
    Decorated function (Callable from javascript side)
    :return: None
    """
    # calling save method
    asfr.save()


@eel.expose
def start() -> None:
    """
    Starting recognizing process
    Decorated function (Callable from javascript side)
    :return: None
    """
    # calling recognizer method
    asfr.recognizer()


@eel.expose
def stop() -> None:
    """
    Stopping recognizing process
    Decorated function (Callable from javascript side)
    :return: None
    """
    # calling stop method
    asfr.stop()


if __name__ == '__main__':
    eel.start("index.html")
