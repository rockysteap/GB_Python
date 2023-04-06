http_status = '400'
match http_status:
    case '400':
        print("Bad Request")
    case 403:
        print("Forbidden")
    case 404:
        print("Not Found")
    case _:
        print("Other")