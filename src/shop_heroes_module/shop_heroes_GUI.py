import wx
import os
import sys
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "db"))
from worker_db import worker_db
from item_db import item_db
from Worker import WorkerLoader as WorkerLoader

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from shop_heroes_module.Worker_params import Worker_params
from shop_heroes_module.Worker import Worker, WorkerLoader
from shop_heroes_module.Item import Item, ItemLoader
from shop_heroes_module.Math import Optimial_craft_time_calculator
import numpy as np
import matplotlib.pyplot as plt
import json

class Opt_Craft_App(wx.Frame):
    def __init__(self, parent, title, version): 
        wx.Frame.__init__(self, None, -1, title,
                        size=(850,630),
                        style=wx.DEFAULT_FRAME_STYLE&~(wx.MAXIMIZE_BOX))
        self.config_path = os.path.join(os.path.dirname(os.path.dirname\
                           (os.path.realpath(__file__))),"config", "default.json")
        with open(self.config_path, "r") as f:
            self.config = json.load(f)
        
        self.InitUI() 
        self.Centre() 
        self.Show()

    def InitUI(self): 
        self.worker_list = self._get_list_of_workers()

        self.panel = wx.Panel(self, -1)
        main_sizer = wx.GridBagSizer(3, 1)
        self.worker_sizer = wx.FlexGridSizer(cols=15, hgap=4, vgap=4)
        self._create_worker_sizer(self.panel)

        self.item_sizer = wx.FlexGridSizer(cols=9, hgap = 6, vgap = 6)
        self._create_item_sizer(self.panel)
        
        self.result_sizer = wx.FlexGridSizer(cols=3, hgap=8, vgap = 6)
        self._create_result_sizer(self.panel)

        main_sizer.Add(self.worker_sizer, pos=(0, 0), flag=wx.TOP|wx.LEFT|wx.BOTTOM,
                       border=5)
        main_sizer.Add(self.item_sizer, pos=(1, 0), flag=wx.TOP|wx.LEFT|wx.BOTTOM,
                       border=5)
        main_sizer.Add(self.result_sizer, pos=(2, 0), flag=wx.TOP|wx.LEFT|wx.BOTTOM,
                       border=30)
        self.panel.SetSizer(main_sizer)

    def _create_worker_sizer(self, parent):
        self._crate_worker_header(parent, self.worker_sizer)
        for i in range(0, 8):
           self._create_worker_tbox(parent, self.worker_sizer, i)
        self._set_tab_order()
        return

    def _create_item_sizer(self, parent):
        st1 = wx.StaticText(parent, -1, "Item: ", style = wx.ALIGN_CENTRE_HORIZONTAL)
        self.item_name_list = []
        self.item_catagory = list(set([item_db[k]["category"] for k in item_db.keys()]))
        self.item_cb1 = wx.Choice(parent, size = (100, -1), choices = list(self.item_catagory), name = "item_cb_1" )
        self.item_cb1.Bind(wx.EVT_CHOICE, self.OnChoice_item_cb1)
        self.item_cb2 = wx.Choice(parent, size = (200, -1), choices = list(self.item_name_list), name = "item_cb_2" )
        self.button_run = wx.Button(parent, label = "Run", size = (100, -1))
        self.button_run.Bind(wx.EVT_BUTTON, self.OnButtonRun)
        self.item_cb2.Bind(wx.EVT_CHOICE, self.OnChoice_item_cb2)
        st2 = wx.StaticText(parent, -1, "Total skill points: ", style = wx.ALIGN_CENTRE_HORIZONTAL)
        self.tc_total_points = wx.TextCtrl(parent, -1, size = (80, -1))
        self.item_sizer.AddMany([wx.StaticText(parent, -1, "", size=(20,20)),
                                 st1, self.item_cb1, 
                                 self.item_cb2, 
                                 wx.StaticText(parent, -1, "", size=(50,20)),
                                 st2,
                                 self.tc_total_points,
                                 wx.StaticText(parent, -1, "", size=(50,20)),
                                 self.button_run])
        
        return

    def _create_result_sizer(self, parent):
        size_text_box = 250
        font = wx.Font(20, wx.DECORATIVE, wx.ITALIC, wx.FONTWEIGHT_BOLD)

        st1 = wx.StaticText(parent, -1, "Craft Time: ", style = wx.ALIGN_RIGHT, size=(size_text_box, -1))
        st1.SetForegroundColour((0, 0, 0))
        st2 = wx.StaticText(parent, -1, "Good rate: ", style = wx.ALIGN_RIGHT,size=(size_text_box, -1))
        st2.SetForegroundColour((0, 164, 0))
        st3 = wx.StaticText(parent, -1, "Great rate: ", style = wx.ALIGN_RIGHT,size=(size_text_box, -1))
        st3.SetForegroundColour((0, 0, 255))
        st4 = wx.StaticText(parent, -1, "Flawless rate: ", style = wx.ALIGN_RIGHT,size=(size_text_box, -1))
        st4.SetForegroundColour((0, 188, 238))
        st5 = wx.StaticText(parent, -1, "Epic rate: ", style = wx.ALIGN_RIGHT,size=(size_text_box, -1))
        st5.SetForegroundColour((228, 2, 217))
        st6 = wx.StaticText(parent, -1, "Legendary rate: ", style = wx.ALIGN_RIGHT,size=(size_text_box, -1))
        st6.SetForegroundColour((212, 227, 0))

        st7 = wx.StaticText(parent, -1, "", style = wx.ALIGN_LEFT, size=(size_text_box, -1),name = "tc_result_1")
        st7.SetForegroundColour((0, 0, 0))
        st8 = wx.StaticText(parent, -1, "", style = wx.ALIGN_LEFT, size=(size_text_box, -1),name = "tc_result_2")
        st8.SetForegroundColour((0, 164, 0))
        st9 = wx.StaticText(parent, -1, "", style = wx.ALIGN_LEFT, size=(size_text_box, -1),name = "tc_result_3")
        st9.SetForegroundColour((0, 0, 255))
        st10 = wx.StaticText(parent, -1, "", style = wx.ALIGN_LEFT, size=(size_text_box, -1),name = "tc_result_4")
        st10.SetForegroundColour((0, 188, 238))
        st11 = wx.StaticText(parent, -1, "", style = wx.ALIGN_LEFT, size=(size_text_box, -1),name = "tc_result_5")
        st11.SetForegroundColour((228, 2, 217))
        st12 = wx.StaticText(parent, -1, "", style = wx.ALIGN_LEFT, size=(size_text_box, -1),name = "tc_result_6")
        st12.SetForegroundColour((212, 227, 0))

        
        for st in [st1, st2, st3, st4, st5, st6, st7, st8, st9, st10, st11, st12]:
            st.SetFont(font)
        self.result_sizer.AddMany([wx.StaticText(parent, -1, "", size=(20,20)),
                                   st1, st7,
                                   wx.StaticText(parent, -1, "", size=(20,20)),
                                   st2, st8,
                                   wx.StaticText(parent, -1, "", size=(20,20)),
                                   st3, st9,
                                   wx.StaticText(parent, -1, "", size=(20,20)),
                                   st4, st10,
                                   wx.StaticText(parent, -1, "", size=(20,20)),
                                   st5, st11,
                                   wx.StaticText(parent, -1, "", size=(20,20)),
                                   st6, st12])
        return

    def _create_worker_tbox(self, parent, sizer, idx_row):
        width_tc = 50
        align_style = wx.ALIGN_CENTRE_HORIZONTAL
        st = wx.StaticText(parent, -1, str(idx_row+1), size=(20,20), style = align_style)
        cb = wx.Choice(parent, size = (100, -1), choices = list(self.worker_list), name = "cb_%s" % (idx_row))
        
        tc0 = wx.TextCtrl(parent, -1, str(self.config["hero%s" % (idx_row+1)]["level"]), size=(width_tc, -1), name = "tc_%s_0" % (idx_row))
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
        
        cb.Bind(wx.EVT_CHOICE, self.OnChoice)
        cb.SetStringSelection(self.config["hero%s" % (idx_row+1)]["name"]) 
        self._send_event(wx.EVT_CHOICE, cb)
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
    
    def OnChoice(self, event):
        current_choice = event.GetEventObject()
        current_worker_name = current_choice.GetString(current_choice.GetSelection())
       # worker_data = worker_db[current_worker_name]
        wl = WorkerLoader(current_worker_name)
        worker_params = wl.get_worker().get_worker_params()
        choice_id = current_choice.Name
        self._set_worker_values(worker_params, choice_id)
        return 

    def _get_tc_by_name(self, name):
        txtCtrls = [widget for widget in self.panel.GetChildren() if isinstance(widget, wx.TextCtrl)]
        result = False
        for ctrl in txtCtrls:
            if ctrl.GetName() == name:      
                result = ctrl
        return result

    def _get_choice_by_name(self, name):
        choices = [widget for widget in self.panel.GetChildren() if isinstance(widget, wx.Choice)]
        result = False
        for ctrl in choices:
            if ctrl.GetName() == name:      
                result = ctrl
        return result

    def _get_st_by_name(self, name):
        sts = [widget for widget in self.panel.GetChildren() if isinstance(widget, wx.StaticText)]
        result = False
        for ctrl in sts:
            if ctrl.GetName() == name:      
                result = ctrl
        return result

    def _set_worker_values(self, worker_params, choice_id):       
        for idx, param in enumerate([worker_params.textile,
                                    worker_params.armor,
                                    worker_params.metal,
                                    worker_params.weapon,
                                    worker_params.wood,
                                    worker_params.alchemy,
                                    worker_params.magic,
                                    worker_params.tinker,
                                    worker_params.jewel,
                                    worker_params.arts_crafts,
                                    worker_params.rune]):
            ctrl_name = "tc_%s_%s" % (choice_id.split("_")[-1], idx+1)
            control = self._get_tc_by_name(ctrl_name)
            if param != -1:
                control.Enable(True)
                control.SetValue(str(param))
            else:
                control.SetValue("")
                control.Enable(False)

        return 
        
    def OnChoice_item_cb1(self, event):
        current_choice = event.GetEventObject()
        category = current_choice.GetString(current_choice.GetSelection())
        item_list = [(key,item_db[key]["name"]) for key in item_db.keys() if item_db[key]["category"] == category]
        self.item_name_list = [v[1] for v in item_list]
        self.item_internal_name_list = [v[0] for v in item_list]
        self.item_cb2.Clear() # Clear the current user list
        self.item_cb2.AppendItems(self.item_name_list) # Repopulate the list
        self.item_cb2.SetSelection(-1)
        return

    def OnChoice_item_cb2(self, event):
        current_choice = event.GetEventObject()
        self.item_internal_name = self.item_internal_name_list[current_choice.GetSelection()]
        return

    def OnButtonRun(self, event):
        item_name = self.item_internal_name  
        worker_name_level_list = self._get_worker_name_level_list()

        if self.tc_total_points.GetValue().isdigit():
            total_skill_points = int(self.tc_total_points.GetValue())
        else:
            total_skill_points = 3000

        il = ItemLoader(item_name)
        
        item = il.get_item()
        octc = Optimial_craft_time_calculator(item, worker_name_level_list, total_skill_points)

        list_workers, time_craft, points_left, mastery_rate = octc.run()

        worker_params = Worker_params()
        for idx, worker in enumerate(list_workers):
            worker_params += worker.get_worker_params()
            
            self._set_worker_values(worker.get_worker_params(), "cb_%s" % (idx))

        self._update_results(time_craft[-1], mastery_rate[-1])
        self._update_config(worker_name_level_list)
        
        #start plot
        
        fig, ax1 = plt.subplots()
        ax1.plot(time_craft, color = "r")
        ax2 = ax1.twinx()
        ax2.plot(np.array(mastery_rate)[:,0], color = "g", linestyle = "--")
        ax2.plot(np.array(mastery_rate)[:,1], color = "b", linestyle = "--")
        ax2.plot(np.array(mastery_rate)[:,2], color = "c", linestyle = "--")
        ax2.plot(np.array(mastery_rate)[:,3], color = "purple", linestyle = "--")
        ax2.plot(np.array(mastery_rate)[:,4], color = "orange", linestyle = "--")

        ax1.set_xlabel("Points added")
        ax1.set_ylabel("Craft time [min]")
        ax2.set_ylabel("Percentage [%]")
        plt.grid()
        plt.show()
    def _update_results(self, craft_time, mastery_rate):
        st1 = self._get_st_by_name("tc_result_1")
        st2 = self._get_st_by_name("tc_result_2")
        st3 = self._get_st_by_name("tc_result_3")
        st4 = self._get_st_by_name("tc_result_4")
        st5 = self._get_st_by_name("tc_result_5")
        st6 = self._get_st_by_name("tc_result_6")
        st1.SetLabel("%.02f minutes" % (craft_time))
        st2.SetLabel("%.02f%%" % (mastery_rate[0]))
        st3.SetLabel("%.02f%%" % (mastery_rate[1]))
        st4.SetLabel("%.02f%%" % (mastery_rate[2]))
        st5.SetLabel("%.02f%%" % (mastery_rate[3]))
        st6.SetLabel("%.02f%%" % (mastery_rate[4]))
        return 

    def _update_config(self,worker_name_level_list):
        result_dict = {}
        try:
            for i,v in enumerate(worker_name_level_list):
                result_dict["hero%s"%(i+1)] = {"name":v[0],
                                                "level":v[1]}
            with open(self.config_path, "w") as f:
                json.dump(result_dict, f)
            return
        except:
            return


    def _get_worker_name_level_list(self):
        result = []
        for i in range(0, 8):
            cb_worker_name = self._get_choice_by_name("cb_%s" % (i))
            tc_level = self._get_tc_by_name("tc_%s_0" % (i))
            worker_name = cb_worker_name.GetString(cb_worker_name.GetSelection())
            level = tc_level.GetValue()
            if worker_name != "" and level.isdigit():
                result.append((worker_name, int(level)))
        return result

    def _set_tab_order(self):
        for i in range(0, 8):
            if i < 7:
                current_tc = self._get_tc_by_name("tc_%s_0" % (i))
                next_tc = self._get_tc_by_name("tc_7_0")
                current_tc.MoveBeforeInTabOrder(next_tc)
        return
    
    def _send_event (self, event, control):
        cmd = wx.CommandEvent(wx.EVT_CHOICE.evtType[0])
        cmd.SetEventObject(control)
        cmd.SetId(control.GetId())
        control.GetEventHandler().ProcessEvent(cmd)
        return

if __name__ == "__main__":
    app = wx.App(False)
    frame = Opt_Craft_App(None, "Craft time opt", "v0.1")
    app.MainLoop()    