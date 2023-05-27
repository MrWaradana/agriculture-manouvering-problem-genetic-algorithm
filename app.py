"""Main Application"""

import requests

# Check web-production-0a28.up.railway.app/docs for API documentation
API_URL = "https://web-production-0a28.up.railway.app/runarp"

def main():
    """Main Function"""
    
    ## 3 inputs from user
    # 1. Tracks
    tracks = int(input("Enter number of tracks: "))
    # 2. radius
    radius = float(input("Enter radius of the circle: "))
    # 3 width
    width = float(input("Enter width between each track: "))
    # 4. runNumbers
    runNumbers = int(input("Enter number of runs: "))
    
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
        
    else:
        print("Error: ", req.status_code)
    
    
    
if __name__ == "__main__":
    main()