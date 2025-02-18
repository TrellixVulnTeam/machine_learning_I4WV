import pandas
import numpy
import os
import data as cd
import regression as cr
from sklearn import linear_model


def main():

    ## Read Data
    trainingData = pandas.read_csv(os.path.join(cd.data_dir(), cd.DataSets.EX1.value, 'train.csv'),
                                   header=0, index_col=0)
    #rs = numpy.random.RandomState(99)
    #newIndex = rs.choice(trainingData.index,trainingData.__len__())
    
    #trainingData = trainingData.loc[newIndex, :]
    
    yCols = ['y']
    xCols = trainingData.drop(columns=yCols).columns

    ## Set-up cross validation
    lambdaParam = [.1, 1, 10, 100, 1000]
    rmseVec = pandas.Series(index=[str(i) for i in lambdaParam], name='RMSE')
    #rmseVec = pandas.Series({key: None for key in lambdaParam}, name='RMSE)
    
    N = 50
    for l in lambdaParam:
        measuredRMSE = []
        for k in range(10):
            fold = numpy.arange(k * (N), ((k + 1) * 50))            
            mask = trainingData.index.isin(fold)
            
            X_t = trainingData.loc[~mask, xCols]
            y_t = trainingData.loc[~mask, yCols]

            X = trainingData.loc[mask, xCols]
            y = trainingData.loc[mask, yCols]
            #reg = linear_model.Ridge(alpha = l)
            #reg.fit(X_t,y_t)
            
            B = cr.ridge_regression(X=X_t, y=y_t, lambdaParam=l)
            betas = pandas.Series(data=B.flatten(), index=xCols)
        
            #betas = reg.coef_
            yFit = pandas.Series(X.dot(betas).values.flatten(), index=y.index, name='yFit')
            measuredRMSE.append(numpy.sqrt(numpy.mean((y.iloc[:, 0] - yFit)**2)))
        rmseVec[str(l)] = numpy.mean(measuredRMSE)

    print(rmseVec)
    rmseVec.to_csv(os.path.join(cd.data_dir(), cd.DataSets.EX1.value, '__sample.csv'), index=False)

if __name__ == '__main__':
    main()





