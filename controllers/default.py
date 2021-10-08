def register(): 
    return dict()

def store():  
    submitted_TITLE = request.vars.TITLE 
    submitted_ADDNOTES = request.vars.ADDNOTES 
     

    results = db.users.insert(      
        db_TITLE = submitted_TITLE,    
        db_ADDNOTES = submitted_ADDNOTES,  
         
                      )

    if results:      
        return "Notes Saved Successfully"   
    else:       
        return "An Error Occurred"




def seeNotes():
    users =db().select(db.users.ALL)
    return dict(users=users) 



def edit(): 
    parameters = request.args
    submitted_id = parameters[0]
    user = db(db.users.id ==submitted_id).select()[0] 
    return dict(user=user)


def update():
    submitted_TITLE = request.vars.TITLE  
    submitted_ADDNOTES = request.vars.body   
    submitted_id = request.vars.id  
    
    if db(db.users.id == submitted_id).select():

        db(db.users.id == submitted_id).update(
           db_TITLE=submitted_TITLE,
           db_ADDNOTES=submitted_ADDNOTES,
           ) 
        
        return redirect('seeNotes')

    else:
        return  'No Notes With this ID! <a href ="edit.html">Go back to edit notes'  

def delete():
    parameters = request.args
    submitted_id = parameters[0]

    if db(db.users.id == submitted_id).select():

        db(db.users.id == submitted_id).delete()
        return 'User Deleted Successfully'

    else:
        return 'No User With the ID found'


#def layout():
  #  return dict()
 #   

