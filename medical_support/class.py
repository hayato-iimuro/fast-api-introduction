class Human:
    #Patientの親クラス
    
    def __init__(self, name):
        self.name = name



class Patient(Human):
    #Humanの子クラス
    #患者の症状と患者のIDを設定
    
    def __init__(self, name, patient_id, symptom):
        super().__init__(name)
        self.symptom = symptom
        self.patient_id = patient_id

class Clinic:
    def __init__(self):
        
        self.patients_list = []

        

        


        
    # 待ち人数表示
    def show_waiting_count(self):
        print(f"ただいまの待ち人数は{len(self.patients_list)}人です。")
        #(self.patients_list)は{}で囲む

    # 予約
    def reserve(self, patient):
        if self._check_reserved(patient):
            print(f'{patient.name}さんはすでに予約済みです。')
        else:
            print(f'{patient.name}さん予約完了')
            # 患者リストpatients_listにpatientを追加
            
            self.patients_list.append(patient)
    
    # 診察
    def diagnosis(self, patient_id=None):
        # 患者指定なしの場合順番に
        patient = None
        if patient_id == None:
            if len(self.patients_list)>0:
                patient = self.patients_list[0]
        else:
            for p in self.patients_list:
                if p.patient_id == patient_id:
                    patient = p
                    
        # 診察患者がいない場合
        if patient == None:
            print('診察する患者がいません。')
        else:
            print(f'{patient.name}さん、{patient.symptom}ですね。')
            
            print(f'診察終わりました。お大事に。')

            # 患者リストpatients_listから除外
            self.patients_list.remove(patient)
        
    # 予約済み確認
    def _check_reserved(self, patient):
        for p in self.patients_list:
            # 引数のpatientとpatients_listの中のpatient_idの比較
            if p.patient_id == patient_id:
                return True
        return False


myclinic = Clinic()




# 患者予約対象データ
# name、age、symptomの順
patients = [['佐藤', '111', '咳'],
           ['田中', '222', '腹痛'],
           ['鈴木', '333', '鼻水'],
           ['山田', '444', '倦怠感'],
           ['中田', '555', 'インフル'],]
 
# 患者予約
for p in patients:
    name, patient_id, symptom = p
    #アンパックというらしい
    #name = p[0]
    # age = p[1]
    # symptom = p[2]
    #と同じ処理が行われている
    
    # loopで取得する name, age, symptomでPatientをインスタンス
    patient = Patient(name, patient_id, symptom)

    # myclinicに予約 *reserveメソッド使用
    myclinic.reserve(patient)
 
# 現在の待ち人数を表示
myclinic.show_waiting_count()


# 自分の名前でインスタンス
me = Patient('中田', '555', 'インフル')
# 予約する
myclinic.reserve(me)
# 現在の待ち人数表示
myclinic.show_waiting_count()


# 診察
myclinic.diagnosis()
# 現在の待ち人数表示
myclinic.show_waiting_count()



# 診察 patient_id 555指定
myclinic.diagnosis(patient_id="555")
# 現在の待ち人数表示
myclinic.show_waiting_count()