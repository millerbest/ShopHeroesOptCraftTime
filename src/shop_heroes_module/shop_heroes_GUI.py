import wx
import os
import sys
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "db"))
from worker_db import worker_db

class Opt_Craft_App(wx.Frame):
    def __init__(self, parent, title, version): 
        wx.Frame.__init__(self, None, -1, title,
                        size=(850,630),
                        style=wx.DEFAULT_FRAME_STYLE&~(wx.MAXIMIZE_BOX))
        self.InitUI() 
        self.Centre() 
        self.Show()

    def InitUI(self): 
        self.worker_list = self._get_list_of_workers()

        panel = wx.Panel(self, -1)
        main_sizer = wx.GridBagSizer(3, 1)
        self.worker_sizer = wx.FlexGridSizer(cols=15, hgap=4, vgap=4)
        self._create_worker_sizer(panel)

        main_sizer.Add(self.worker_sizer, pos=(0, 0), flag=wx.TOP|wx.LEFT|wx.BOTTOM,
                       border=5)

        panel.SetSizer(main_sizer)

    def _create_worker_sizer(self, parent):
        self._crate_worker_header(parent, self.worker_sizer)
        for i in range(0, 8):
           self._create_worker_tbox(parent, self.worker_sizer, i)

    def _create_worker_tbox(self, parent, sizer, idx_row):
        width_tc = 50
        align_style = wx.ALIGN_CENTRE_HORIZONTAL
        st = wx.StaticText(parent, -1, str(idx_row+1), size=(20,20), style = align_style)
        cb = wx.ComboBox(parent, -1, "", size = (100, -1), choices = list(self.worker_list))
        tc0 = wx.TextCtrl(parent, -1, "", size=(width_tc, -1), name = "tc_%s_0" % (idx_row))
        tc1 = wx.TextCtrl(parent, -1, "", size=(width_tc, -1), name = "tc_%s_1" % (idx_row))
        tc2 = wx.TextCtrl(parent, -1, "", size=(width_tc, -1), name = "tc_%s_2" % (idx_row))
        tc3 = wx.TextCtrl(parent, -1, "", size=(width_tc, -1), name = "tc_%s_3" % (idx_row))
        tc4 = wx.TextCtrl(parent, -1, "", size=(width_tc, -1), name = "tc_%s_4" % (idx_row))
        tc5 = wx.TextCtrl(parent, -1, "", size=(width_tc, -1), name = "tc_%s_5" % (idx_row))
        tc6 = wx.TextCtrl(parent, -1, "", size=(width_tc, -1), name = "tc_%s_6" % (idx_row))
        tc7 = wx.TextCtrl(parent, -1, "", size=(width_tc, -1), name = "tc_%s_7" % (idx_row))
        tc8 = wx.TextCtrl(parent, -1, "", size=(width_tc, -1), name = "tc_%s_8" % (idx_row))
        tc9 = wx.TextCtrl(parent, -1, "", size=(width_tc, -1), name = "tc_%s_9" % (idx_row))
        tc10 = wx.TextCtrl(parent, -1, "", size=(width_tc, -1), name = "tc_%s_10" % (idx_row))
        tc11 = wx.TextCtrl(parent, -1, "", size=(width_tc, -1), name = "tc_%s_11" % (idx_row))
        sizer.AddMany([wx.StaticText(parent, -1, "", size=(20,20)), \
                    st, cb, tc0, tc1, tc2, tc3, tc4, tc5, tc6, tc7, tc8, tc9, tc10, tc11])
        return 

    def _crate_worker_header(self, parent, sizer):
        width_st = 50
        align_style = wx.ALIGN_CENTRE_HORIZONTAL
        st0 = wx.StaticText(parent, -1, "Idx", size=(20,20), style = align_style)
        st1 = wx.StaticText(parent, -1, "Worker", size=(100, 20), style = align_style)
        st2 = wx.StaticText(parent, -1, "Level", size=(width_st, 20), style = align_style)
        st3 = wx.StaticText(parent, -1, "textile", size=(width_st, 20), style = align_style)
        st4 = wx.StaticText(parent, -1, "armor", size=(width_st, 20), style = align_style)
        st5 = wx.StaticText(parent, -1, "metal", size=(width_st, 20), style = align_style)
        st6 = wx.StaticText(parent, -1, "weapon", size=(width_st, 20), style = align_style)
        st7 = wx.StaticText(parent, -1, "wood", size=(width_st, 20), style = align_style)
        st8 = wx.StaticText(parent, -1, "alchemy", size=(width_st, 20), style = align_style)
        st9 = wx.StaticText(parent, -1, "magic", size=(width_st, 20), style = align_style)
        st10 = wx.StaticText(parent, -1, "tinker", size=(width_st, 20), style = align_style)
        st11 = wx.StaticText(parent, -1, "jewel", size=(width_st, 20), style = align_style)
        st12 = wx.StaticText(parent, -1, "arts", size=(width_st, 20), style = align_style)
        st13 = wx.StaticText(parent, -1, "rune", size=(width_st, 20), style = align_style)

        sizer.AddMany([wx.StaticText(parent, -1, "", size=(20,20)), \
                    st0, st1, st2, st3, st4, st5, st6, st7, st8, st9, st10, st11, st12, st13])
        return 

    def _get_list_of_workers(self):
        dict_workers = worker_db
        return dict_workers.keys()

    def _create_item_tbox(self, sizer, idx_row):
        pass

    def _create_buttons(self, parent):
        pass

if __name__ == "__main__":
    app = wx.App(False)
    frame = Opt_Craft_App(None, "Craft time opt", "v0.1")
    app.MainLoop()    