erDiagram
	direction TB
	USER {
		string id PK ""  
		string first_name  ""  
		string last_name  ""  
		string email  ""  
		string password  ""  
		boolean is_admin  ""  
	}

	PLACE {
		string id PK ""  
		string title  ""  
		string description  ""  
		float price  ""  
		float latitude  ""  
		float longitude  ""  
		string owner_id FK ""  
	}

	REVIEW {
		string id PK ""  
		string text  ""  
		int rating  ""  
		string user_id FK ""  
		string place_id FK ""  
	}

	AMENITY {
		string id PK ""  
		string name  ""  
	}

	PLACE_AMENITY {
		string place_id PK,FK ""  
		string amenity_id PK,FK ""  
	}

	USER||--o{PLACE:"has"
	USER||--o{REVIEW:"writes"
	PLACE||--o{REVIEW:"has"
	PLACE||--o{PLACE_AMENITY:"has"
	AMENITY||--o{PLACE_AMENITY:"available_in"

