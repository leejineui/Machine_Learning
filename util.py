# 평가지표 출력 함수 
from sklearn.metrics import accuracy_score, recall_score, precision_score, f1_score,mean_squared_error, r2_score
def print_metrics(y,pred,title=None):
    acc= accuracy_score(y, pred)
    recall =recall_score(y,pred)
    precision =precision_score(y, pred)
    f1=f1_score(y,pred)
    
    if title:
        print(title)
    print(f'acc: {acc}, recall:{recall}, Precision :{precision}, f1점수:{f1}')
    
    
    
def print_regression_metrics(y,pred, title=None):
    mse = mean_squared_error(y,pred)
    rmse =np.sqrt(mse)
    r2=r2_score(y,pred)
    if title:
        print(title)
    print(f'MSE:{mse}, RMSE:{rmse}, R2: {r2}')
    print('_' *100)
