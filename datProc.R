library("maatie")

args <- commandArgs(trailingOnly = TRUE)
#importedDat <- read.csv(paste("SelectedHealthWHO.csv", sep = ""), header = TRUE)
importedDat <- read.csv(paste("/var/www/files/",args[1],"/upload.csv", sep = ""), header = TRUE)


Alist <- function(dataSet){
  names <- names(dataSet)
  lr<-length(names)
  outMat <- array(-1, c(lr,lr))
  pValMat <- array(-1, c(lr,lr))
  print(paste("Processing",toString(lr),"variables.",toString(lr*(lr-1)/2),"pairs"))
  for (i in 1:(lr-1)) {
    for (j in (i+1):lr) {
      d <- data.frame(V1=dataSet[,i],V2=dataSet[,j])
      dok <- d[complete.cases(d),]
      if(is.numeric(dok[,1]) && is.numeric(dok[,2]) && length(dok[,1])>10){
        score <- ma(dok)
        aScore <- round(score$A,3)
        pVal <- paLookup(score)
        if(pVal<0.05){print(paste(names[i],"vs",names[j],": A=",aScore,", p=",format.pval(pVal)))}
        outMat[i,j]<-aScore
        outMat[j,i]<-aScore  
        pValMat[i,j]<-pVal
        pValMat[j,i]<-pVal
      }
    }
    print(paste(toString(i)," variable(s) complete",sep = ""))
  }  
  #dFrame<-data.frame(outMat,row.names = names)
  return(list(outMat,pValMat))
}

print("Computing the association matrix:")
dims = dim(importedDat)
if(dims[1]<=1000&&dims[2]<=35){
  #Compute the association matrix
  alist <- Alist(importedDat)
  mat = as.matrix(alist[[1]])
  spearmanCOD <- cor(as.matrix(importedDat), use='pairwise.complete.obs',method='spearman')^2
  spearmanCODframe <- data.frame(spearmanCOD,row.names = NULL)
  print("Done.")
  
  #Call the Agram function
  print("Generating AGram...")
  #pdf(file=paste("Agram.pdf"), height=16, width=22)
  pdf(file=paste("/var/www/files/",args[1],"/Agram.pdf", sep = ""), height=dim(mat)[1], width=dim(mat)[1]*1.3)
  
  Agram(importedDat,mat,order=FALSE)
  dev.off()
  #png(filename=paste("Agram.png"),height=700, width=1000)
  png(filename=paste("/var/www/files/",args[1],"/Agram.png", sep = ""),height=dim(mat)[1]*40, width=dim(mat)[1]*60)
  Agram(importedDat,mat,order=FALSE)
  dev.off()
  print("Done.")
  
  print("Exporting the data...")
  aMatFram<-data.frame(mat)
  aPFram<-data.frame(alist[[2]])
  names(aMatFram)<-names(importedDat)
  names(aPFram)<-names(importedDat)
  #write.table(aMatFram,file=paste("testoutputclean.csv", sep = ""),sep=",",row.names=F)
  #write.table(aPFram,file=paste("testoutputcleanPval.csv", sep = ""),sep=",",row.names=F)
  write.table(aMatFram,file=paste("/var/www/files/",args[1],"/output.csv", sep = ""),sep=",",row.names=F)
  write.table(aPFram,file=paste("/var/www/files/",args[1],"/outputPval.csv", sep = ""),sep=",",row.names=F)
  write.table(spearmanCODframe,file=paste("/var/www/files/",args[1],"/spearmanCODoutput.csv", sep = ""),sep=",",row.names=F)
  print("Done.")
  
  graphScale <- round(10*mean(mat),2)
  print("Generating the AGraph...")
  system(paste("python /var/www/pydot/createGraph.py /var/www/files/",args[1],"/ 0 ",graphScale, sep = ""))
  print("Done.")
}else
{
  print("Our humblest apologies. For comparisons involving all pairs we only process data files with a maximum of 25 variables, and 500 observations. I'm afraid all the output links will be broken. If you download the R code, you can run MAATIE without constraints.")
}
