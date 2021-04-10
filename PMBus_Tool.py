import wx
import PMBus_Status
import Status
import time
from ctypes import *
import MCP_Driver as PMBusDriver
McpDriver = PMBusDriver.MCP_Driver()
McpDriver.MCP_Init()
Device_Add = 0xB0

class PMBus_Tool(object):
    def __init__(self):
        #Control initialization
        self.control_status = Status.status(None)
        self.Status = PMBus_Status.PMBus_Status()

        self._Color_Fault = wx.Colour(255, 69, 0)
        self._Color_Warn = wx.Colour(255, 69, 0)
        self._Color_None = wx.Colour(143, 188, 143)
        #_Color_None = Color.DarkSeaGreen
        #print(Status.Status_Input.State_Input_List)

    #region Set_Showed_State and update all the status Call --> Update_PMbus_Status();
    def Set_Status_Vout_State(self):

        self.control_status.dgv_Status_vout.SetCellBackgroundColour(0,0,self._Color_Fault) if \
            self.Status.Status_Vout.Vout_OV_Fault == True else \
            self.control_status.dgv_Status_vout.SetCellBackgroundColour(0, 0, self._Color_None)

        self.control_status.dgv_Status_vout.SetCellBackgroundColour(1, 0, self._Color_Warn) if \
            self.Status.Status_Vout.Vout_OV_Warning == True else \
            self.control_status.dgv_Status_vout.SetCellBackgroundColour(1, 0, self._Color_None)

        self.control_status.dgv_Status_vout.SetCellBackgroundColour(2, 0, self._Color_Warn) if \
            self.Status.Status_Vout.Vout_UV_Warning == True else \
            self.control_status.dgv_Status_vout.SetCellBackgroundColour(2, 0, self._Color_None)

        self.control_status.dgv_Status_vout.SetCellBackgroundColour(3, 0, self._Color_Fault) if \
            self.Status.Status_Vout.Vout_UV_Fault == True else \
            self.control_status.dgv_Status_vout.SetCellBackgroundColour(3, 0, self._Color_None)

        self.control_status.dgv_Status_vout.SetCellBackgroundColour(4, 0, self._Color_Warn) if \
            self.Status.Status_Vout.Vout_MAX_Warning == True else \
            self.control_status.dgv_Status_vout.SetCellBackgroundColour(4, 0, self._Color_None)

        self.control_status.dgv_Status_vout.SetCellBackgroundColour(5, 0, self._Color_Fault) if \
            self.Status.Status_Vout.TON_MAX_Fault == True else \
            self.control_status.dgv_Status_vout.SetCellBackgroundColour(5, 0, self._Color_None)

        self.control_status.dgv_Status_vout.SetCellBackgroundColour(6, 0, self._Color_Warn) if \
            self.Status.Status_Vout.TOFF_MAX_Warning == True else \
            self.control_status.dgv_Status_vout.SetCellBackgroundColour(6, 0, self._Color_None)

        self.control_status.dgv_Status_vout.SetCellBackgroundColour(7, 0, self._Color_Fault) if \
            self.Status.Status_Vout.Vout_Tracking_Error == True else \
            self.control_status.dgv_Status_vout.SetCellBackgroundColour(7, 0, self._Color_None)

    def Set_Status_Iout_State(self):

        self.control_status.dgv_Status_iout.SetCellBackgroundColour(0, 0, self._Color_Fault) if \
            self.Status.Status_Iout.Iout_OC_Fault == True else \
            self.control_status.dgv_Status_iout.SetCellBackgroundColour(0, 0, self._Color_None)

        self.control_status.dgv_Status_iout.SetCellBackgroundColour(1, 0, self._Color_Fault) if \
            self.Status.Status_Iout.Iout_OC_LV_Fault == True else \
            self.control_status.dgv_Status_iout.SetCellBackgroundColour(1, 0, self._Color_None)

        self.control_status.dgv_Status_iout.SetCellBackgroundColour(2, 0, self._Color_Warn) if \
            self.Status.Status_Iout.Iout_OC_Warning == True else \
            self.control_status.dgv_Status_iout.SetCellBackgroundColour(2, 0, self._Color_None)

        self.control_status.dgv_Status_iout.SetCellBackgroundColour(3, 0, self._Color_Fault) if \
            self.Status.Status_Iout.Iout_UC_Fault == True else \
            self.control_status.dgv_Status_iout.SetCellBackgroundColour(3, 0, self._Color_None)

        self.control_status.dgv_Status_iout.SetCellBackgroundColour(4, 0, self._Color_Fault) if \
            self.Status.Status_Iout.Current_Share_Fault == True else \
            self.control_status.dgv_Status_iout.SetCellBackgroundColour(4, 0, self._Color_None)

        self.control_status.dgv_Status_iout.SetCellBackgroundColour(5, 0, self._Color_Fault) if \
            self.Status.Status_Iout.Power_Limiting_Mode == True else \
            self.control_status.dgv_Status_iout.SetCellBackgroundColour(5, 0, self._Color_None)

        self.control_status.dgv_Status_iout.SetCellBackgroundColour(6, 0, self._Color_Fault) if \
            self.Status.Status_Iout.Pout_OP_Fault == True else \
            self.control_status.dgv_Status_iout.SetCellBackgroundColour(6, 0, self._Color_None)

        self.control_status.dgv_Status_iout.SetCellBackgroundColour(7, 0, self._Color_Warn) if \
            self.Status.Status_Iout.Pout_OP_Warning == True else \
            self.control_status.dgv_Status_iout.SetCellBackgroundColour(7, 0, self._Color_None)

    def Set_Status_Temp_State(self):

        self.control_status.dgv_Status_temp.SetCellBackgroundColour(0, 0, self._Color_Fault) if \
            self.Status.Status_Temp.OT_Fault == True else \
            self.control_status.dgv_Status_temp.SetCellBackgroundColour(0, 0, self._Color_None)

        self.control_status.dgv_Status_temp.SetCellBackgroundColour(1, 0, self._Color_Warn) if \
            self.Status.Status_Temp.OT_Warning == True else \
            self.control_status.dgv_Status_temp.SetCellBackgroundColour(1, 0, self._Color_None)

        self.control_status.dgv_Status_temp.SetCellBackgroundColour(2, 0, self._Color_Warn) if \
            self.Status.Status_Temp.UT_Warning == True else \
            self.control_status.dgv_Status_temp.SetCellBackgroundColour(2, 0, self._Color_None)

        self.control_status.dgv_Status_temp.SetCellBackgroundColour(3, 0, self._Color_Fault) if \
            self.Status.Status_Temp.UT_Fault == True else \
            self.control_status.dgv_Status_temp.SetCellBackgroundColour(3, 0, self._Color_None)

        self.control_status.dgv_Status_temp.SetCellBackgroundColour(4, 0, self._Color_Fault) if \
            self.Status.Status_Temp.Reseved1 == True else \
            self.control_status.dgv_Status_temp.SetCellBackgroundColour(4, 0, self._Color_None)

        self.control_status.dgv_Status_temp.SetCellBackgroundColour(5, 0, self._Color_Fault) if \
            self.Status.Status_Temp.Reseved2 == True else \
            self.control_status.dgv_Status_temp.SetCellBackgroundColour(5, 0, self._Color_None)

        self.control_status.dgv_Status_temp.SetCellBackgroundColour(6, 0, self._Color_Fault) if \
            self.Status.Status_Temp.Reseved3 == True else \
            self.control_status.dgv_Status_temp.SetCellBackgroundColour(6, 0, self._Color_None)

        self.control_status.dgv_Status_temp.SetCellBackgroundColour(7, 0, self._Color_Fault) if \
            self.Status.Status_Temp.Reseved4 == True else \
            self.control_status.dgv_Status_temp.SetCellBackgroundColour(7, 0, self._Color_None)

    def Set_Status_Input_State(self):

        self.control_status.dgv_Status_input.SetCellBackgroundColour(0, 0, self._Color_Fault) if \
            self.Status.Status_Input.Vin_OV_Fault == True else \
            self.control_status.dgv_Status_input.SetCellBackgroundColour(0, 0, self._Color_None)

        self.control_status.dgv_Status_input.SetCellBackgroundColour(1, 0, self._Color_Warn) if \
            self.Status.Status_Input.Vin_OV_Warning == True else \
            self.control_status.dgv_Status_input.SetCellBackgroundColour(1, 0, self._Color_None)

        self.control_status.dgv_Status_input.SetCellBackgroundColour(2, 0, self._Color_Warn) if \
            self.Status.Status_Input.Vin_LV_Warning == True else \
            self.control_status.dgv_Status_input.SetCellBackgroundColour(2, 0, self._Color_None)

        self.control_status.dgv_Status_input.SetCellBackgroundColour(3, 0, self._Color_Fault) if \
            self.Status.Status_Input.Vin_UV_Fault == True else \
            self.control_status.dgv_Status_input.SetCellBackgroundColour(3, 0, self._Color_None)

        self.control_status.dgv_Status_input.SetCellBackgroundColour(4, 0, self._Color_Fault) if \
            self.Status.Status_Input.Unit_Off_For_Low_IV == True else \
            self.control_status.dgv_Status_input.SetCellBackgroundColour(4, 0, self._Color_None)

        self.control_status.dgv_Status_input.SetCellBackgroundColour(5, 0, self._Color_Fault) if \
            self.Status.Status_Input.Iin_OC_Fault == True else \
            self.control_status.dgv_Status_input.SetCellBackgroundColour(5, 0, self._Color_None)

        self.control_status.dgv_Status_input.SetCellBackgroundColour(6, 0, self._Color_Warn) if \
            self.Status.Status_Input.Iin_OC_Warning == True else \
            self.control_status.dgv_Status_input.SetCellBackgroundColour(6, 0, self._Color_None)

        self.control_status.dgv_Status_input.SetCellBackgroundColour(7, 0, self._Color_Warn) if \
            self.Status.Status_Input.Pin_OP_Warning == True else \
            self.control_status.dgv_Status_input.SetCellBackgroundColour(7, 0, self._Color_None)

    def Set_Status_Cml_State(self):

        self.control_status.dgv_Status_cml.SetCellBackgroundColour(0, 0, self._Color_Fault) if \
            self.Status.Status_Cml.Invalid_CMD== True else \
            self.control_status.dgv_Status_cml.SetCellBackgroundColour(0, 0, self._Color_None)

        self.control_status.dgv_Status_cml.SetCellBackgroundColour(1, 0, self._Color_Fault) if \
            self.Status.Status_Cml.InValid_DATA == True else \
            self.control_status.dgv_Status_cml.SetCellBackgroundColour(1, 0, self._Color_None)

        self.control_status.dgv_Status_cml.SetCellBackgroundColour(2, 0, self._Color_Fault) if \
            self.Status.Status_Cml.Packet_Error_Check_Faild== True else \
            self.control_status.dgv_Status_cml.SetCellBackgroundColour(2, 0, self._Color_None)

        self.control_status.dgv_Status_cml.SetCellBackgroundColour(3, 0, self._Color_Fault) if \
            self.Status.Status_Cml.Memory_Fault == True else \
            self.control_status.dgv_Status_cml.SetCellBackgroundColour(3, 0, self._Color_None)

        self.control_status.dgv_Status_cml.SetCellBackgroundColour(4, 0, self._Color_Fault) if \
            self.Status.Status_Cml.Processor_Fault == True else \
            self.control_status.dgv_Status_cml.SetCellBackgroundColour(4, 0, self._Color_None)

        self.control_status.dgv_Status_cml.SetCellBackgroundColour(5, 0, self._Color_Fault) if \
            self.Status.Status_Cml.Reserved == True else \
            self.control_status.dgv_Status_cml.SetCellBackgroundColour(5, 0, self._Color_None)

        self.control_status.dgv_Status_cml.SetCellBackgroundColour(6, 0, self._Color_Fault) if \
            self.Status.Status_Cml.Other_Communication_Fault == True else \
            self.control_status.dgv_Status_cml.SetCellBackgroundColour(6, 0, self._Color_None)

        self.control_status.dgv_Status_cml.SetCellBackgroundColour(7, 0, self._Color_Fault) if \
            self.Status.Status_Cml.Other_Memory_Or_Logic_Fault == True else \
            self.control_status.dgv_Status_cml.SetCellBackgroundColour(7, 0, self._Color_None)

    def Set_Status_Mfr_State(self):
        pass

    def Set_Status_Fan_1_2_State(self):

        self.control_status.dgv_Status_fan_1_2.SetCellBackgroundColour(0, 0, self._Color_Fault) if \
            self.Status.Status_Fan_1_2.Fan1_Fault == True else \
            self.control_status.dgv_Status_fan_1_2.SetCellBackgroundColour(0, 0, self._Color_None)

        self.control_status.dgv_Status_fan_1_2.SetCellBackgroundColour(1, 0, self._Color_Fault) if \
            self.Status.Status_Fan_1_2.Fan2_Fault == True else \
            self.control_status.dgv_Status_fan_1_2.SetCellBackgroundColour(1, 0, self._Color_None)

        self.control_status.dgv_Status_fan_1_2.SetCellBackgroundColour(2, 0, self._Color_Warn) if \
            self.Status.Status_Fan_1_2.Fan1_Warning == True else \
            self.control_status.dgv_Status_fan_1_2.SetCellBackgroundColour(2, 0, self._Color_None)

        self.control_status.dgv_Status_fan_1_2.SetCellBackgroundColour(3, 0, self._Color_Warn) if \
            self.Status.Status_Fan_1_2.Fan2_Warning == True else \
            self.control_status.dgv_Status_fan_1_2.SetCellBackgroundColour(3, 0, self._Color_None)

        self.control_status.dgv_Status_fan_1_2.SetCellBackgroundColour(4, 0, self._Color_Fault) if \
            self.Status.Status_Fan_1_2.Fan1_Speed_Override == True else \
            self.control_status.dgv_Status_fan_1_2.SetCellBackgroundColour(4, 0, self._Color_None)

        self.control_status.dgv_Status_fan_1_2.SetCellBackgroundColour(5, 0, self._Color_Fault) if \
            self.Status.Status_Fan_1_2.Fan2_Speed_Override == True else \
            self.control_status.dgv_Status_fan_1_2.SetCellBackgroundColour(5, 0, self._Color_None)

        self.control_status.dgv_Status_fan_1_2.SetCellBackgroundColour(6, 0, self._Color_Fault) if \
            self.Status.Status_Fan_1_2.Air_Flow_Fault == True else \
            self.control_status.dgv_Status_fan_1_2.SetCellBackgroundColour(6, 0, self._Color_None)

        self.control_status.dgv_Status_fan_1_2.SetCellBackgroundColour(7, 0, self._Color_Warn) if \
            self.Status.Status_Fan_1_2.Air_Flow_Warning == True else \
            self.control_status.dgv_Status_fan_1_2.SetCellBackgroundColour(7, 0, self._Color_None)

    def Set_Status_Fan_3_4_State(self):
        self.control_status.dgv_Status_fan_3_4.SetCellBackgroundColour(0, 0, self._Color_Fault) if \
            self.Status.Status_Fan_3_4.Fan3_Fault == True else \
            self.control_status.dgv_Status_fan_3_4.SetCellBackgroundColour(0, 0, self._Color_None)

        self.control_status.dgv_Status_fan_3_4.SetCellBackgroundColour(1, 0, self._Color_Fault) if \
            self.Status.Status_Fan_3_4.Fan4_Fault == True else \
            self.control_status.dgv_Status_fan_3_4.SetCellBackgroundColour(1, 0, self._Color_None)

        self.control_status.dgv_Status_fan_3_4.SetCellBackgroundColour(2, 0, self._Color_Warn) if \
            self.Status.Status_Fan_3_4.Fan3_Warning == True else \
            self.control_status.dgv_Status_fan_3_4.SetCellBackgroundColour(2, 0, self._Color_None)

        self.control_status.dgv_Status_fan_3_4.SetCellBackgroundColour(3, 0, self._Color_Warn) if \
            self.Status.Status_Fan_3_4.Fan4_Warning == True else \
            self.control_status.dgv_Status_fan_3_4.SetCellBackgroundColour(3, 0, self._Color_None)

        self.control_status.dgv_Status_fan_3_4.SetCellBackgroundColour(4, 0, self._Color_Fault) if \
            self.Status.Status_Fan_3_4.Fan3_Speed_Override == True else \
            self.control_status.dgv_Status_fan_3_4.SetCellBackgroundColour(4, 0, self._Color_None)

        self.control_status.dgv_Status_fan_3_4.SetCellBackgroundColour(5, 0, self._Color_Fault) if \
            self.Status.Status_Fan_3_4.Fan4_Speed_Override == True else \
            self.control_status.dgv_Status_fan_3_4.SetCellBackgroundColour(5, 0, self._Color_None)

        self.control_status.dgv_Status_fan_3_4.SetCellBackgroundColour(6, 0, self._Color_Fault) if \
            self.Status.Status_Fan_3_4.Reserved1 == True else \
            self.control_status.dgv_Status_fan_3_4.SetCellBackgroundColour(6, 0, self._Color_None)

        self.control_status.dgv_Status_fan_3_4.SetCellBackgroundColour(7, 0, self._Color_Fault) if \
            self.Status.Status_Fan_3_4.Reserved2 == True else \
            self.control_status.dgv_Status_fan_3_4.SetCellBackgroundColour(7, 0, self._Color_None)

    def Set_Status_Word_State(self):
        # Higher byte
        self.control_status.dgv_Status_word.SetCellBackgroundColour(0, 0, self._Color_Fault) if \
            self.Status.Status_Word.Vout == True else \
            self.control_status.dgv_Status_word.SetCellBackgroundColour(0, 0, self._Color_None)

        self.control_status.dgv_Status_word.SetCellBackgroundColour(1, 0, self._Color_Fault) if \
            self.Status.Status_Word.Iout_Pout == True else \
            self.control_status.dgv_Status_word.SetCellBackgroundColour(1, 0, self._Color_None)

        self.control_status.dgv_Status_word.SetCellBackgroundColour(2, 0, self._Color_Fault) if \
            self.Status.Status_Word.Input == True else \
            self.control_status.dgv_Status_word.SetCellBackgroundColour(2, 0, self._Color_None)

        self.control_status.dgv_Status_word.SetCellBackgroundColour(3, 0, self._Color_Fault) if \
            self.Status.Status_Word.MFR == True else \
            self.control_status.dgv_Status_word.SetCellBackgroundColour(3, 0, self._Color_None)

        self.control_status.dgv_Status_word.SetCellBackgroundColour(4, 0, self._Color_Fault) if \
            self.Status.Status_Word.Power_Good == True else \
            self.control_status.dgv_Status_word.SetCellBackgroundColour(4, 0, self._Color_None)

        self.control_status.dgv_Status_word.SetCellBackgroundColour(5, 0, self._Color_Fault) if \
            self.Status.Status_Word.Fans == True else \
            self.control_status.dgv_Status_word.SetCellBackgroundColour(5, 0, self._Color_None)

        self.control_status.dgv_Status_word.SetCellBackgroundColour(6, 0, self._Color_Fault) if \
            self.Status.Status_Word.Others == True else \
            self.control_status.dgv_Status_word.SetCellBackgroundColour(6, 0, self._Color_None)

        self.control_status.dgv_Status_word.SetCellBackgroundColour(7, 0, self._Color_Fault) if \
            self.Status.Status_Word.Unknow == True else \
            self.control_status.dgv_Status_word.SetCellBackgroundColour(7, 0, self._Color_None)

        # Lower byte
        self.control_status.dgv_Status_word.SetCellBackgroundColour(8, 0, self._Color_Fault) if \
            self.Status.Status_Word.Busy == True else \
            self.control_status.dgv_Status_word.SetCellBackgroundColour(8, 0, self._Color_None)

        self.control_status.dgv_Status_word.SetCellBackgroundColour(9, 0, self._Color_Fault) if \
            self.Status.Status_Word.Output_Off == True else \
            self.control_status.dgv_Status_word.SetCellBackgroundColour(9, 0, self._Color_None)

        self.control_status.dgv_Status_word.SetCellBackgroundColour(10, 0, self._Color_Fault) if \
            self.Status.Status_Word.Vout_OV_Fault == True else \
            self.control_status.dgv_Status_word.SetCellBackgroundColour(10, 0, self._Color_None)

        self.control_status.dgv_Status_word.SetCellBackgroundColour(11, 0, self._Color_Fault) if \
            self.Status.Status_Word.Iout_OC_Fault == True else \
            self.control_status.dgv_Status_word.SetCellBackgroundColour(11, 0, self._Color_None)

        self.control_status.dgv_Status_word.SetCellBackgroundColour(12, 0, self._Color_Fault) if \
            self.Status.Status_Word.Vin_UV_Fault == True else \
            self.control_status.dgv_Status_word.SetCellBackgroundColour(12, 0, self._Color_None)

        self.control_status.dgv_Status_word.SetCellBackgroundColour(13, 0, self._Color_Fault) if \
            self.Status.Status_Word.Temperature == True else \
            self.control_status.dgv_Status_word.SetCellBackgroundColour(13, 0, self._Color_None)

        self.control_status.dgv_Status_word.SetCellBackgroundColour(14, 0, self._Color_Fault) if \
            self.Status.Status_Word.CML == True else \
            self.control_status.dgv_Status_word.SetCellBackgroundColour(14, 0, self._Color_None)

        self.control_status.dgv_Status_word.SetCellBackgroundColour(15, 0, self._Color_Fault) if \
            self.Status.Status_Word.None_Of_The_Above == True else \
            self.control_status.dgv_Status_word.SetCellBackgroundColour(15, 0, self._Color_None)

    def Update_PMbus_Status(self):
        self.Set_Status_Vout_State()
        self.Set_Status_Iout_State()
        self.Set_Status_Temp_State()
        self.Set_Status_Input_State()
        self.Set_Status_Cml_State()
        self.Set_Status_Mfr_State()
        self.Set_Status_Fan_1_2_State()
        self.Set_Status_Fan_3_4_State()
        self.Set_Status_Word_State()

    # endregion
    # region Set Pmbus Status and clear the UI so that we can see the flash effects

    def Set_Pmbus_Status_Data(self):

        self.Status.Status_Cml.Set_Status(self.Status.BT_Status_Cml)
        self.Status.Status_Fan_1_2.Set_Status(self.Status.BT_Status_Fan_1_2)
        self.Status.Status_Fan_3_4.Set_Status(self.Status.BT_Status_Fan_3_4)
        self.Status.Status_Input.Set_Status(self.Status.BT_Status_Input)
        self.Status.Status_Iout.Set_Status(self.Status.BT_Status_Iout)
        self.Status.Status_Mfr.Set_Status(self.Status.BT_Status_Mfr)
        self.Status.Status_Temp.Set_Status(self.Status.BT_Status_Temp)
        self.Status.Status_Vout.Set_Status(self.Status.BT_Status_Vout)
        self.Status.Status_Word.Set_Status(self.Status.WD_Status_Word) #word, int format


    def Clear_All_Status_Data(self):


        self.Status.Status_Cml.Set_Status(0)
        self.Status.Status_Fan_1_2.Set_Status(0)
        self.Status.Status_Fan_3_4.Set_Status(0)
        self.Status.Status_Input.Set_Status(0)
        self.Status.Status_Iout.Set_Status(0)
        self.Status.Status_Mfr.Set_Status(0)
        self.Status.Status_Temp.Set_Status(0)
        self.Status.Status_Vout.Set_Status(0)
        self.Status.Status_Word.Set_Status(0)


    def Get_All_Status_From_PSU(self):
        R_Data = (c_ubyte * 20)()

        if (McpDriver.MCP_I2C_Read(Device_Add, 0x7A, 2, R_Data) != 10):
            self.Status.BT_Status_Vout = R_Data[0]
        else:
            self.Status.BT_Status_Vout = 0xFF
            self.Status.BT_Status_Vout = R_Data[0]

        time.sleep(0.005)
        if (McpDriver.MCP_I2C_Read(Device_Add, 0x7B, 2, R_Data) != 10):
            self.Status.BT_Status_Iout = R_Data[0]
        else:
            self.Status.BT_Status_Iout = 0xFF
            self.Status.BT_Status_Iout = R_Data[0]

        time.sleep(0.005)
        if (McpDriver.MCP_I2C_Read(Device_Add, 0x7C, 2, R_Data) != 10):

            self.Status.BT_Status_Input = R_Data[0]

        else:
            self.Status.BT_Status_Input = 0xFF
            self.Status.BT_Status_Input = R_Data[0]

        time.sleep(0.005)
        if (McpDriver.MCP_I2C_Read(Device_Add, 0x7D, 2, R_Data) != 10):
            self.Status.BT_Status_Temp = R_Data[0]

        else:
            self.Status.BT_Status_Temp = 0xFF
            self.Status.BT_Status_Temp = R_Data[0]
        time.sleep(0.005)

        if (McpDriver.MCP_I2C_Read(Device_Add, 0x7E, 2, R_Data) != 10):
            self.Status.BT_Status_Cml = R_Data[0]
        else:
            Status.BT_Status_Cml = 0xFF
            Status.BT_Status_Cml = R_Data[0]


        time.sleep(0.005)

        if (McpDriver.MCP_I2C_Read(Device_Add, 0x80, 2, R_Data) != 10):
            self.Status.BT_Status_Mfr = R_Data[0]

        else:
            self.Status.BT_Status_Mfr = 0xFF
            self.Status.BT_Status_Mfr = R_Data[0]

        time.sleep(0.005)
        if (McpDriver.MCP_I2C_Read(Device_Add, 0x81, 2, R_Data) != 10):
            self.Status.BT_Status_Fan_1_2 = R_Data[0]

        else:
            self.Status.BT_Status_Fan_1_2 = 0xFF
            self.Status.BT_Status_Fan_1_2 = R_Data[0]

        time.sleep(0.005)
        if (McpDriver.MCP_I2C_Read(Device_Add, 0x79, 3, R_Data) != 10):
            # Status.WD_Status_Word = Convert.ToInt16(R_Data[0]) + Convert.ToInt16(R_Data[1] * 0x100)
            self.Status.WD_Status_Word = McpDriver.Linear11Conversion((R_Data[0]) + R_Data[1] * 256)

        else:
            self.Status.WD_Status_Word = 0xFFFF
            self.Status.WD_Status_Word = McpDriver.Linear11Conversion((R_Data[0]) + R_Data[1] * 256)

        # warning this used for status other
        if (McpDriver.MCP_I2C_Read(Device_Add, 0x7F, 2, R_Data) != 10):
            Status.BT_Status_Fan_3_4 = R_Data[0]

        else:
            self.Status.BT_Status_Fan_3_4 = 0xFF
            self.Status.BT_Status_Fan_3_4 = R_Data[0]

        time.sleep(0.005)
        if (McpDriver.MCP_I2C_Read(Device_Add, 0x82, 2, R_Data) != 10):
            Status.BT_Status_Fan_3_4 = R_Data[0]

        else:
            self.Status.BT_Status_Fan_3_4 = 0xFF
            self.Status.BT_Status_Fan_3_4 = R_Data[0]

    # endif
"""
    def Set_status_textbox(self):
        txb_Status_Word79.Text = String.Format("{0:X4}", self.Status.WD_Status_Word)
        txb_Status_Input7C.Text = String.Format("{0:X2}", self.Status.BT_Status_Input)
        txb_Status_Vout7A.Text = String.Format("{0:X2}", self.Status.BT_Status_Vout)
        txb_Status_Iout7B.Text = String.Format("{0:X2}", self.Status.BT_Status_Iout)
        txb_Status_Input7C.Text = String.Format("{0:X2}", self.Status.BT_Status_Input)
        txb_Status_Temp7D.Text = String.Format("{0:X2}", self.Status.BT_Status_Temp)
        txb_Status_CML7E.Text = String.Format("{0:X2}", self.Status.BT_Status_Cml)
        txb_Status_Fan181.Text = String.Format("{0:X2}", self.Status.BT_Status_Fan_1_2)
        txb_Status_Fan282.Text = String.Format("{0:X2}", self.Status.BT_Status_Fan_3_4)
        txb_Status_Mfr.Text = String.Format("{0:X2}", self.Status.BT_Status_Mfr)
"""
if __name__ == "__main__":
    app = wx.App()
    pmbus_tool = PMBus_Tool()
    control_status = pmbus_tool.control_status
    control_status.Show()
    app.MainLoop()