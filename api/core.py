import requests

# Check web-production-0a28.up.railway.app/docs for API documentation
API_URL = "https://web-production-0a28.up.railway.app/runarp"

def requestApi(tracks, radius, width, runNumbers):
    # Request to API
    headers = {
        "Content-Type": "application/json"
    }
    data = {
        "track": tracks,
        "radius": radius,
        "width": width,
        "runNumbers": runNumbers
    }
    
    req = requests.post(API_URL, headers=headers, json=data)
    
    if(req.status_code == 200):
        req_json = req.json()
        data = req_json["data"]
        
        print("\n")
        print("Total distance: ", data["best_fitness"])
        print("Best solution:")
        for i in range(len(data["best_solution"])):
            if i == 0:
                print("Truck should start from track ", data["best_solution"][i])
            else:
                turn = "U-turn" if data["best_turns"][i-1]== 0 else "Omega-turn"
                print("Using ", turn,",truck should move to track ", data["best_solution"][i])
                
        # turn solution to int
        data["best_solution"] = [int(i) for i in data["best_solution"]]
        
        return {
            "status": True,
            "solution":data["best_solution"],
            "turns": data["best_turns"],
            "fitness": data["best_fitness"]
        } 
        
    else:
        return {
            "status":False,
            "error": req.status_code
        }