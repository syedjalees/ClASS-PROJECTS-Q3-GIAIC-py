import os

def main():
    i = 0
    path ="E:/GI-AIWMD/Quarter 3/Sir Zia Project/CLASSPROJECTS/project4-assignments/Assignment-01/Bulk-File-Re-namer/img/"
    for filename in os.listdir(path):
        my_dest = "image" + str(i) + ".jpg"
        my_source =path + filename
        my_dest =path + my_dest
        os.rename(my_source, my_dest)
        i += 1
        
if __name__ == "__main__":
    main()