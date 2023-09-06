car_make_list = ["chevy","ford","hyundai","honda","toyota"]
car_color_list = ["red","blue","green","orange","purple"]
car_model_list = ["impala","taurus","sonata","accord","camry"]
for make,model in zip(car_make_list,range(0,len(car_model_list),1)):
    for color in car_color_list:
        print(color,make,car_model_list[model],"\n","\bThe make is",make,\
              ",the color is",color,\
              ",and the model is",car_model_list[model],"\b.")