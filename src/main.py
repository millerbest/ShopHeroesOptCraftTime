import sys
import os
import wx
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from shop_heroes_module.shop_heroes_GUI import Opt_Craft_App

if __name__ == "__main__":
    app = wx.App(False)
    frame = Opt_Craft_App(None, "Craft time opt", "v0.1")
    app.MainLoop()   
    