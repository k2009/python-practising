# coding=UTF-8
import os

# 用Python修改 具有明确意义文件名的文件
def rename():
	path='/Volumes/myPhoto'
	renameType = '.NEF'

	filelist=os.listdir(path)#该文件夹下所有的文件（包括文件夹）
	for files in filelist:#遍历所有文件
		Olddir=os.path.join(path,files)#原来的文件路径
		if os.path.isdir(Olddir):#如果是文件夹则跳过
			continue
		filename=os.path.splitext(files)[0]#文件名
		filetype=os.path.splitext(files)[1]#文件扩展名

		if filetype == renameType:
			day = filename[0:2]
			month = filename[2:4]
			year = filename[4:6]
			hour = filename[7:9]
			minites = filename[9:11]

			newName =  '%s年%s月%s日%s时%s分' % (year,month,day,hour,minites)
			print newName

			Newdir=os.path.join(path,newName+filetype)#新的文件路径
			os.rename(Olddir,Newdir)#重命名

# rename()