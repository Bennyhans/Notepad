def Addnote():   
    return dict()

def store():
    submitted_Title = request.vars.title
    submitted_Body = request.vars.body

    results = db.Memo.insert(
        db_Title=submitted_Title,
        db_Body=submitted_Body
    )

    if results:
        return "Note Saved Successfully"
    else:
        return "Error Please Check"