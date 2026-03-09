# 第一章剧情模块 (基准脚本)

label chapter1_start:
    f "ch1_intro"
    
    menu:
        "where_to_go"
        
        "go_forest":
            jump chapter2_start
            
        "stay_here":
            f "ch1_stay"
            jump end_game
