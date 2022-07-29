"""
This module is just for language completion.
The actual module gets created at runtime by golly.
"""
from typing import List, Tuple

Rect = List[int]
CellList = List[int]
# FILING COMMANDS


def open(filename: str, remember: bool = False) -> None:
    """
    Open the given file and process it according to its type:

    A HTML file (.htm or .html extension) is displayed in the help window.

    A text file (.txt or .doc extension, or a name containing "readme") is opened in your text editor.

    A script file (.lua or .py extension) is executed.

    A zip file (.zip extension) is processed as described here.

    Any other type of file is assumed to be a pattern file and is loaded into the current layer.
    A non-absolute path is relative to the location of the script.
    The 2nd parameter is optional (default = False) and specifies if the given pattern or zip file
    should be remembered in the Open Recent submenu, or in the Run Recent submenu if the file is a script.
    Example: g.open("my-patterns/foo.rle")
    """
    pass


def save(filename: str, format: str, remember: bool = False) -> None:
    """
    Save the current pattern in a given file using the specified format:
    "rle"
    run length encoded (RLE)
    "rle.gz"
    compressed RLE
    "mc"
    macrocell
    "mc.gz"
    compressed macrocell
    A non-absolute path is relative to the location of the script.
    The 3rd parameter is optional (default = False) and specifies if the file
    should be remembered in the Open Recent submenu.
    If the savexrle option is True then extended RLE format is used (see the Save Extended RLE item for details).
    Example: g.save("foo.rle", "rle", True)
    """
    pass


def opendialog(title, filetypes, initialdir, initialfname, mustexist=True):
    """
    Present a standard Open dialog to the user and return the chosen path in a string.
    All parameters are optional; the default is an Open dialog showing the current directory,
    with a title of "Choose a file" and a file type of "All files (*)|*".
    If the 5th parameter (default = True) is set to False,
    the user can specify a new filename instead of choosing an existing file.
    If the given file type is "dir" then the dialog lets the user choose a directory rather than a file.
    If the user cancels the dialog, the return value will be an empty string.
    Example: fname = g.opendialog("Open MCell File", "MCell files (*.mcl)|*.mcl", "C:\\Temp", "sample.mcl")
    Example: dirname = g.opendialog("Choose a folder", "dir");
    """
    pass


def savedialog(title: str, filetypes, initialdir, initialfname, suppressprompt=False):
    """
    Present a standard Save dialog to the user and return the chosen path in a string.
    All parameters are optional; the default is a Save dialog showing the current directory,
    with a title of "Choose a save location and filename" and a file type of "All files (*)|*".
    If a file already exists at the chosen location, an Overwrite?
    query will be displayed unless the 5th parameter (default = False) is set to True.
    If the user cancels the dialog, the return value will be an empty string.
    Example: fname = g.savedialog("Save text file", "Text files (*.txt;*.csv)|*.txt;*.csv", "C:\\Temp", "Params.txt", 1)
    """
    pass


def load(filename: str) -> CellList:
    """
    Read the given pattern file and return a cell list.
    Example: blinker = g.load("blinker.rle")
    """
    return []


def store(cell_list: CellList, filename: str):
    """
    Write the given cell list to the specified file in RLE format.
    If the savexrle option is True then extended RLE format is used (see the Save Extended RLE item for details).
    Example: g.store(clist, "foo.rle")
    """
    pass


def getdir(dirname: str) -> str:
    """
    Return the path of the specified directory:
    "app" — the directory containing the Golly application.
    "data" — the user-specific data directory:
    On Linux:
    ~/.golly/
    On Mac:
    ~/Library/Application Support/Golly/
    On Windows 7+:
    "temp" — the directory Golly uses to store various temporary files. All these files are deleted when Golly quits.
    "rules" — the user-specific rules directory set in Preferences > Control.
    "files" — the directory displayed by File > Show Files.
    "download" — the directory Golly uses to store downloaded files.
    In each case a full path is returned, terminated by the appropriate path separator for the current platform.
    Example: g.open(g.getdir("app") + "Patterns/Life/Breeders/breeder.lif")
    """
    return ""


def setdir(dirname: str, dirpath: str) -> None:
    """
    Set the specified directory to the given path (which must be a full path to an existing directory).
    All the directory names listed above are allowed, except for "app", "data" and "temp".
    Example: g.setdir("download", "/path/to/my-downloads/")
    """
    pass


def getinfo() -> str:
    """
    Return the comments from the current pattern.
    Example: comments = g.getinfo()
    """
    return ""


def getpath() -> str:
    """
        Return the pathname of the current open pattern.
    Returns "" if the current pattern is new and has not been saved.
        Example: path = g.getpath()

        EDITING COMMANDS
    """
    return ""


def new(title: str):
    """
    Create a new, empty universe and set the window title.
    If the given title is empty then the current title won't change.
    Example: g.new("test-pattern")
    """
    pass


def cut():
    """
    Cut the current selection to the clipboard.
    """
    pass


def copy():
    """
    Copy the current selection to the clipboard.
    """
    pass


def clear(where: int):
    """
    Clear inside (where = 0) or outside (where = 1) the current selection.
    Example: g.clear(1)
    """
    pass


def paste(x: int, y: int, mode: str):
    """
    Paste the clipboard pattern at x,y using the given mode ("and", "copy", "or", "xor").
    Example: g.paste(0, 0, "or")
    """
    pass


def shrink(remove_if_empty: bool = False):
    """
    Shrink the current selection to the smallest rectangle enclosing all of the selection's live cells.
    If the selection has no live cells then the optional parameter specifies whether the selection remains unchanged or is removed.
    Example: if len(g.getselrect()) > 0: g.shrink(True)
    """
    pass


def randfill(percentage: int):
    """
    Randomly fill the current selection to a density specified by the given percentage (1 to 100).
    Example: g.randfill(50)
    """
    pass


def flip(direction: int):
    """
    Flip the current selection left-right (direction = 0) or top-bottom (direction = 1).
    """
    pass


def rotate(direction: int):
    """
    Rotate the current selection 90 degrees clockwise (direction = 0) or anticlockwise (direction = 1).
    """
    pass


def evolve(cell_list: CellList, numgens: int):
    """
    Advance the pattern in the given cell list by the specified number of generations and return the resulting cell list.
    Example: newpatt = g.evolve(currpatt, 100)
    """
    pass


def join(cell_list1: CellList, cell_list2: CellList):
    """
    Join the given cell lists and return the resulting cell list.
    If the given lists are both one-state then the result is one-state.
    If at least one of the given lists is multi-state then the result is multi-state,
    but with one exception: if both lists have no cells then the result is [] (an empty one-state list) rather than [0].
    See below for a description of one-state and multi-state cell lists.
    Example: result = g.join(part1, part2)
    """
    pass


def transform(
    cell_list: CellList,
    x0: int,
    y0: int,
    axx: int = 1,
    axy: int = 0,
    ayx: int = 0,
    ayy: int = 1,
):
    """
    Apply an affine transformation to the given cell list and return the resulting cell list.
    For each x,y cell in the input list the corresponding xn,yn cell in the output list
    is calculated as xn = x0 + x*axx + y*axy, yn = y0 + x*ayx + y*ayy.
    Example: rot_blinker = g.transform(blinker, 0, 0, 0, -1, 1, 0)
    """
    pass


def parse(
    string: str,
    x0: int = 0,
    y0: int = 0,
    axx: int = 1,
    axy: int = 0,
    ayx: int = 0,
    ayy: int = 1,
):
    """
    Parse an RLE or Life 1.05 string and return an optionally transformed cell list.
    Example: blinker = g.parse("3o!")
    """
    pass


def putcells(
    cell_list: CellList,
    x0: int = 0,
    y0: int = 0,
    axx: int = 1,
    axy: int = 0,
    ayx: int = 0,
    ayy: int = 1,
    mode: str = "or",
):
    """
    Paste the given cell list into the current universe using an
    optional affine transformation and optional mode ("and", "copy", "not", "or", "xor").
    Example: g.putcells(currpatt, 6, -40, 1, 0, 0, 1, "xor")
    """
    pass


def getcells(rect_list: Rect) -> CellList:
    """
    Return any live cells in the specified rectangle as a cell list.
    The given list can be empty (in which case the cell list is empty)
    or it must represent a valid rectangle of the form [x,y,width,height].
    Example: clist = g.getcells( g.getrect() )
    """
    return []


def getclip():
    """
    Parse the pattern data in the clipboard and return a cell list,
    but where the first two numbers are the pattern's width and height
    (not necessarily the minimal bounding box because the pattern
    might have empty borders, or it might even be empty).
    If the clipboard data is multi-state but all cell states happen to be zero
    then the returned cell list is [wd,ht] rather than [wd,ht,0].
    Example: clist = g.getclip()
    """
    pass


def hash(rect_list: Rect) -> int:
    """
    Return an integer hash value for the pattern in the given rectangle.
    Two identical patterns will have the same hash value,
    regardless of their location in the universe.
    This command provides a fast way to detect pattern equality,
    but there is a tiny probability that two different patterns will have the same hash value,
    so you might need to use additional (slower) tests to check for true pattern equality.
    Example: h = g.hash( g.getrect() )
    """
    return 0


def select(rect_list: Rect):
    """
    Create a selection if the given list represents a valid rectangle
    of the form [x,y,width,height] or remove the current selection if the given list is [].
    Example: g.select( [-10,-10,20,20] )
    """
    pass


def getrect() -> Rect:
    """
    Return the current pattern's bounding box as a list.
    If there is no pattern then the list is empty ([]),
    otherwise the list is of the form [x,y,width,height].
    Example: if len(g.getrect()) == 0: g.show("No pattern.")
    """
    return []


def getselrect() -> Rect:
    """
    Return the current selection rectangle as a list.
    If there is no selection then the list is empty ([]),
    otherwise the list is of the form [x,y,width,height].
    Example: if len(g.getselrect()) == 0: g.show("No selection.")
    """
    return []


def setcell(x: int, y: int, state: int):
    """
    Set the given cell to the specified state (0 for a dead cell, 1 for a live cell).
    """
    pass


def getcell(x: int, y: int) -> int:
    """
    Return the state of the given cell.
    The following example inverts the state of the cell at 0,0.
    Example: g.setcell(0, 0, 1 - g.getcell(0, 0))
    """
    return 0


def setcursor(string: str) -> str:
    """
    Set the current cursor according to the given string and return the old cursor string.
    The given string must match one of the names in the Cursor Mode menu.
    Example: oldcurs = g.setcursor("Draw")
    """
    return ""


def getcursor() -> str:
    """
    Return the current cursor as a string (ie. the ticked name in the Cursor Mode menu).
    """
    return ""


# CONTROL COMMANDS


def run(numgens: int):
    """
    Run the current pattern for the specified number of generations.
    Intermediate generations are never displayed,
    and the final generation is only displayed if the current autoupdate setting is True.
    Example: g.run(100)
    """
    pass


def step():
    """
    Run the current pattern for the current step.
    Intermediate generations are never displayed,
    and the final generation is only displayed if the current autoupdate setting is True.
    """
    pass


def setstep(exp: int) -> None:
    """
    Temporarily set the current step exponent to the given integer.
    A negative exponent sets the step size to 1 and also sets a delay between each step,
    but that delay is ignored by the run and step commands.
    Golly will reset the step exponent to 0
    upon creating a new pattern, loading a pattern file, or switching to a different algorithm.
    Example: g.setstep(0)
    """
    pass


def getstep() -> int:
    """
    Return the current step exponent.
    Example: g.setstep( g.getstep() + 1 )
    """
    return 0


def setbase(base: int) -> None:
    """
    Temporarily set the current base step to an integer from 2 to 2,000,000,000.
    The current exponent may be reduced if necessary.
    Golly will restore the default base step (set in Preferences > Control)
    upon creating a new pattern, loading a pattern file, or switching to a different algorithm.
    Example: g.setbase(2)
    """
    pass


def getbase() -> int:
    """
    Return the current base step.
    """
    return 0


def advance(where: int, numgens: int):
    """
    Advance inside (where = 0) or outside (where = 1)
    the current selection by the specified number of generations.
    The generation count does not change.
    Example: g.advance(0, 3)
    """
    pass


def reset() -> None:
    """
    Restore the starting pattern and generation count.
    Also reset the algorithm, rule, scale, location and step exponent
    to the values they had at the starting generation.
    The starting generation is usually zero,
    but it can be larger after loading an RLE/macrocell file that stores a non-zero generation count.
    """
    pass


def setgen(gen: str) -> None:
    """
    Set the generation count using the given string.
    Commas and other punctuation marks can be used to make a large number more readable.
    Include a leading +/- sign to specify a number relative to the current generation count.
    Example: g.setgen("-1,000")
    """
    pass


def getgen(sepchar: str = "\0") -> str:
    """
    Return the current generation count as a string.
    The optional parameter (default = '\0') specifies a separator character
    that can be used to make the resulting string more readable.
    For example, g.getgen(',') would return a string like "1,234,567"
    but g.getgen() would return "1234567".
    Use the latter call if you want to do arithmetic on the generation count
    because then it's easy to use int to convert the string to an integer.
    Note that Python supports arbitrarily large integers.
    Example: gen = int( g.getgen() )
    """
    return ""


def getpop(sepchar="\0") -> str:
    """
    Return the current population as a string.
    The optional parameter (default = '\0') specifies a separator character
    that can be used to make the resulting string more readable.
    For example, g.getpop(',') would return a string like "1,234,567"
    but g.getpop() would return "1234567".
    Use the latter call if you want to do arithmetic on the population count.
    The following example converts the population to a floating point number.
    Example: pop = float( g.getpop() )
    """
    return ""


def empty() -> bool:
    """
    Return True if the universe is empty or False if there is at least one live cell.
    This is much more efficient than testing getpop() == "0".
    Example: if g.empty(): g.show("All cells are dead.")
    """
    return True


def numstates() -> int:
    """
    Return the number of cell states in the current universe.
    This will be a number from 2 to 256, depending on the current algorithm and rule.
    Example: maxstate = g.numstates() - 1
    """
    return 0


def numalgos() -> int:
    """
    Return the number of algorithms (ie. the number of items in the Set Algorithm menu).
    Example: maxalgo = g.numalgos() - 1
    """
    return 0


def setalgo(string: str):
    """
    Set the current algorithm according to the given string
    which must match one of the names in the Set Algorithm menu.
    Example: g.setalgo("HashLife")
    """
    pass


def getalgo(index=None) -> str:
    """
    Return the algorithm name at the given index in the Set Algorithm menu,
    or the current algorithm's name if no index is supplied.
    Example: lastalgo = g.getalgo( g.numalgos() - 1 )
    """
    return ""


def setrule(string: str):
    """
    Set the current rule according to the given string.
    If the current algorithm doesn't support the specified rule
    then Golly will automatically switch to the first algorithm that does support the rule.
    If no such algorithm can be found then you'll get an error message and the script will be aborted.
    Example: g.setrule("b3/s23")
    """
    pass


def getrule() -> str:
    """
    Return the current rule as a string in canonical format.
    Example: oldrule = g.getrule()
    """
    return ""


def getwidth() -> int:
    """
    Return the width (in cells) of the current universe (0 if unbounded).
    Example: wd = g.getwidth()
    """
    return 0


def getheight() -> int:
    """
    Return the height (in cells) of the current universe (0 if unbounded).
    Example: ht = g.getheight()

    VIEWING COMMANDS
    """
    return 0


def setpos(x: str, y: str):
    """
    Change the position of the viewport so the given cell is in the middle.
    The x,y coordinates are given as strings so the viewport can be moved to any location in the unbounded universe.
    Commas and other punctuation marks can be used to make large numbers more readable.
    Apart from a leading minus sign, most non-digits are simply ignored;
    only alphabetic characters will cause an error message.
    Note that positive y values increase downwards in Golly's coordinate system.
    Example: g.setpos("1,000,000,000,000", "-123456")
    """
    pass


def getpos(sepchar: str = "\0") -> Tuple[str, str]:
    """
    Return the x,y position of the viewport's middle cell
    in the form of a Python tuple containing two strings.
    The optional parameter (default = '\0') specifies a separator character
    that can be used to make the resulting strings more readable.
    For example, g.getpos(',') might return two strings like "1,234" and "-5,678" but g.getpos()
    would return "1234" and "-5678".
    Use the latter call if you want to do arithmetic on the x,y values,
    or just use the getposint() function defined in the glife package.
    Example: x, y = g.getpos()
    """
    return ("", "")


def setmag(mag: int):
    """
    Set the magnification, where 0 corresponds to the scale 1:1, 1 = 1:2, -1 = 2:1, etc. The maximum allowed magnification is 5 (= 1:32).
    Example: g.setmag(0)
    """
    pass


def getmag() -> int:
    """
    Return the current magnification.
    Example: g.setmag( g.getmag() - 1 )
    """
    return 0


def fit():
    """
    Fit the entire pattern in the viewport.
    """
    pass


def fitsel():
    """
    Fit the current selection in the viewport.
    The script aborts with an error message if there is no selection.
    """
    pass


def visrect(rect_list: Rect) -> bool:
    """
    Return True if the given rectangle is completely visible in the viewport.
    The rectangle must be a list of the form [x,y,width,height].
    Example: if g.visrect( [0,0,44,55] ): . . .
    """
    return False


def setview(wd: int, ht: int):
    """
    Set the pixel width and height of the viewport (the main window will be resized accordingly).
    Example: g.setview(32*32, 32*30)
    """
    pass


def getview(index: int = -1) -> Tuple[int, int]:
    """
    Return the pixel width and height of the viewport if the given index is -1 (the default),
    or the pixel width and height of the specified layer
    if the given index is an integer from 0 to numlayers() - 1.
    Example: wd, ht = g.getview()
    """
    return (0, 0)


def autoupdate(bool: bool):
    """
    When Golly runs a script this setting is initially False.
    If the given parameter is True then Golly will automatically update the viewport
    and the status bar after each command that changes the universe or viewport in some way.
    Useful for debugging Python scripts.
    Example: g.autoupdate(True)
    """
    pass


def update():
    """
    Immediately update the viewport and the status bar,
    regardless of the current autoupdate setting.
    Note that Golly always does an update when a script finishes.
    """
    pass


# LAYER COMMANDS


def addlayer() -> int:
    """
    Add a new, empty layer immediately after the current layer and return the new layer's index,
    an integer from 0 to numlayers() - 1.
    The new layer becomes the current layer and inherits most of the previous layer's settings,
    including its algorithm, rule, scale, location, cursor mode, etc.
    The step exponent is set to 0, there is no selection, no origin offset,
    and the layer's initial name is "untitled".
    Example: newindex = g.addlayer()
    """
    return 0


def clone() -> int:
    """
    Like addlayer (see above) but the new layer shares the same universe as the current layer.
    The current layer's settings are duplicated and most will be kept synchronized
    so that a change to one clone automatically changes all the others.
    Each cloned layer does however have a separate viewport,
    so the same pattern can be viewed at different scales and locations
    (at the same time if layers are tiled).
    Example: cloneindex = g.clone()
    """
    return 0


def duplicate() -> int:
    """
    Like addlayer (see above) but the new layer has a copy of the current layer's pattern.
    Also duplicates all the current settings but,
    unlike a cloned layer, the settings are not kept synchronized.
    Example: dupeindex = g.duplicate()
    """
    return 0


def dellayer():
    """
    Delete the current layer. The current layer changes to the previous layer (unless layer 0 was deleted).
    """
    pass


def movelayer(fromindex: int, toindex: int):
    """
    Move a specified layer to a new position in the layer sequence.
    The chosen layer becomes the current layer.
    Example: g.movelayer(1, 0)
    """
    pass


def setlayer(index: int):
    """
    Set the current layer to the layer with the given index,
    an integer from 0 to numlayers() - 1.
    Example: g.setlayer(0)
    """
    pass


def getlayer() -> int:
    """
    Return the index of the current layer,
    an integer from 0 to numlayers() - 1.
    Example: currindex = g.getlayer()
    """
    return 0


def numlayers() -> int:
    """
    Return the number of existing layers, an integer from 1 to maxlayers().
    Example: if g.numlayers() > 1: g.setoption("tilelayers",1)
    """
    return 0


def maxlayers() -> int:
    """
    Return the maximum number of layers (10 in this implementation).
    """
    return 0


def setname(string: str, index: int = -1):
    """
    Set the name of the given layer, or the current layer's name if no index is supplied.
    Example: g.setname("temporary")
    """
    pass


def getname(index: int = -1) -> str:
    """
    Return the given layer's name, or the current layer's name if no index is supplied.
    Example: if g.getname() == "temporary": g.dellayer()
    """
    return ""


def setcolors(color_list: List[int]):
    """
        Set the color(s) of one or more states in the current layer and its clones (if any).
        If the given list contains a multiple of 4 integers then they are interpreted as state, red, green, blue values.
        A state value of -1 can be used to set all live states to the same color (state 0 is not changed).
        If the given list contains exactly 6 integers then they are interpreted as a color gradient from
        r1, g1, b1 to r2, g2, b2 for all the live states (state 0 is not changed).
        If the given list is empty then all states (including state 0) are reset to their default colors,
        depending on the current algorithm and rule.
        Note that the color changes made by this command are only temporary.
        Golly will restore the default colors if a new pattern is opened or created,
        or if the algorithm or rule changes, or if Preferences > Color is used to change any of the default colors for the current layer's algorithm.
        Example: g.setcolors([1,0,0,0, 2,0,0,0])
    # set states 1 and 2 to black
        Example: g.setcolors([-1,0,255,0])
    # set all live states to green
        Example: g.setcolors([255,0,0, 0,0,255])
    # live states vary from red to blue
        Example: g.setcolors([])
    # restore default colors

    """
    pass


def getcolors(state: int = -1) -> List[int]:
    """
    Return the color of a given state in the current layer as a list of the form
    [ state, red, green, blue ]
    or if the given state is -1 (or not supplied) then return all colors as
    [ 0, r0, g0, b0, . . . N, rN, gN, bN ]
    where N equals numstates() - 1. Note that the list returned by getcolors can be passed into setcolors;
    this makes it easy to save and restore colors.
    Example: allcolors = g.getcolors()
    Example: deadcolor = g.getcolors(0)

    MISCELLANEOUS COMMANDS
    """
    return []


def os() -> str:
    """
    Return the current operating system: "Windows", "Mac" or "Linux".
    Example: if g.os() == "Mac": do_mac_stuff()
    """
    return ""


def sound(command: str, soundfile: str, level):
    """
    Control playback of audio files. If present the soundfile argument must point to a WAV or OGG format file containing the sound to be played. If the volume level is supplied it must be a number from 0.0 (silent) to 1.0 (maximum). Multiple sounds can be played simultaneously.
    If the function is invoked with no arguments then it returns an integer indicating whether sound is available:
    0
    – sound support is not available
    1
    – sound support is available but failed to initialize
    2
    – sound support is available and ready to use
    There are seven sound commands (if sound support is not available or failed to initialize then the commands will silently do nothing):
    play soundfile (level)
    Play the named soundfile at volume level asynchronously and return immediately. The volume is set to maximum level (1.0) if not specified.

    loop soundfile (level)
    Play the named soundfile at volume level asynchronously and loop until the stop command is used.

    stop (soundfile)
    Stop all sound playback or just the specified soundfile. All sounds automatically stop playing when a script finishes.

    pause (soundfile)
    Pause all sound playback or just the specified soundfile.

    resume (soundfile)
    Resume all sound playback or just the specified soundfile.

    volume soundfile level
    Set the named soundfile volume level from 0.0 (silent) to 1.0 (maximum). This is typically used to change the volume of a sound that is already playing.

    state (soundfile)
    Returns "playing" if any sound (or the specified sound) is playing,
    "paused" if the specified sound is paused, "stopped" if the sound is not playing, or "unknown" if soundfile is not found.
    Examples:
    g.sound("play", "beep.wav", 0.5) # play beep.wav at half volume
    g.sound("play", "beep.wav") # play beep.wav at full volume
    g.sound("loop", "background.ogg") # play background.ogg in a loop at full volume
    g.sound("volume", "background.ogg", 0.7) # set background.ogg volume to 0.7
    g.sound("pause", "background.ogg") # pause playback of background.ogg
    g.sound("resume") # resume playback of all paused sounds
    g.sound("stop") # stop all sounds playing
    """
    pass


def setoption(name: str, value):
    """
    Set the given option to the given value.
    The old value is returned to make it easy to restore a setting.
    Here are all the valid option names and their possible values:
    "autofit"
    1 or 0 (True or False)
    "boldspacing"
    2 to 1000 (cells)
    "drawingstate"
    0 to numstates()-1
    "fullscreen"
    1 or 0 (True or False)
    "hyperspeed"
    1 or 0 (True or False)
    "maxdelay"
    0 to 5000 (millisecs)
    "mindelay"
    0 to 5000 (millisecs)
    "opacity"
    1 to 100 (percent)
    "restoreview"
    1 or 0 (True or False)
    "savexrle"
    1 or 0 (True or False)
    "showallstates"
    1 or 0 (True or False)
    "showboldlines"
    1 or 0 (True or False)
    "showbuttons"
    0 to 4
    "showcellborders"
    1 or 0 (True or False)
    "showeditbar"
    1 or 0 (True or False)
    "showexact"
    1 or 0 (True or False)
    "showfiles"
    1 or 0 (True or False)
    "showgrid"
    1 or 0 (True or False)
    "showhashinfo"
    1 or 0 (True or False)
    "showicons"
    1 or 0 (True or False)
    "showlayerbar"
    1 or 0 (True or False)
    "showoverlay"
    1 or 0 (True or False)
    "showpopulation"
    1 or 0 (True or False)
    "showprogress"
    1 or 0 (True or False)
    "showscrollbars"
    1 or 0 (True or False)
    "showstatusbar"
    1 or 0 (True or False)
    "showtimeline"
    1 or 0 (True or False)
    "showtoolbar"
    1 or 0 (True or False)
    "smartscale"
    1 or 0 (True or False)
    "stacklayers"
    1 or 0 (True or False)
    "swapcolors"
    1 or 0 (True or False)
    "switchlayers"
    1 or 0 (True or False)
    "synccursors"
    1 or 0 (True or False)
    "syncviews"
    1 or 0 (True or False)
    "tilelayers"
    1 or 0 (True or False)
    Example: oldgrid = g.setoption("showgrid", True)
    """
    pass


def getoption(name: str):
    """
    Return the current value of the given option.
    See above for a list of all the valid option names.
    Example: if g.getoption("autofit"): g.fit()
    """
    pass


def setcolor(name, r, g, b):
    """
    Set the given color to the given RGB values (integers from 0 to 255).
    The old RGB values are returned as a 3-tuple to make it easy to restore the color.
    Here is a list of all the valid color names and how they are used:
    "border"
    color for border around bounded grid
    "paste"
    color for pasting patterns
    "select"
    color for selections (will be 50% transparent)
    algoname
    status bar background for given algorithm
    Example: oldrgb = g.setcolor("HashLife", 255, 255, 255)
    """
    pass


def getcolor(name):
    """
    Return the current RGB values for the given color as a 3-tuple.
    See above for a list of all the valid color names.
    Example: selr, selg, selb = g.getcolor("select")
    """
    pass


def getclipstr() -> str:
    """
    Return the current contents of the clipboard as an unmodified string.
    Example: illegalRLE = g.getclipstr()
    """
    return ""


def setclipstr(string):
    """
    Copy an arbitrary string (not necessarily a cell pattern) directly to the clipboard.
    Example: g.setclipstr(correctedRLE)
    """
    pass


def getstring(prompt, initial="", title=""):
    """
    Display a dialog box and get a string from the user.
    If the initial string is supplied it will be shown and selected.
    If the title string is supplied it will be used in the dialog's title bar.
    The script will be aborted if the user hits the dialog's Cancel button.
    Example: i = int( g.getstring("Enter a number:", "100") )
    """
    pass


def getevent(get=True):
    """
    When Golly runs a script it initially handles all user events, but if the script calls getevent() then future events are put into a queue for retrieval via later calls. These events are returned in the form of strings (see below for the syntax). If there are no events in the queue then the returned string is empty. Note that the very first getevent() call will always return an empty string, but this isn't likely to be a problem because it normally occurs very soon after the script starts running. A script can call getevent(False) if it wants Golly to resume handling any further events. See flood-fill.py for a good example.
    Key-down events are triggered when a key is pressed or autorepeats. The returned string is of the form "key charname modifiers" where charname can be any displayable ASCII character from '!' to '~' or one of the following names: space, home, end, pageup, pagedown, help, insert, delete, tab, return, left, right, up, down, or f1 to f24. If no modifier key was pressed then modifiers is none, otherwise it is some combination of alt, cmd, ctrl, meta, shift. Note that cmd will only be returned on a Mac and corresponds to the command key. The alt modifier corresponds to the option key on a Mac.
    Key-up events occur when a key is released and are strings of the form "kup charname".
    Mouse-down events in the current layer are strings of the form "click x y button modifiers" where x and y are integers giving the cell position of the click, button is one of left, middle or right, and modifiers is the same as above.
    Mouse-down events in a non-transparent pixel in the overlay are strings of the form "oclick x y button modifiers" where x and y are integers giving the pixel position in the overlay (0,0 is the top left pixel), button is one of left, middle or right, and modifiers is the same as above.
    Mouse-up events are strings of the form "mup button" where button is one of left, middle or right.
    Mouse wheel events in the current layer are strings of the form "zoomin x y" or "zoomout x y" where x and y are the mouse's pixel position in the viewport.
    Mouse wheel events in a non-transparent pixel in the overlay are strings of the form "ozoomin x y" or "ozoomout x y" where x and y are the mouse's pixel position in the overlay.
    File events are strings of the form "file filepath" where filepath is an absolute path. File events can be triggered in a number of ways: by clicking on a file in the left panel, by clicking an "open:" link in the Help window, by double-clicking a Golly-associated file, or by dropping a file onto the Golly window. It is up to the script to decide what to do with the file.
    The following examples show the strings returned after various user events:
    "key m none"
    user pressed M key
    "key space shift"
    user pressed space bar and shift key
    "key , altctrlshift"
    user pressed comma and 3 modifier keys
    "kup left"
    user released the left arrow key
    "click 100 5 left none"
    user clicked cell at 100,5 with left button
    "click -10 9 middle alt"
    user clicked cell with middle button and pressed alt key
    "click 0 1 right altshift"
    user clicked cell with right button and pressed 2 modifiers
    "oclick 10 5 left none"
    user clicked pixel at 10,5 in overlay with left button
    "mup left"
    user released the mouse's left button
    "zoomout 10 20"
    mouse wheel was used to zoom out from pixel in viewport
    "ozoomin 10 20"
    mouse wheel was used to zoom in to pixel in overlay
    "file /path/to/foo.rle"
    user tried to open the given file
    Example: evt = g.getevent()
    """
    pass


def doevent(event):
    """
    Pass the given event to Golly to handle in the usual manner
    (but events that can change the current pattern will be ignored).
    The given event must be a string with the exact same format
    as returned by the getevent command (see above).
    If the string is empty then Golly does nothing.
    Note that the cmd modifier corresponds to the command key on a Mac
    or the control key on Windows/Linux
    (this lets you write portable scripts that work on any platform).
    Example: g.doevent("key q cmd") # quit Golly
    """
    pass


def getxy() -> str:
    """
    Return the mouse's current grid position as a string.
    The string is empty if the mouse is outside the viewport
    or outside a bounded grid or over the translucent buttons,
    otherwise the string contains x and y cell coordinates separated by a space;
    eg. "-999 12345". See draw-lines.py for a good example of how to use this command.
    Example: mousepos = g.getxy()
    """
    return ""


def show(message: str):
    """
    Show the given string in the bottom line of the status bar.
    The status bar is automatically shown if necessary.
    Example: g.show("Hit any key to continue...")
    """
    pass


def error(message: str):
    """
    Beep and show the given string in the bottom line of the status bar.
    The status bar is automatically shown if necessary.
    Example: g.error("The pattern is empty.")
    """
    pass


def warn(message: str, showCancel=True):
    """
    Beep and show the given string in a modal warning dialog.
    Useful for debugging Python scripts or displaying error messages.
    If showCancel is True (the default)
    then the dialog has a Cancel button as well as the usual OK button.
    Clicking OK will close the dialog and continue;
    clicking Cancel will close the dialog and abort the script.
    Example: g.warn("xxx = " + str(xxx))
    """
    pass


def note(message: str, showCancel: bool = True):
    """
    Show the given string in a modal information dialog.
    Useful for displaying multi-line results.
    If showCancel is True (the default) then
    the dialog has a Cancel button as well as the usual OK button.
    Clicking OK will close the dialog and continue;
    clicking Cancel will close the dialog and abort the script.
    Example: g.note("Line 1\nLine 2\nLine 3", False)
    """
    pass


def check(bool: bool):
    """
    When Golly runs a script this setting is initially True,
    which means that event checking is enabled.
    If the given parameter is False then event checking is disabled.
    Typically used to prevent mouse clicks being seen at the wrong time.
    This should only be done for short durations
    because the script cannot be aborted while the setting is False.
    Example: g.check(False)
    """
    pass


def exit(message: str = ""):
    """
    Exit the script with an optional error message.
    If a non-empty string is supplied then it will be displayed
    in the status bar along with a beep, just like the error command.
    If no message is supplied, or if the string is empty,
    then there is no beep and the current status bar message will not be changed.
    Example: if g.empty(): g.exit("There is no pattern.")
    """
