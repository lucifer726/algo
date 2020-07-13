# 在朋友列表中找到名字结尾为m的芒果销售商，朋友列表如下：
graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []

from collections import deque

search_queue = deque()
search_queue += graph["you"]


def search(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = []
    while search_queue:
        person = search_queue.popleft()
        if person not in searched:
            if person_is_seller(person):
                print(person + ' is a mango seller!')
                return True
            else:
                search_queue += graph[person]
                searched.append(person)


def person_is_seller(name):
    return name[-1] == 'm'

if __name__ == '__main__':
    search("you")
