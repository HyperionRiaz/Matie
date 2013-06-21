library("maatie")
print("Getting args")
args <- commandArgs(trailingOnly = TRUE)
print(paste("I got passed:",args[[2]]))
print("Loading data")
#args = list("","Salary")
#importedDat <- read.csv(paste("baseballdat.csv", sep = ""), header = TRUE)
importedDat <- read.csv(paste("/var/www/files/",args[1],"/upload.csv", sep = ""), header = TRUE)
print("Done.")
AlistOVR <- function(dataSet,intName){
  
  drops <- c(intName)
  vOfInt <- dataSet[,(names(dataSet) %in% drops)]
  dataSet <- dataSet[,!(names(dataSet) %in% drops)]
  
  names <- names(dataSet)
  lr<-length(names)
  intNameMat <- array(-1, c(lr))
  compNameMat <- array(-1, c(lr))
  outMat <- array(-1, c(lr))
  pValMat <- array(-1, c(lr))
  spearmanMat <- array(-1, c(lr))
  linMat <- array(-1, c(lr))
  print(paste("One vs rest: Processing",toString(lr),"variables pairs"))
  for (i in 1:(lr)) {

      d <- data.frame(V1=vOfInt,V2=dataSet[,i])
      dok <- d[complete.cases(d),]
      if(is.numeric(dok[,1]) && is.numeric(dok[,2]) && length(dok[,1])>10){
        score <- ma(dok)
        aScore <- round(score$A,3)
        pVal <- paLookup(score)
        outMat[i]<-aScore 
        pValMat[i]<-pVal
        intNameMat[i]<-intName
        compNameMat[i]<-names[i]
        spearmanMat[i]<-round(cor(dok,method='spearman')[1,2]^2,3)
        if(outMat[i]>0){linMat[i] <- round(max(outMat[i]-spearmanMat[i],0)/outMat[i],3)}else{linMat[i] <- 0}
        if(pVal<0.05){print(paste(intName,"vs",names[i],": A=",aScore,", p=",format.pval(pVal),", nonlinearity=",linMat[i]))}
    }
  }  
  #dFrame<-data.frame(outMat,row.names = names)
  return(data.frame(V1=intNameMat,V2=compNameMat,A=outMat,pVal=pValMat,spearmanCOD=spearmanMat,nonLinearity=linMat))
}

print("Attempting to compute one-against-rest associations...")
dims = dim(importedDat)
if(dims[1]<=500&&dims[2]<=250){
  varNames<-names(importedDat)
  specName<-varNames[as.numeric(as.character(args[[2]]))]
  print(paste("Main variable:",specName))
  #specName<-args[[2]]
  #if(length(args)>2){specName <- do.call("paste", c(args[-1], sep = " "))}
  #if(length(args)>2){specName <- do.call("paste", c(args[-1], sep = " "))}else{specName<-args[[2]]}
  #Compute the association matrix
  alist <- AlistOVR(importedDat,specName)
  print("Done.")
  
  print("Exporting the data...")
  #write.table(alist,file=paste("testoutputcleanPval.csv", sep = ""),sep=",",row.names=F)
  write.table(alist,file=paste("/var/www/files/",args[1],"/outputOVR.csv", sep = ""),sep=",",row.names=F)
  print("Done.")
  
  print("Generating the .json graph file.")
  system(paste("python /var/www/pydot/createJson.py /var/www/files/",args[1],"/", sep = ""))
  print("Done.")
  
}else
{
  print("Our humblest apologies. For one-vs-rest analyses, we only process data files with a maximum of 250 variables, and 500 observations. I'm afraid all the output links will be broken. If you download the R code, you can run MAATIE without constraints.")
}