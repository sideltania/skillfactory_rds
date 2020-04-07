def game_core_v2(number):
    count = 1
    predict = 50
    grl = 0
    grr = 100
    while number != predict:
        count+=1
        if number > predict: 
            grl = predict
            predict= round((grr-grl)/2+predict)
        elif number < predict: 
            grr = predict
            predict=round(predict - (grr-grl)/2)
            
    return(count) 

def score_game(game_core):
    count_ls = []
    np.random.seed(1) 
    random_array = np.random.randint(1,101, size=(10000))
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print("Ваш алгоритм угадывает число в среднем за {score} попыток")
    return(score)

score_game(game_core_v2)