data <- read.csv("R/titanic.csv",sep = "\t")
library(randomForest)

data <- as.data.frame(data)
data <- data[,!(names(data) %in% c("PassengerId","Name","Ticket","Cabin","Embarked"))]
data <- na.omit(data)
model <- randomForest(as.factor(Survived)~., data= data, ntree=500)

names(data)
particular <- data.frame(Pclass=3, Sex=factor("male",levels=c("male","female")), Age=2, SibSp=3, Parch=1, Fare = 10.0)
pred <- predict(model,particular,type = "prob")
pred
