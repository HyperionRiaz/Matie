#THIS POS DOES ONE AGAINST ALL PAIRS. NOT BLOODY HELPFUL!

library("maatie")

args <- commandArgs(trailingOnly = TRUE)
#importedDat <- read.csv(paste("SelectedHealthWHO.csv", sep = ""), header = TRUE)
importedDat <- read.csv(paste("/var/www/files/",args[1],"/upload.csv", sep = ""), header = TRUE)

dims = dim(importedDat)
if(dims[1]<=500&&dims[2]<=25){
  #Compute the association matrix
  print("Computing the association matrix:")
  mat = as.matrix(tap(importedDat,one = args[2]))
  spearmanCOD <- cor(as.matrix(importedDat), use='pairwise.complete.obs',method='spearman')^2
  spearmanCODframe <- data.frame(spearmanCOD,row.names = NULL)
  print("Done.")
  
  #Call the Agram function
  #print("Generating AGram...")
  #pdf(file=paste("Agram.pdf"), height=16, width=22)
  #pdf(file=paste("/var/www/files/",args[1],"/AgramOVR.pdf", sep = ""), height=dim(mat)[1], width=dim(mat)[1]*1.3)
  
  #Agram(importedDat,mat,one=args[2],order=FALSE)
  #dev.off()
  #png(filename=paste("Agram.png"),height=700, width=1000)
  #png(filename=paste("/var/www/files/",args[1],"/AgramOVR.png", sep = ""),height=dim(mat)[1]*40, width=dim(mat)[1]*60)
  #Agram(importedDat,mat,one=args[2],order=FALSE)
  #dev.off()
  #print("Done.")
  
  print("Exporting the data...")
  aMatFram<-data.frame(mat)
  names(aMatFram)<-names(importedDat)
  #write.table(aMatFram,file=paste("testoutputclean.csv", sep = ""),sep=",",row.names=F)
  write.table(aMatFram,file=paste("/var/www/files/",args[1],"/outputOVR.csv", sep = ""),sep=",",row.names=F)
  write.table(spearmanCODframe,file=paste("/var/www/files/",args[1],"/spearmanCODoutputOVR.csv", sep = ""),sep=",",row.names=F)
  print("Done.")
}
else
{
  print("Our humblest apologies. We only process data files with a maximum of 25 variables, and 500 observations. I'm afraid all the output links will be broken. If you download the R code, you can run MAATIE without constraints.")
}