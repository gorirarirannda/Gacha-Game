import random

# Drop_of_artifacts =0 #聖遺物ドロップ数

# artifact_1_set = 0 #聖遺物1個目の聖遺物セット
artifact_1_type = 0 #聖遺物1個目の聖遺物タイプ0=花 1=羽 2=時計 3=杯 4=冠
artifact_1_main = 0 #聖遺物1個目のメインステータス0=攻撃実数 1=防御実数 2=熟知 3=HP実数 4=会心率 5=会心ダメ 6=元チャ 7=HP％  8=攻撃％ 9=防御％ 10=風元素ダメージ 11=岩元素ダメージ 12=雷元素ダメージ 13=草元素ダメージ 14=水元素ダメージ 15=炎元素ダメージ 16=氷元素ダメージ 17=物理ダメージ  18=与える治療効果
artifact_1_main_value = 0 #聖遺物1個目のメインステータス値(実数値または％)
artifact_1_sub = 0 #聖遺物1個目のサブステータス数(3または4)
artifact_1_sub_1 = 0 #聖遺物1個目のサブステータス1
artifact_1_sub_1_value = 0 #聖遺物1個目のサブステータス1値(実数値または％)
artifact_1_sub_2 = 0 #聖遺物1個目のサブステータス2
artifact_1_sub_2_value = 0 #聖遺物1個目のサブステータス2値(実数値または％)
artifact_1_sub_3 = 0 #聖遺物1個目のサブステータス3
artifact_1_sub_3_value = 0 #聖遺物1個目のサブステータス3値(実数値または％)
artifact_1_sub_4 = 0 #聖遺物1個目のサブステータス4
artifact_1_sub_4_value = 0 #聖遺物1個目のサブステータス4値(実数値または％)

'''
artifact_2_set = 0 #聖遺物2個目の聖遺物セット
artifact_2_type = 0 #聖遺物2個目の聖遺物タイプ0=花 1=羽 2=時計 3=杯 4=冠
artifact_2_main = 0 #聖遺物2個目のメインステータス0=攻撃実数 1=防御実数 2=熟知 3=HP実数 4=会心率 5=会心ダメ 6=元チャ 7=HP%  8=攻撃％ 9=防御％ 10=風元素ダメージ 11=岩元素ダメージ 12=雷元素ダメージ 13=草元素ダメージ 14=水元素ダメージ 15=炎元素ダメージ 16=氷元素ダメージ 17=物理ダメージ 18=与える治療効果
artifact_2_main_value = 0 #聖遺物2個目のメインステータス値(実数値または％)
artifact_2_sub = 0 #聖遺物2個目のサブステータス数(3または4)
artifact_2_sub_1 = 0 #聖遺物2個目のサブステータス1
artifact_2_sub_1_value = 0 #聖遺物2個目のサブステータス1値(実数値または％)
artifact_2_sub_2 = 0 #聖遺物2個目のサブステータス2
artifact_2_sub_2_value = 0 #聖遺物2個目のサブステータス2値(実数値または％)
artifact_2_sub_3 = 0 #聖遺物2個目のサブステータス3
artifact_2_sub_3_value = 0 #聖遺物2個目のサブステータス3値(実数値または％)
artifact_2_sub_4 = 0 #聖遺物2個目のサブステータス4
artifact_2_sub_4_value = 0 #聖遺物2個目のサブステータス4値(実数値または％)
'''

#聖遺物セット

#計算
artifact_1_type = random.randint(0, 4)  # 0=花 1=羽 2=時計 3=杯 4=冠
if artifact_1_type == 0:
    artifact_1_main = 3;  # HP実数 
    artifact_1_main_value = 717
elif artifact_1_type == 1:
    artifact_1_main = 0;  # 攻撃実数
    artifact_1_main_value = 47
elif artifact_1_type == 2:
    artifact_1_main = random.randint(1,1000)
    if 1<= artifact_1_main <= 267:
        artifact_1_main = 7; # HP%
        artifact_1_main_value = 7.0
    elif 267< artifact_1_main <= 534:
        artifact_1_main = 8; # 攻撃％
        artifact_1_main_value = 7.0
    elif 534 < artifact_1_main <= 801:
        artifact_1_main = 9; # 防御％
        artifact_1_main_value = 8.7
    elif 801 < artifact_1_main <= 901:
        artifact_1_main = 2; # 熟知
        artifact_1_main_value = 28
    elif 901< artifact_1_main <= 1000:
        artifact_1_main = 6; # 元素チャージ効率
        artifact_1_main_value = 7.8
elif artifact_1_type == 3:
    artifact_1_main = random.randint(1,1000)
    if 1 <= artifact_1_main <= 191:
        artifact_1_main = 7; # HP%
        artifact_1_main_value = 7.0
    elif 191 < artifact_1_main <= 383:
        artifact_1_main = 8; # 攻撃％
        artifact_1_main_value = 7.0
    elif 383 < artifact_1_main <= 575:
        artifact_1_main = 9; # 防御％
        artifact_1_main_value = 8.7
    elif 575 < artifact_1_main <= 600:
        artifact_1_main = 2; # 熟知
        artifact_1_main_value = 28
    elif 600 < artifact_1_main <= 650:
        artifact_1_main = 10; # 風元素ダメージ
        artifact_1_main_value = 7.0
    elif 650 < artifact_1_main <= 700:
        artifact_1_main = 11; # 岩元素ダメージ
        artifact_1_main_value = 7.0
    elif 700 < artifact_1_main <= 750:
        artifact_1_main = 12; # 雷元素ダメージ
        artifact_1_main_value = 7.0
    elif 750 < artifact_1_main <= 800:
        artifact_1_main = 13; # 草元素ダメージ
        artifact_1_main_value = 7.0
    elif 800 < artifact_1_main <= 850:
        artifact_1_main = 14; # 水元素ダメージ
        artifact_1_main_value = 7.0 
    elif 850 < artifact_1_main <= 900:
        artifact_1_main = 15; # 炎元素ダメージ
        artifact_1_main_value = 7.0
    elif 900 < artifact_1_main <= 950:
        artifact_1_main = 16; # 氷元素ダメージ
        artifact_1_main_value = 7.0
    elif 950 < artifact_1_main <= 1000:
        artifact_1_main = 17; # 物理ダメージ
        artifact_1_main_value = 7.0
elif artifact_1_type == 4:
    artifact_1_main = random.randint(1,100)
    if 1 <= artifact_1_main <= 22:
        artifact_1_main = 8; # 攻撃％
        artifact_1_main_value = 7.0
    elif 22 < artifact_1_main <= 44:
        artifact_1_main = 9; # 防御％
        artifact_1_main_value = 8.7
    elif 44 < artifact_1_main <= 66:
        artifact_1_main = 7; # HP%
        artifact_1_main_value = 7.0
    elif 66 < artifact_1_main <= 70:
        artifact_1_main = 2; # 熟知
        artifact_1_main_value = 28
    elif 70 < artifact_1_main <= 80:
        artifact_1_main = 4; # 会心率
        artifact_1_main_value = 9.3
    elif 80 < artifact_1_main <= 90:
        artifact_1_main = 5; # 会心ダメージ
        artifact_1_main_value = 18.6
    elif 90 < artifact_1_main <= 100:
        artifact_1_main = 18; # 与える治療効果
        artifact_1_main_value = 5.8

artifact_1_sub = random.randint(3, 4)  # サブステータス数(3または4)
if artifact_1_sub == 3:
    artifact_1_sub_1 = random.randint(0, 9)  # サブステータス1の種類
    while artifact_1_sub_1 == artifact_1_main: # メインステータスと同じサブステータスは出ない
        artifact_1_sub_1 = random.randint(0, 9)
    if artifact_1_sub_1 == 0:
        artifact_1_sub_1_value = random.choice([14, 16, 18, 19])  # 攻撃実数
    elif artifact_1_sub_1 == 1:
        artifact_1_sub_1_value = random.choice([16, 19, 21, 23]) # 防御実数
    elif artifact_1_sub_1 == 2:
        artifact_1_sub_1_value = random.choice([16, 19, 21, 23]) # 熟知
    elif artifact_1_sub_1 == 3:
        artifact_1_sub_1_value = random.choice([209, 239, 269, 299])  # HP実数
    elif artifact_1_sub_1 == 4:
        artifact_1_sub_1_value = random.choice([2.7, 3.1, 3.5, 3.9])  # 会心率
    elif artifact_1_sub_1 == 5:
        artifact_1_sub_1_value = random.choice([5.4, 6.2, 7.0, 7.8]) # 会心ダメージ
    elif artifact_1_sub_1 == 6:
        artifact_1_sub_1_value = random.choice([4.5, 5.2, 5.8, 6.5]) # 元素チャージ効率
    elif artifact_1_sub_1 == 7:
        artifact_1_sub_1_value = random.choice([4.1, 4.7, 5.3, 5.8])  # HP%
    elif artifact_1_sub_1 == 8:
        artifact_1_sub_1_value = random.choice([4.1, 4.7, 5.3, 5.8]) # 攻撃％
    elif artifact_1_sub_1 == 9:
        artifact_1_sub_1_value = random.choice([5.1, 5.8, 6.6, 7.3])  # 防御％

    artifact_1_sub_2 = random.randint(0, 9)  # サブステータス2の種類
    while artifact_1_sub_2 == artifact_1_main or artifact_1_sub_2 == artifact_1_sub_1: # 既に出たステータスと同じサブステータスは出ない
        artifact_1_sub_2 = random.randint(0, 9)
    if artifact_1_sub_2 == 0:
        artifact_1_sub_2_value = random.choice([14, 16, 18, 19])  # 攻撃実数
    elif artifact_1_sub_2 == 1:
        artifact_1_sub_2_value = random.choice([16, 19, 21, 23]) # 防御実数
    elif artifact_1_sub_2 == 2:
        artifact_1_sub_2_value = random.choice([16, 19, 21, 23]) # 熟知
    elif artifact_1_sub_2 == 3:
        artifact_1_sub_2_value = random.choice([209, 239, 269, 299])  # HP実数
    elif artifact_1_sub_2 == 4:
        artifact_1_sub_2_value = random.choice([2.7, 3.1, 3.5, 3.9])  # 会心率
    elif artifact_1_sub_2 == 5:
        artifact_1_sub_2_value = random.choice([5.4, 6.2, 7.0, 7.8]) # 会心ダメージ
    elif artifact_1_sub_2 == 6:
        artifact_1_sub_2_value = random.choice([4.5, 5.2, 5.8, 6.5]) # 元素チャージ効率
    elif artifact_1_sub_2 == 7:
        artifact_1_sub_2_value = random.choice([4.1, 4.7, 5.3, 5.8])  # HP%
    elif artifact_1_sub_2 == 8:
        artifact_1_sub_2_value = random.choice([4.1, 4.7, 5.3, 5.8]) # 攻撃％
    elif artifact_1_sub_2 == 9:
        artifact_1_sub_2_value = random.choice([5.1, 5.8, 6.6, 7.3])  # 防御％

    artifact_1_sub_3 = random.randint(0, 9)  # サブステータス3の種類
    while artifact_1_sub_3 == artifact_1_main or artifact_1_sub_3 == artifact_1_sub_1 or artifact_1_sub_3 == artifact_1_sub_2: # 既に出たステータスと同じサブステータスは出ない
        artifact_1_sub_3 = random.randint(0, 9)
    if artifact_1_sub_3 == 0:
        artifact_1_sub_3_value = random.choice([14, 16, 18, 19])  # 攻撃実数
    elif artifact_1_sub_3 == 1:
        artifact_1_sub_3_value = random.choice([16, 19, 21, 23]) # 防御実数
    elif artifact_1_sub_3 == 2:
        artifact_1_sub_3_value = random.choice([16, 19, 21, 23]) # 熟知
    elif artifact_1_sub_3 == 3:
        artifact_1_sub_3_value = random.choice([209, 239, 269, 299])  # HP実数
    elif artifact_1_sub_3 == 4:
        artifact_1_sub_3_value = random.choice([2.7, 3.1, 3.5, 3.9])  # 会心率
    elif artifact_1_sub_3 == 5:
        artifact_1_sub_3_value = random.choice([5.4, 6.2, 7.0, 7.8]) # 会心ダメージ
    elif artifact_1_sub_3 == 6:
        artifact_1_sub_3_value = random.choice([4.5, 5.2, 5.8, 6.5]) # 元素チャージ効率
    elif artifact_1_sub_3 == 7:
        artifact_1_sub_3_value = random.choice([4.1, 4.7, 5.3, 5.8])  # HP%
    elif artifact_1_sub_3 == 8:
        artifact_1_sub_3_value = random.choice([4.1, 4.7, 5.3, 5.8]) # 攻撃％
    elif artifact_1_sub_3 == 9:
        artifact_1_sub_3_value = random.choice([5.1, 5.8, 6.6, 7.3])  # 防御％

elif artifact_1_sub == 4:
    artifact_1_sub_1 = random.randint(0, 9)  # サブステータス1の種類
    while artifact_1_sub_1 == artifact_1_main: # メインステータスと同じサブステータスは出ない
        artifact_1_sub_1 = random.randint(0, 9)
    if artifact_1_sub_1 == 0:
        artifact_1_sub_1_value = random.choice([14, 16, 18, 19])  # 攻撃実数
    elif artifact_1_sub_1 == 1:
        artifact_1_sub_1_value = random.choice([16, 19, 21, 23]) # 防御実数
    elif artifact_1_sub_1 == 2:
        artifact_1_sub_1_value = random.choice([16, 19, 21, 23]) # 熟知
    elif artifact_1_sub_1 == 3:
        artifact_1_sub_1_value = random.choice([209, 239, 269, 299])  # HP実数
    elif artifact_1_sub_1 == 4:
        artifact_1_sub_1_value = random.choice([2.7, 3.1, 3.5, 3.9])  # 会心率
    elif artifact_1_sub_1 == 5:
        artifact_1_sub_1_value = random.choice([5.4, 6.2, 7.0, 7.8]) # 会心ダメージ
    elif artifact_1_sub_1 == 6:
        artifact_1_sub_1_value = random.choice([4.5, 5.2, 5.8, 6.5]) # 元素チャージ効率
    elif artifact_1_sub_1 == 7:
        artifact_1_sub_1_value = random.choice([4.1, 4.7, 5.3, 5.8])  # HP%
    elif artifact_1_sub_1 == 8:
        artifact_1_sub_1_value = random.choice([4.1, 4.7, 5.3, 5.8]) # 攻撃％
    elif artifact_1_sub_1 == 9:
        artifact_1_sub_1_value = random.choice([5.1, 5.8, 6.6, 7.3])  # 防御％

    artifact_1_sub_2 = random.randint(0, 9)  # サブステータス2の種類
    while artifact_1_sub_2 == artifact_1_main or artifact_1_sub_2 == artifact_1_sub_1: # 既に出たステータスと同じサブステータスは出ない
        artifact_1_sub_2 = random.randint(0, 9)
    if artifact_1_sub_2 == 0:
        artifact_1_sub_2_value = random.choice([14, 16, 18, 19])  # 攻撃実数
    elif artifact_1_sub_2 == 1:
        artifact_1_sub_2_value = random.choice([16, 19, 21, 23]) # 防御実数
    elif artifact_1_sub_2 == 2:
        artifact_1_sub_2_value = random.choice([16, 19, 21, 23]) # 熟知
    elif artifact_1_sub_2 == 3:
        artifact_1_sub_2_value = random.choice([209, 239, 269, 299])  # HP実数
    elif artifact_1_sub_2 == 4:
        artifact_1_sub_2_value = random.choice([2.7, 3.1, 3.5, 3.9])  # 会心率
    elif artifact_1_sub_2 == 5:
        artifact_1_sub_2_value = random.choice([5.4, 6.2, 7.0, 7.8]) # 会心ダメージ
    elif artifact_1_sub_2 == 6:
        artifact_1_sub_2_value = random.choice([4.5, 5.2, 5.8, 6.5]) # 元素チャージ効率
    elif artifact_1_sub_2 == 7:
        artifact_1_sub_2_value = random.choice([4.1, 4.7, 5.3, 5.8])  # HP%
    elif artifact_1_sub_2 == 8:
        artifact_1_sub_2_value = random.choice([4.1, 4.7, 5.3, 5.8]) # 攻撃％
    elif artifact_1_sub_2 == 9:
        artifact_1_sub_2_value = random.choice([5.1, 5.8, 6.6, 7.3])  # 防御％

    artifact_1_sub_3 = random.randint(0, 9)  # サブステータス3の種類
    while artifact_1_sub_3 == artifact_1_main or artifact_1_sub_3 == artifact_1_sub_1 or artifact_1_sub_3 == artifact_1_sub_2: # 既に出たステータスと同じサブステータスは出ない
        artifact_1_sub_3 = random.randint(0, 9)
    if artifact_1_sub_3 == 0:
        artifact_1_sub_3_value = random.choice([14, 16, 18, 19])  # 攻撃実数
    elif artifact_1_sub_3 == 1:
        artifact_1_sub_3_value = random.choice([16, 19, 21, 23]) # 防御実数
    elif artifact_1_sub_3 == 2:
        artifact_1_sub_3_value = random.choice([16, 19, 21, 23]) # 熟知
    elif artifact_1_sub_3 == 3:
        artifact_1_sub_3_value = random.choice([209, 239, 269, 299])  # HP実数
    elif artifact_1_sub_3 == 4:
        artifact_1_sub_3_value = random.choice([2.7, 3.1, 3.5, 3.9])  # 会心率
    elif artifact_1_sub_3 == 5:
        artifact_1_sub_3_value = random.choice([5.4, 6.2, 7.0, 7.8]) # 会心ダメージ
    elif artifact_1_sub_3 == 6:
        artifact_1_sub_3_value = random.choice([4.5, 5.2, 5.8, 6.5]) # 元素チャージ効率
    elif artifact_1_sub_3 == 7:
        artifact_1_sub_3_value = random.choice([4.1, 4.7, 5.3, 5.8])  # HP%
    elif artifact_1_sub_3 == 8:
        artifact_1_sub_3_value = random.choice([4.1, 4.7, 5.3, 5.8]) # 攻撃％
    elif artifact_1_sub_3 == 9:
        artifact_1_sub_3_value = random.choice([5.1, 5.8, 6.6, 7.3])  # 防御％
    artifact_1_sub_4 = random.randint(0, 9)  # サブステータス4の種類
    while artifact_1_sub_4 == artifact_1_main or artifact_1_sub_4 == artifact_1_sub_1 or artifact_1_sub_4 == artifact_1_sub_2 or artifact_1_sub_4 == artifact_1_sub_3: # 既に出たステータスと同じサブステータスは出ない
        artifact_1_sub_4 = random.randint(0, 9)
    if artifact_1_sub_4 == 0:
        artifact_1_sub_4_value = random.choice([14, 16, 18, 19])  # 攻撃実数
    elif artifact_1_sub_4 == 1:
        artifact_1_sub_4_value = random.choice([16, 19, 21, 23]) # 防御実数
    elif artifact_1_sub_4 == 2:
        artifact_1_sub_4_value = random.choice([16, 19, 21, 23]) # 熟知
    elif artifact_1_sub_4 == 3:
        artifact_1_sub_4_value = random.choice([209, 239, 269, 299])  # HP実数
    elif artifact_1_sub_4 == 4:
        artifact_1_sub_4_value = random.choice([2.7, 3.1, 3.5, 3.9])  # 会心率
    elif artifact_1_sub_4 == 5:
        artifact_1_sub_4_value = random.choice([5.4, 6.2, 7.0, 7.8]) # 会心ダメージ
    elif artifact_1_sub_4 == 6:
        artifact_1_sub_4_value = random.choice([4.5, 5.2, 5.8, 6.5]) # 元素チャージ効率
    elif artifact_1_sub_4 == 7:
        artifact_1_sub_4_value = random.choice([4.1, 4.7, 5.3, 5.8])  # HP%
    elif artifact_1_sub_4 == 8:
        artifact_1_sub_4_value = random.choice([4.1, 4.7, 5.3, 5.8]) # 攻撃％
    elif artifact_1_sub_4 == 9:
        artifact_1_sub_4_value = random.choice([5.1, 5.8, 6.6, 7.3])  # 防御％