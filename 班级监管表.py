from itertools import combinations
import random

# 提示用户输入人名，以中文逗号分隔
names_input = input("请输入人名，使用中文逗号隔开：")

# 使用中文逗号分割字符串，得到名单列表
names = [name.strip() for name in names_input.split("，") if name.strip()]

# Fisher-Yates洗牌算法
def fisher_yates_shuffle(arr):
    for i in range(len(arr)-1, 0, -1):
        j = random.randint(0, i)
        arr[i], arr[j] = arr[j], arr[i]
    return arr

# 生成所有可能的值日组合
all_combinations = list(combinations(names, 2))

# 初始化每个人的值日间隔天数
interval_days = {name: 0 for name in names}

# 安排值日表
schedule = []

# 当前天数
day = 0

# 预计天数
time = int(input("请输入预计天数：")) + 1

#选择模式
choose = input("请选择模式（输入 1 或者 2 ）：")
if choose == "1":
    # 直到生成满足条件的time天值日表
    while day < time:
        max_interval = -1
        best_combination = None
        for combination in all_combinations:
            # 计算组合中的最小间隔天数
            current_min_interval = min(interval_days[combination[0]], interval_days[combination[1]])
            if current_min_interval > max_interval:
                max_interval = current_min_interval
                best_combination = combination
        
        # 更新选中组合中每个人的间隔天数
        for name in names:
            if name in best_combination:
                interval_days[name] = 0
            else:
                interval_days[name] += 1
        
        # 添加最佳组合到值日表
        schedule.append(best_combination)
        day += 1

    # 显示最终的值日表
    for i, pair in enumerate(schedule, 1):
        print(f"第{i}天: {pair[0]}, {pair[1]}")
    input("Press ENTER to continue...")
else:
    # 生成time天的值日安排
    for day in range(1, time):
        # 每天都使用Fisher-Yates算法来随机排序值日组合
        shuffled_combinations = fisher_yates_shuffle(all_combinations.copy())
        
        # 从随机化的组合中选择一对作为当天的值日生
        duty_pair = shuffled_combinations[0]
        
        print(f"第{day}天: {duty_pair[0]}, {duty_pair[1]}")
    input("Press ENTER to continue...")
