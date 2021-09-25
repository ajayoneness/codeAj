import facebook as fb

access_token ="EAAplekaKunEBAJURQDlrWgABrYfRD0GUNEXm7dkSSBPDYZBpYIabAZAiPdwxMjNaMKUBHebd6p4OgS62LBWG4mmKVUOuvIflaPGwktbpZAhUctftJSj56dTMO0U0gZCpee88WNtsSyYOFAGgmwBJ8L8ZCNUqcZCxtKkfXHklOxuacbickpIgX4GDCRgZAv8DcZAiE5lp50IZBGHlOwCZCwG5xr"

codepyfb = fb.GraphAPI(access_token)
print(codepyfb)
#codepyfb.put_object("me","feed", message = "hello")
codepyfb.put_photo(open(),message="Live Corona Update")