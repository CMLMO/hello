import wx
import wx.xrc
import wx.grid
status_vout_code = 0x00
status_iout_code = 0x00
status_input_code = 0x00
status_temp_code = 0x00
status_cml_code = 0x00
status_fan1_code = 0x00
status_fan2_code = 0x00



###########################################################################
## Class MyFrame1
###########################################################################

class status(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString, pos=wx.DefaultPosition,
                          size=wx.Size(610, 563), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)
        self.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_MENU))
        bSizer1 = wx.BoxSizer(wx.HORIZONTAL)

        bSizer2 = wx.BoxSizer(wx.VERTICAL)
        text = u"Status Vout 7A : "+'{:02X}'.format(status_vout_code) + ""

        sbSizer1 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, text),
                                     wx.VERTICAL)


        self.dgv_Status_vout = wx.grid.Grid(sbSizer1.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)
        status_vout = ["Vout OV Fault","Vout OV Warning","Vout UV Warning","Vout UV Fault","Vout MAX Warning",
                       "TON MAX Fault","TOFF MAX Warning","Vout_Tracking_Error"]


        # Grid
        self.dgv_Status_vout.CreateGrid(8, 1)
        self.dgv_Status_vout.EnableEditing(False)
        self.dgv_Status_vout.EnableGridLines(True)
        self.dgv_Status_vout.EnableDragGridSize(False)
        self.dgv_Status_vout.SetMargins(0, 0)

        # Columns
        self.dgv_Status_vout.SetColSize(0, 150)
        self.dgv_Status_vout.EnableDragColMove(False)
        self.dgv_Status_vout.EnableDragColSize(True)
        self.dgv_Status_vout.SetColLabelSize(0)
        self.dgv_Status_vout.SetColLabelAlignment(wx.ALIGN_CENTER, wx.ALIGN_CENTER)

        row1 = self.dgv_Status_vout.GetNumberRows()
        column1 = self.dgv_Status_vout.GetNumberCols()

        # Rows
        for row in range(row1):
            self.dgv_Status_vout.SetRowSize(row, 16)
            self.dgv_Status_vout.SetCellValue(row, 0, status_vout[row])
        self.dgv_Status_vout.EnableDragRowSize(True)
        self.dgv_Status_vout.SetRowLabelSize(25)
        self.dgv_Status_vout.SetRowLabelValue(0, u"7")
        self.dgv_Status_vout.SetRowLabelValue(1, u"6")
        self.dgv_Status_vout.SetRowLabelValue(2, u"5")
        self.dgv_Status_vout.SetRowLabelValue(3, u"4")
        self.dgv_Status_vout.SetRowLabelValue(4, u"3")
        self.dgv_Status_vout.SetRowLabelValue(5, u"2")
        self.dgv_Status_vout.SetRowLabelValue(6, u"1")
        self.dgv_Status_vout.SetRowLabelValue(7, u"0")
        self.dgv_Status_vout.SetRowLabelAlignment(wx.ALIGN_CENTER, wx.ALIGN_CENTER)

        # Label Appearance

        # Cell Defaults
        self.dgv_Status_vout.SetDefaultCellBackgroundColour(wx.Colour(143, 188, 143))
        self.dgv_Status_vout.SetDefaultCellFont(
            wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "宋体"))
        self.dgv_Status_vout.SetDefaultCellAlignment(wx.ALIGN_LEFT, wx.ALIGN_CENTER)
        #self.dgv_Status_vout.SelectionMode()
        sbSizer1.Add(self.dgv_Status_vout, 0, wx.ALL, 5)

        bSizer2.Add(sbSizer1, 1, wx.EXPAND, 5)
        text2 = '{:02X}'.format(status_vout_code)

        #text2 = '\033[0;34mtt\033[0m'
        #text2 = ('\033[36;1m'+str('{:02X}'.format(status_vout_code))+'\033[0m')
        my_box = wx.StaticBox(self, wx.ID_ANY, u"Status Iout 7B : "+text2)
        #my_box.SetForegroundColour(wx.BLUE)
        """
        my_box.SetLabelMarkup("<b>&ampBed</b> &ampmp "
                     "<span foreground='red'>breakfast</span> "
                     "available <big>HERE</big>")
        """

        #my_box.SetFont(3,)
        #my_box.Label = "Status Iout 7B : "+text2
        #my_box.SetBackgroundColour(wx.RED)
        sbSizer2 = wx.StaticBoxSizer(my_box, wx.VERTICAL)

        self.dgv_Status_iout = wx.grid.Grid(sbSizer2.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)
        status_iout = ["Iout OC Fault", "Iout OC LV Fault", "Iout OC Warning", "Iout UC Fault", "Current Share Fault",
                       "Power Limiting Mode", "Pout OP Fault", "Pout_OP_Warning"]
        # Grid
        self.dgv_Status_iout.CreateGrid(8, 1)
        self.dgv_Status_iout.EnableEditing(False)
        self.dgv_Status_iout.EnableGridLines(True)
        self.dgv_Status_iout.EnableDragGridSize(False)
        self.dgv_Status_iout.SetMargins(0, 0)

        # Columns
        self.dgv_Status_iout.SetColSize(0, 150)
        self.dgv_Status_iout.EnableDragColMove(False)
        self.dgv_Status_iout.EnableDragColSize(True)
        self.dgv_Status_iout.SetColLabelSize(0)
        self.dgv_Status_iout.SetColLabelAlignment(wx.ALIGN_CENTER, wx.ALIGN_CENTER)

        row2 = self.dgv_Status_iout.GetNumberRows()
        column2 = self.dgv_Status_iout.GetNumberCols()

        # Rows
        for row in range(row2):
            self.dgv_Status_iout.SetRowSize(row, 16)
            self.dgv_Status_iout.SetCellValue(row,0,status_iout[row])
        self.dgv_Status_iout.EnableDragRowSize(True)
        self.dgv_Status_iout.SetRowLabelSize(25)
        self.dgv_Status_iout.SetRowLabelValue(0, u"7")
        self.dgv_Status_iout.SetRowLabelValue(1, u"6")
        self.dgv_Status_iout.SetRowLabelValue(2, u"5")
        self.dgv_Status_iout.SetRowLabelValue(3, u"4")
        self.dgv_Status_iout.SetRowLabelValue(4, u"3")
        self.dgv_Status_iout.SetRowLabelValue(5, u"2")
        self.dgv_Status_iout.SetRowLabelValue(6, u"1")
        self.dgv_Status_iout.SetRowLabelValue(7, u"0")
        self.dgv_Status_iout.SetRowLabelAlignment(wx.ALIGN_CENTER, wx.ALIGN_CENTER)

        # Label Appearance

        # Cell Defaults
        self.dgv_Status_iout.SetDefaultCellBackgroundColour(wx.Colour(143, 188, 143))
        self.dgv_Status_iout.SetDefaultCellFont(
            wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "宋体"))
        self.dgv_Status_iout.SetDefaultCellAlignment(wx.ALIGN_LEFT, wx.ALIGN_CENTER)
        sbSizer2.Add(self.dgv_Status_iout, 0, wx.ALL, 5)

        bSizer2.Add(sbSizer2, 1, wx.EXPAND, 5)

        sbSizer3 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, u"Status Temp 7D"), wx.VERTICAL)

        self.dgv_Status_temp = wx.grid.Grid(sbSizer3.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)
        status_temp = ["OT Fault", "OT Wrning", "UT Warning", "UT Fault", "Resered", "Resered", "Resered", "Resered"]
        # Grid
        self.dgv_Status_temp.CreateGrid(8, 1)
        self.dgv_Status_temp.EnableEditing(False)
        self.dgv_Status_temp.EnableGridLines(True)
        self.dgv_Status_temp.EnableDragGridSize(False)
        self.dgv_Status_temp.SetMargins(0, 0)

        # Columns
        self.dgv_Status_temp.SetColSize(0, 150)
        self.dgv_Status_temp.EnableDragColMove(False)
        self.dgv_Status_temp.EnableDragColSize(True)
        self.dgv_Status_temp.SetColLabelSize(0)
        self.dgv_Status_temp.SetColLabelAlignment(wx.ALIGN_CENTER, wx.ALIGN_CENTER)

        row3 = self.dgv_Status_temp.GetNumberRows()
        column3 = self.dgv_Status_temp.GetNumberCols()

        # Rows
        for row in range(row3):
            self.dgv_Status_temp.SetRowSize(row, 16)
            self.dgv_Status_temp.SetCellValue(row,0,status_temp[row])
        self.dgv_Status_temp.EnableDragRowSize(True)
        self.dgv_Status_temp.SetRowLabelSize(25)
        self.dgv_Status_temp.SetRowLabelValue(0, u"7")
        self.dgv_Status_temp.SetRowLabelValue(1, u"6")
        self.dgv_Status_temp.SetRowLabelValue(2, u"5")
        self.dgv_Status_temp.SetRowLabelValue(3, u"4")
        self.dgv_Status_temp.SetRowLabelValue(4, u"3")
        self.dgv_Status_temp.SetRowLabelValue(5, u"2")
        self.dgv_Status_temp.SetRowLabelValue(6, u"1")
        self.dgv_Status_temp.SetRowLabelValue(7, u"0")
        self.dgv_Status_temp.SetRowLabelValue(8, wx.EmptyString)
        self.dgv_Status_temp.SetRowLabelAlignment(wx.ALIGN_CENTER, wx.ALIGN_CENTER)

        # Label Appearance

        # Cell Defaults
        self.dgv_Status_temp.SetDefaultCellBackgroundColour(wx.Colour(143, 188, 143))
        self.dgv_Status_temp.SetDefaultCellFont(
            wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "宋体"))
        self.dgv_Status_temp.SetDefaultCellAlignment(wx.ALIGN_LEFT, wx.ALIGN_CENTER)
        sbSizer3.Add(self.dgv_Status_temp, 0, wx.ALL, 5)

        bSizer2.Add(sbSizer3, 1, wx.EXPAND, 5)

        bSizer1.Add(bSizer2, 3, wx.EXPAND, 5)

        bSizer3 = wx.BoxSizer(wx.VERTICAL)

        sbSizer4 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, u"Status Word 79"), wx.VERTICAL)

        self.dgv_Status_word = wx.grid.Grid(sbSizer4.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)
        status_word = ["Vout", "Iout Pout", "Input", "MFR", "Power Good", "Fans", "Others", "Unknow", "Busy", "Output Off",
                       "Vout OV Fault", "Iout OC Fault", "Vin UV Fault", "Temperature", "CML", "None_Of_The_Above"]
        # Grid
        self.dgv_Status_word.CreateGrid(16, 1)
        self.dgv_Status_word.EnableEditing(False)
        self.dgv_Status_word.EnableGridLines(True)
        self.dgv_Status_word.EnableDragGridSize(False)
        self.dgv_Status_word.SetMargins(0, 0)

        # Columns
        self.dgv_Status_word.SetColSize(0, 150)
        self.dgv_Status_word.EnableDragColMove(False)
        self.dgv_Status_word.EnableDragColSize(True)
        self.dgv_Status_word.SetColLabelSize(0)
        self.dgv_Status_word.SetColLabelAlignment(wx.ALIGN_CENTER, wx.ALIGN_CENTER)

        row4 = self.dgv_Status_word.GetNumberRows()
        column4 = self.dgv_Status_word.GetNumberCols()

        # Rows
        for row in range(row4):
            self.dgv_Status_word.SetRowSize(row, 16)
            self.dgv_Status_word.SetCellValue(row,0,status_word[row])
        self.dgv_Status_word.EnableDragRowSize(True)
        self.dgv_Status_word.SetRowLabelSize(25)
        self.dgv_Status_word.SetRowLabelValue(0, u"F")
        self.dgv_Status_word.SetRowLabelValue(1, u"E")
        self.dgv_Status_word.SetRowLabelValue(2, u"D")
        self.dgv_Status_word.SetRowLabelValue(3, u"C")
        self.dgv_Status_word.SetRowLabelValue(4, u"B")
        self.dgv_Status_word.SetRowLabelValue(5, u"A")
        self.dgv_Status_word.SetRowLabelValue(6, u"9")
        self.dgv_Status_word.SetRowLabelValue(7, u"8")
        self.dgv_Status_word.SetRowLabelValue(8, u"7")
        self.dgv_Status_word.SetRowLabelValue(9, u"6")
        self.dgv_Status_word.SetRowLabelValue(10, u"5")
        self.dgv_Status_word.SetRowLabelValue(11, u"4")
        self.dgv_Status_word.SetRowLabelValue(12, u"3")
        self.dgv_Status_word.SetRowLabelValue(13, u"2")
        self.dgv_Status_word.SetRowLabelValue(14, u"1")
        self.dgv_Status_word.SetRowLabelValue(15, u"0")
        self.dgv_Status_word.SetRowLabelAlignment(wx.ALIGN_CENTER, wx.ALIGN_CENTER)

        # Label Appearance

        # Cell Defaults
        self.dgv_Status_word.SetDefaultCellBackgroundColour(wx.Colour(143, 188, 143))
        self.dgv_Status_word.SetDefaultCellFont(
            wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "宋体"))
        self.dgv_Status_word.SetDefaultCellAlignment(wx.ALIGN_LEFT, wx.ALIGN_CENTER)
        sbSizer4.Add(self.dgv_Status_word, 0, wx.ALL, 5)

        bSizer3.Add(sbSizer4, 1, wx.EXPAND, 5)

        sbSizer5 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, u"Status CML 7E"), wx.VERTICAL)

        self.dgv_Status_cml = wx.grid.Grid(sbSizer5.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)
        status_cml = ["Invalid CMD", "Invalid DATA", "PEC Faild", "Memory Fault", "Processor Fault", "Reserved",
                      "Other Cml Fault", "OtherMemoryOrLogic"]
        # Grid
        self.dgv_Status_cml.CreateGrid(8, 1)
        self.dgv_Status_cml.EnableEditing(False)
        self.dgv_Status_cml.EnableGridLines(True)
        self.dgv_Status_cml.EnableDragGridSize(False)
        self.dgv_Status_cml.SetMargins(0, 0)

        # Columns
        self.dgv_Status_cml.SetColSize(0, 150)
        self.dgv_Status_cml.EnableDragColMove(False)
        self.dgv_Status_cml.EnableDragColSize(True)
        self.dgv_Status_cml.SetColLabelSize(0)
        self.dgv_Status_cml.SetColLabelAlignment(wx.ALIGN_CENTER, wx.ALIGN_CENTER)

        row5 = self.dgv_Status_cml.GetNumberRows()
        column5 = self.dgv_Status_cml.GetNumberCols()

        # Rows
        for row in range(row5):
            self.dgv_Status_cml.SetRowSize(row, 16)
            self.dgv_Status_cml.SetCellValue(row,0,status_cml[row])
        self.dgv_Status_cml.EnableDragRowSize(True)
        self.dgv_Status_cml.SetRowLabelSize(25)
        self.dgv_Status_cml.SetRowLabelValue(0, u"7")
        self.dgv_Status_cml.SetRowLabelValue(1, u"6")
        self.dgv_Status_cml.SetRowLabelValue(2, u"5")
        self.dgv_Status_cml.SetRowLabelValue(3, u"4")
        self.dgv_Status_cml.SetRowLabelValue(4, u"3")
        self.dgv_Status_cml.SetRowLabelValue(5, u"2")
        self.dgv_Status_cml.SetRowLabelValue(6, u"1")
        self.dgv_Status_cml.SetRowLabelValue(7, u"0")
        self.dgv_Status_cml.SetRowLabelAlignment(wx.ALIGN_CENTER, wx.ALIGN_CENTER)

        # Label Appearance

        # Cell Defaults
        self.dgv_Status_cml.SetDefaultCellBackgroundColour(wx.Colour(143, 188, 143))
        self.dgv_Status_cml.SetDefaultCellFont(
            wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "宋体"))
        self.dgv_Status_cml.SetDefaultCellAlignment(wx.ALIGN_LEFT, wx.ALIGN_CENTER)
        sbSizer5.Add(self.dgv_Status_cml, 0, wx.ALL, 5)

        bSizer3.Add(sbSizer5, 1, wx.EXPAND, 5)

        bSizer1.Add(bSizer3, 3, wx.EXPAND, 5)

        bSizer4 = wx.BoxSizer(wx.VERTICAL)

        sbSizer6 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, u"Status Input 7C"), wx.VERTICAL)

        self.dgv_Status_input = wx.grid.Grid(sbSizer6.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)
        status_input = ["Vin OV Fault", "Vin OV Warning", "Vin LV Warning", "Vin UV Fault", "Unit Off For Low lV",
                        "lin OC Fault", "lin OC Warning", "Pin_OP_Warning"]
        # Grid
        self.dgv_Status_input.CreateGrid(8, 1)
        self.dgv_Status_input.EnableEditing(False)
        self.dgv_Status_input.EnableGridLines(True)
        self.dgv_Status_input.EnableDragGridSize(False)
        self.dgv_Status_input.SetMargins(0, 0)

        # Columns
        self.dgv_Status_input.SetColSize(0, 150)
        self.dgv_Status_input.EnableDragColMove(False)
        self.dgv_Status_input.EnableDragColSize(True)
        self.dgv_Status_input.SetColLabelSize(0)
        self.dgv_Status_input.SetColLabelAlignment(wx.ALIGN_CENTER, wx.ALIGN_CENTER)

        row6 = self.dgv_Status_input.GetNumberRows()
        column6 = self.dgv_Status_input.GetNumberCols()

        # Rows
        for row in range(row6):
            self.dgv_Status_input.SetRowSize(row, 16)
            self.dgv_Status_input.SetCellValue(row,0,status_input[row])
        self.dgv_Status_input.EnableDragRowSize(True)
        self.dgv_Status_input.SetRowLabelSize(25)
        self.dgv_Status_input.SetRowLabelValue(0, u"7")
        self.dgv_Status_input.SetRowLabelValue(1, u"6")
        self.dgv_Status_input.SetRowLabelValue(2, u"5")
        self.dgv_Status_input.SetRowLabelValue(3, u"4")
        self.dgv_Status_input.SetRowLabelValue(4, u"3")
        self.dgv_Status_input.SetRowLabelValue(5, u"2")
        self.dgv_Status_input.SetRowLabelValue(6, u"1")
        self.dgv_Status_input.SetRowLabelValue(7, u"0")
        self.dgv_Status_input.SetRowLabelAlignment(wx.ALIGN_CENTER, wx.ALIGN_CENTER)

        # Label Appearance

        # Cell Defaults
        self.dgv_Status_input.SetDefaultCellBackgroundColour(wx.Colour(143, 188, 143))
        self.dgv_Status_input.SetDefaultCellFont(
            wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "宋体"))
        self.dgv_Status_input.SetDefaultCellAlignment(wx.ALIGN_LEFT, wx.ALIGN_CENTER)
        sbSizer6.Add(self.dgv_Status_input, 0, wx.ALL, 5)

        bSizer4.Add(sbSizer6, 1, wx.EXPAND, 5)

        sbSizer7 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, u"Status Fan_1_2 81"), wx.VERTICAL)

        self.dgv_Status_fan_1_2 = wx.grid.Grid(sbSizer7.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)
        status_fan1_2 = ["Fan1 Fault", "Fan2 Fault", "Fan1 Warning", "Fan2 Warning", "Fan1 Speed Override",
                         "Fan2 Speed Override", "Air Flow Fault", "Air_Flow_Warning"]
        # Grid
        self.dgv_Status_fan_1_2.CreateGrid(8, 1)
        self.dgv_Status_fan_1_2.EnableEditing(False)
        self.dgv_Status_fan_1_2.EnableGridLines(True)
        self.dgv_Status_fan_1_2.EnableDragGridSize(False)
        self.dgv_Status_fan_1_2.SetMargins(0, 0)

        # Columns
        self.dgv_Status_fan_1_2.SetColSize(0, 150)
        self.dgv_Status_fan_1_2.EnableDragColMove(False)
        self.dgv_Status_fan_1_2.EnableDragColSize(True)
        self.dgv_Status_fan_1_2.SetColLabelSize(0)
        self.dgv_Status_fan_1_2.SetColLabelAlignment(wx.ALIGN_CENTER, wx.ALIGN_CENTER)

        row7 = self.dgv_Status_fan_1_2.GetNumberRows()
        column7 = self.dgv_Status_fan_1_2.GetNumberCols()

        # Rows
        for row in range(row7):
            self.dgv_Status_fan_1_2.SetRowSize(row, 16)
            self.dgv_Status_fan_1_2.SetCellValue(row,0,status_fan1_2[row])
        self.dgv_Status_fan_1_2.EnableDragRowSize(True)
        self.dgv_Status_fan_1_2.SetRowLabelSize(25)
        self.dgv_Status_fan_1_2.SetRowLabelValue(0, u"7")
        self.dgv_Status_fan_1_2.SetRowLabelValue(1, u"6")
        self.dgv_Status_fan_1_2.SetRowLabelValue(2, u"5")
        self.dgv_Status_fan_1_2.SetRowLabelValue(3, u"4")
        self.dgv_Status_fan_1_2.SetRowLabelValue(4, u"3")
        self.dgv_Status_fan_1_2.SetRowLabelValue(5, u"2")
        self.dgv_Status_fan_1_2.SetRowLabelValue(6, u"1")
        self.dgv_Status_fan_1_2.SetRowLabelValue(7, u"0")
        self.dgv_Status_fan_1_2.SetRowLabelAlignment(wx.ALIGN_CENTER, wx.ALIGN_CENTER)

        # Label Appearance

        # Cell Defaults
        self.dgv_Status_fan_1_2.SetDefaultCellBackgroundColour(wx.Colour(143, 188, 143))
        self.dgv_Status_fan_1_2.SetDefaultCellFont(
            wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "宋体"))
        self.dgv_Status_fan_1_2.SetDefaultCellAlignment(wx.ALIGN_LEFT, wx.ALIGN_CENTER)
        sbSizer7.Add(self.dgv_Status_fan_1_2, 0, wx.ALL, 5)

        bSizer4.Add(sbSizer7, 1, wx.EXPAND, 5)

        sbSizer8 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, u"Status Fan_3_4 81"), wx.VERTICAL)

        self.dgv_Status_fan_3_4 = wx.grid.Grid(sbSizer8.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)
        status_fan3_4 = ["Fan3 Fault", "Fan4 Fault", "Fan3 Warning", "Fan4 Warning", "Fan3 Speed Override",
                       "Fan4 Speed Override", "Reserved", "Reserved"]
        # Grid
        self.dgv_Status_fan_3_4.CreateGrid(8, 1)
        self.dgv_Status_fan_3_4.EnableEditing(False)
        self.dgv_Status_fan_3_4.EnableGridLines(True)
        self.dgv_Status_fan_3_4.EnableDragGridSize(False)
        self.dgv_Status_fan_3_4.SetMargins(0, 0)

        # Columns
        self.dgv_Status_fan_3_4.SetColSize(0, 150)
        self.dgv_Status_fan_3_4.EnableDragColMove(False)
        self.dgv_Status_fan_3_4.EnableDragColSize(True)
        self.dgv_Status_fan_3_4.SetColLabelSize(0)
        self.dgv_Status_fan_3_4.SetColLabelAlignment(wx.ALIGN_CENTER, wx.ALIGN_CENTER)

        row8 = self.dgv_Status_fan_3_4.GetNumberRows()
        column8 = self.dgv_Status_fan_3_4.GetNumberCols()

        # Rows
        for row in range(row8):
            self.dgv_Status_fan_3_4.SetRowSize(row, 16)
            self.dgv_Status_fan_3_4.SetCellValue(row,0,status_fan3_4[row])
        self.dgv_Status_fan_3_4.EnableDragRowSize(True)
        self.dgv_Status_fan_3_4.SetRowLabelSize(25)
        self.dgv_Status_fan_3_4.SetRowLabelValue(0, u"7")
        self.dgv_Status_fan_3_4.SetRowLabelValue(1, u"6")
        self.dgv_Status_fan_3_4.SetRowLabelValue(2, u"5")
        self.dgv_Status_fan_3_4.SetRowLabelValue(3, u"4")
        self.dgv_Status_fan_3_4.SetRowLabelValue(4, u"3")
        self.dgv_Status_fan_3_4.SetRowLabelValue(5, u"2")
        self.dgv_Status_fan_3_4.SetRowLabelValue(6, u"1")
        self.dgv_Status_fan_3_4.SetRowLabelValue(7, u"0")
        self.dgv_Status_fan_3_4.SetRowLabelAlignment(wx.ALIGN_CENTER, wx.ALIGN_CENTER)

        # Label Appearance

        # Cell Defaults
        self.dgv_Status_fan_3_4.SetDefaultCellBackgroundColour(wx.Colour(143, 188, 143))
        self.dgv_Status_fan_3_4.SetDefaultCellFont(
            wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "宋体"))
        self.dgv_Status_fan_3_4.SetDefaultCellAlignment(wx.ALIGN_LEFT, wx.ALIGN_CENTER)
        sbSizer8.Add(self.dgv_Status_fan_3_4, 0, wx.ALL, 5)

        bSizer4.Add(sbSizer8, 1, wx.EXPAND, 5)

        bSizer1.Add(bSizer4, 3, wx.EXPAND, 5)

        self.SetSizer(bSizer1)
        self.Layout()

        self.Centre(wx.BOTH)

    def __del__(self):
        pass


if __name__ == "__main__":
    app = wx.App()
    frame = status(None)
    frame.Show()
    app.MainLoop()
