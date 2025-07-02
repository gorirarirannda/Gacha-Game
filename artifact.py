import random

class Artifact:
    def __init__(self, part_name):
        self.part_name = part_name  # 花・羽など
        self.main_stat = self.generate_main_stat()
        self.sub_stats = self.generate_sub_stats()

    def generate_main_stat(self):
        if self.part_name == "flower":
            return ("HP実数", 717)
        elif self.part_name == "feather":
            return ("攻撃実数", 47)
        elif self.part_name == "sand":
            return self.random_weighted_choice({
                "HP%": 267,
                "攻撃%": 267,
                "防御%": 267,
                "熟知": 100,
                "元素チャージ効率": 99
            })
        elif self.part_name == "goblet":
            return self.random_weighted_choice({
                "HP%": 191,
                "攻撃%": 191,
                "防御%": 192,
                "熟知": 25,
                "風元素ダメ": 50,
                "岩元素ダメ": 50,
                "雷元素ダメ": 50,
                "草元素ダメ": 50,
                "水元素ダメ": 50,
                "炎元素ダメ": 50,
                "氷元素ダメ": 50,
                "物理ダメ": 51
            })
        elif self.part_name == "circlet":
            return self.random_weighted_choice({
                "攻撃%": 22,
                "防御%": 22,
                "HP%": 22,
                "熟知": 4,
                "会心率": 10,
                "会心ダメ": 10,
                "治癒効果": 10
            })

    def generate_sub_stats(self):
        sub_stat_candidates = {
            "攻撃実数": [14, 16, 18, 19],
            "防御実数": [16, 19, 21, 23],
            "熟知": [16, 19, 21, 23],
            "HP実数": [209, 239, 269, 299],
            "会心率": [2.7, 3.1, 3.5, 3.9],
            "会心ダメ": [5.4, 6.2, 7.0, 7.8],
            "元素チャージ効率": [4.5, 5.2, 5.8, 6.5],
            "HP%": [4.1, 4.7, 5.3, 5.8],
            "攻撃%": [4.1, 4.7, 5.3, 5.8],
            "防御%": [5.1, 5.8, 6.6, 7.3],
        }

        count = random.randint(3, 4)
        main_stat_name, _ = self.main_stat
        choices = [k for k in sub_stat_candidates.keys() if k != main_stat_name]
        random.shuffle(choices)

        sub_stats = []
        for stat in choices[:count]:
            value = random.choice(sub_stat_candidates[stat])
            sub_stats.append((stat, value))
        return sub_stats

    def random_weighted_choice(self, stat_weights):
        total = sum(stat_weights.values())
        r = random.randint(1, total)
        cumulative = 0
        for stat, weight in stat_weights.items():
            cumulative += weight
            if r <= cumulative:
                value = self.estimate_main_value(stat)
                return (stat, value)

    def estimate_main_value(self, stat):
        values = {
            "HP%": 7.0, "攻撃%": 7.0, "防御%": 8.7,
            "熟知": 28, "元素チャージ効率": 7.8,
            "風元素ダメ": 7.0, "岩元素ダメ": 7.0, "雷元素ダメ": 7.0,
            "草元素ダメ": 7.0, "水元素ダメ": 7.0, "炎元素ダメ": 7.0,
            "氷元素ダメ": 7.0, "物理ダメ": 7.0,
            "会心率": 9.3, "会心ダメ": 18.6, "治癒効果": 5.8
        }
        return values.get(stat, 0)

    def __str__(self):
        # 英語 → 日本語の部位変換表
        part_names = {
            "flower": "生の花",
            "feather": "死の羽",
            "sand": "時の砂",
            "goblet": "空の杯",
            "circlet": "理の冠"
        }

        # 「%」が必要なステータス名
        percent_stats = {
            "HP%", "攻撃%", "防御%", "会心率", "会心ダメ", "元素チャージ効率", "風元素ダメ", "岩元素ダメ",
            "雷元素ダメ", "草元素ダメ", "水元素ダメ", "炎元素ダメ", "氷元素ダメ", "物理ダメ", "治癒効果"
        }

        # メインステータス
        main_stat_name, main_stat_value = self.main_stat
        if main_stat_name in percent_stats:
            main_stat_value_str = f"{main_stat_value}%"
        else:
            main_stat_value_str = str(main_stat_value)

        result = f"{part_names.get(self.part_name, self.part_name)} - メイン: {main_stat_name} {main_stat_value_str}\n"

        # サブステータス
        for stat, val in self.sub_stats:
            val_str = f"{val}%" if stat in percent_stats else str(val)
            result += f"  サブ: {stat} {val_str}\n"

        return result

# 使用例
parts = ["flower", "feather", "sand", "goblet", "circlet"]
artifacts = [Artifact(random.choice(parts))]
for a in artifacts:
    print(a)

if __name__ == "__main__":
    parts = ["flower", "feather", "sand", "goblet", "circlet"]

    while True:
        print("----- 聖遺物生成 -----")
        artifact = Artifact(random.choice(parts))
        print(artifact)

        again = input("もう一度生成しますか？（y/n）: ").lower()
        if again != "y":
            print("終了します。")
            break
