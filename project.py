import sqlite3 as lite


# functionality goes here

class VideoManager(object):
    
    def __init__(self):
        global con
        con = lite.connect('videos.db')
        try:
            with con:
                cur = con.cursor()         
                cur.execute("CREATE TABLE IF NOT EXISTS video(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, description TEXT)") 
                cur.execute("CREATE TABLE IF NOT EXISTS tagged(id INTEGER PRIMARY KEY, tag1 TEXT DEFAULT null, tag2 TEXT default null, tag3 TEXT default null, tag4 TEXT default null, tag5 TEXT default null, FOREIGN KEY(id) REFERENCES video(id))")
        except Exception:
            print("Sorry! unable to create the database properly")
        
    #todo create data
    def insert_data(self, data, tagList):
        with con:
            cur = con.cursor()    
            cur.execute("INSERT INTO video(name, description) VALUES (?,?)", data)
            lastId = cur.lastrowid
            
            cur.execute("INSERT INTO tagged(id, tag1, tag2, tag3, tag4, tag5) VALUES (?,?,?,?,?,?)", (lastId, tagList[0], tagList[1], tagList[2], tagList[3], tagList[4]))
            return True
        
            
    
    #todo fetch data
    def fetch_data(self):
        try:
            with con:
                cur = con.cursor()
                cur.execute("SELECT * from video join tagged where video.id = tagged.id ")
                detail =  cur.fetchall()
                return detail
        except Exception:
            print("Oh my god, there is some error - fetch data ") 
    
    #todo delete data
    def delete_data(self, id):
        try:
            with con:
                cur = con.cursor()
                cur.execute("DELETE FROM video where id = ?", [id])
                return True
        except Exception:
            print("there is some erroe while deleting as per your given request")

#  user interface 

def main():
    print("*"*40)
    print("\n:: YOUTUBE VIDEO MANAGEMENT :: \n")
    print("*"*40)
    
    
    db = VideoManager()
    
    print("#"*40)
    print("\n :: User Manual :: \n")
    print("#"*40)
    print("\n")
    
    print("1. Insert a new video")
    print("2. Manage videos")
    print("3. Delete a video detail (id required)")
    print("#"*40)
    
    choice = input("\n Enter a choice: ")
    
    if choice == "1":
        name = input("\n Enter video name: \n")
        description = input("\n Enter video description: \n")
        
        tagList = [item for item in input ("enter tags (maximum five): ").split()]  
        if len(tagList) < 5:
            for i in range(len(tagList)+1, 6, 1):
                tagList.append(" ")            
    #help help todo todo TODO 
    
        if db.insert_data([name, description], tagList):
            print("Data Successfully Inserted")
        else:
            print("Oops! something went wrong")

    elif choice == "2":
        print("\n:: Video List ::")
        for index, item in enumerate(db.fetch_data()):            
            print("\n video id : ", item[0]) 
            print("video Name : ", item[1])
            print("video Description : ", item[3])
            print("Video tags :", item[4], item[5], item[6], item[7], item[8])
            
    elif choice == "3":
        video_id = input("Hey please enter the video id to delete: ")
        
        if db.delete_data(video_id):
            print("video was deleted with a success")
        else:
            print("Oops ! something went wrong")
        
    else:
        print("\n BAD CHOICE")                 
        
        
if __name__ == '__main__':
    main()