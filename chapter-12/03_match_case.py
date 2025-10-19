def http_status(status):
  match status:
    case 200:
      return "ok"
    case 404:
      return "Not Found"
    case 500:
      return "Internal Server Error"
    case _:
      return "Unknown status" # Usage print(http_status(200)) #Output:ok print(http_status(404)) # Not found print(http_status(500)) # Output : Internal server

print(http_status(500))      