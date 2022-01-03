import requests
from pprint import pprint

from client.github_client import API_URL, headers
from client.secret import User_Name


def createproject():
    create_project = requests.post(
        API_URL + "/user/projects", data='{"name": "test_project"}', headers=headers
    )
    pprint(create_project.json())


def createrepo():
    create_repo = requests.post(
        API_URL + "/user/repos", data='{"name":"test_repo"}', headers=headers
    )
    pprint(create_repo.json())


def deleteproject():
    pro_id = str(input("Enter project Id: "))
    delete_project = requests.delete(API_URL + f"/projects/{pro_id}", headers=headers)
    pprint(delete_project.text)


def deleterepo():
    repo = str(input("Enter repo name: "))
    delete_repo = requests.delete(
        API_URL + f"/repos/{User_Name}/{repo}", headers=headers
    )
    pprint(delete_repo.text)


def getprojects():
    get_projects = requests.get(
        API_URL + f"/users/{User_Name}/projects", headers=headers
    )
    pprint(get_projects.json())


def getrepos():
    get_repos = requests.get(API_URL + "/user/repos", headers=headers)
    pprint(get_repos.json())


def updateproject():
    pro_id = str(input("Enter project Id: "))
    update_project = requests.patch(
        API_URL + f"/projects/{pro_id}",
        data='{"name":"test_update_project"}',
        headers=headers,
    )
    pprint(update_project.json())


def updaterepo():
    repo_name = str(input("Enter repo name: "))
    update_repo = requests.patch(
        API_URL + f"/repos/{User_Name}/{repo_name}",
        data='{"name":"test_update_repo"}',
        headers=headers,
    )
    pprint(update_repo.json())


def userdetails():
    user_details = requests.get(API_URL + "/user", headers=headers)
    pprint(user_details.json())
