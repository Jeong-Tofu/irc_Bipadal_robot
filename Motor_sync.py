from dynamixel_sdk import *   

class LEG:

    count = 0 

    def __init__(self,ID_list,groupSyncWrite,packetHandler):
        self.ID_list = ID_list
        self.groupSyncWrite = groupSyncWrite
        self.packetHandler = packetHandler
        LEG.count += 1
        print("{}번째 다리 객체가 생성되었습니다.".format(LEG.count))

    # map함수 
    def map2(self,val, in_min, in_max, out_min, out_max):
        return int((val - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)

    def formap(self,val):
        return self.map2(val, -180, 180, 0, 4096)

    # sync 함수화 시키기 - 직접 움직임 - 3모터 제어
    def sync_motor_move(self,angle0,angle1,angle2,angle3,angle4,angle5):
        #print("모터를 움직인다")

        angle = [angle0 ,angle1, angle2, angle3, angle4, angle5]

        for ID in range(1,7):

            dxl_goal_position = self.formap(angle[ID - 1])

            # Allocate goal position value into byte array
            param_goal_position = [DXL_LOBYTE(dxl_goal_position), DXL_HIBYTE(dxl_goal_position)]

            # Add Dynamixel#1 goal position value to the Syncwrite parameter storage

            dxl_addparam_result = self.groupSyncWrite.addParam(self.ID_list[ID - 1], param_goal_position)

            if dxl_addparam_result != True:
                print("[ID:%03d] groupSyncWrite addparam failed" % self.ID_list[ID - 1])
                quit()
        
        # Syncwrite goal position
        dxl_comm_result = self.groupSyncWrite.txPacket()
        if dxl_comm_result != COMM_SUCCESS:
            print("%s" % self.packetHandler.getTxRxResult(dxl_comm_result))

        # Clear syncwrite parameter storage -- Tx Packet보내고 정리 해줘야 하나봄
        self.groupSyncWrite.clearParam()


    #Sync write에 사용되는 parameter만 저장 - 다중 제어
    def sync_param_add(self,angle0,angle1,angle2,angle3,angle4,angle5):
        #print("모터를 움직인다")

        angle = [angle0 ,angle1, angle2, angle3, angle4, angle5]

        for ID in range(1,7):

            dxl_goal_position = self.formap(angle[ID - 1])

            # Allocate goal position value into byte array
            param_goal_position = [DXL_LOBYTE(dxl_goal_position), DXL_HIBYTE(dxl_goal_position)]

            # Add Dynamixel#1 goal position value to the Syncwrite parameter storage

            dxl_addparam_result = self.groupSyncWrite.addParam(self.ID_list[ID - 1], param_goal_position)

            if dxl_addparam_result != True:
                print("[ID:%03d] groupSyncWrite addparam failed" % self.ID_list[ID - 1])
                quit()
        
       
   

