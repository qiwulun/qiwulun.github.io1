import glob
import os
inputPath = './posts/*.org'
outputPath = r'~/git/hexo_demo/source/_posts/'

a = glob.glob(inputPath)

for iname in a:
    filename = ""
    filecontent=""
    with open(iname,"r") as ifile :
        for line in ifile.readlines():
            # print(line)
            if "#+BEGIN_COMMENT" in line or "#+END_COMMENT" in line or ".. slug:" in line or '# -*- mode: Org; org-download-image-dir: "../images"; -*-' in line:
                pass
            else:
                line=line.replace(".. title:","#+TITLE:")
                line=line.replace(".. date:","#+DATE:")
                line=line.replace("UTC+08:00", "" )
                line=line.replace(".. tags:","#+TAGS:")
                line=line.replace(".. category:","#+CATEGORY:")
                line=line.replace(".. link:","#+LINK:")
                line=line.replace(".. description:","#+DESCRIPTION:")
                line=line.replace(".. type: text","#+LAYOUT : post")
                line=line.replace(".. type: micro","#+LAYOUT : post") 
                line=line.replace("[[file:../images","[[file:images") 
                filecontent=filecontent+line
            if "../images" in line:
                print(line)
            if "#+TITLE" in line:
                filename = line.replace("#+TITLE:","").strip()
    os.renames(iname, "./posts/"+filename+".org")

    # with open(iname,"w") as f:
    #     f.writelines(filecontent)
