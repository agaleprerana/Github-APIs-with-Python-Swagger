from github_operations import (
    userdetails,
    getrepos,
    createrepo,
    createproject,
    updaterepo,
    deleterepo,
    getprojects,
    updateproject,
    deleteproject,
)

while True:
    print(
        "\n1.Get user details\n2.Get repos\n3.create Repo\n4.Update Repo\n5.Delete Repo\n6.Get projects\n7.Create "
        "project\n8.Update project\n9.Delete project"
    )
    num = int(input("\nEnter your choice (or 0 to quit):"))
    if num == 0:
        break
    elif num == 1:
        userdetails()
    elif num == 2:
        getrepos()
    elif num == 3:
        createrepo()
    elif num == 4:
        updaterepo()
    elif num == 5:
        deleterepo()
    elif num == 6:
        getprojects()
    elif num == 7:
        createproject()
    elif num == 8:
        updateproject()
    elif num == 9:
        deleteproject()
    else:
        print("enter correct option:")
