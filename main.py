import subprocess

def run_ffmpeg(cmd, fileName, outName):
    if not fileName:
        raise ValueError("fileName 不能为空")
    if not outName:
        raise ValueError("outName 不能为空")



def cmd(cutNumber, fileName, outName):
    # cmd命令拼接

    commend = a(fileName)
    print(type(commend), commend)
    i=0
    for e in range(cutNumber):

        commend = commend + b(cutTime, i) + c(cutTime, i) + d(outName,i)

        i += 1
    commend = commend + b(cutTime,i) + d(outName,i)
    return commend

def a(fileName):
    a = "ffmpeg -i " + fileName + ".mp4"
    return a
def b(cutTime, i):
    b = " -ss " + cutTime[i]
    return b


def c(cutTime, i):
    c = " -to " + cutTime[i + 1]
    return c


def d(outName, i):
    d = " -c copy " + outName + str((i + 1)) + ".mp4"
    return d
#a,b,c,d全是ffmpeg的部分拼接

#输入 输入文件名,文件名没有后缀，且要加上路径
print("plese input fileName")
fileName=input()

#输入 输出文件名，同输出文件名
print("plese input outName")
outName=input()


#输入裁剪点，记得一定要加上0点，因为这个和数组一样，包头不包尾，头必须要写。
print("plese input cutTime")
cutTime=input().split()
if cutTime[0] != "00:00:00":
    cutTime.insert(0, "00:00:00")

cutNumber= len(cutTime)-1


cmd=cmd(cutNumber,fileName,outName)
print(cmd)
try:
    subprocess.run(cmd, shell=True, check=True, text=True)
except subprocess.CalledProcessError:
        raise RuntimeError("ffmpeg 执行失败，请检查输入文件是否存在")










