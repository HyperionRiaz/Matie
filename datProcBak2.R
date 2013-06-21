library("maatie")

args <- commandArgs(trailingOnly = TRUE)
#importedDat <- read.csv(paste("SelectedHealthWHO.csv", sep = ""), header = TRUE)
importedDat <- read.csv(paste("/var/www/files/",args[1],"/upload.csv", sep = ""), header = TRUE)

dims = dim(importedDat)
if(dims[1]<=500&&dims[2]<=25){
  #Compute the association matrix
  print("Computing the association matrix:")
  mat = as.matrix(tap(importedDat))
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
  names(aMatFram)<-names(importedDat)
  #write.table(aMatFram,file=paste("testoutputclean.csv", sep = ""),sep=",",row.names=F)
  write.table(aMatFram,file=paste("/var/www/files/",args[1],"/output.csv", sep = ""),sep=",",row.names=F)
  write.table(spearmanCODframe,file=paste("/var/www/files/",args[1],"/spearmanCODoutput.csv", sep = ""),sep=",",row.names=F)
  print("Done.")
  
  graphScale <- round(10*mean(mat),2)
  print("Generating the AGraph...")
  system(paste("python /var/www/pydot/createGraph.py /var/www/files/",args[1],"/ 0 ",graphScale, sep = ""))
  print("Done.")
}
else
{
  print("Our humblest apologies. We only process data files with a maximum of 25 variables, and 500 observations. I'm afraid all the output links will be broken. If you download the R code, you can run MAATIE without constraints.")
}