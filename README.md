# BRIT Testing Project

## Overview
This repository contains automated API tests for the https://api.restful-api.dev/ REST API service testing PATCH method operations as well as UI WebSite Testing of britinsurance.com

## Setup
1. Clone repo & install dependencies:
```bash
git clone 
python -m venv venv
source venv/bin/activate 
pip install -r requirements.txt
PYTHONPATH=. pytest -s                 
PYTHONPATH=. pytest -m api 
PYTHONPATH=. pytest -m ui         
PYTHONPATH=. pytest -v             
PYTHONPATH=. pytest --html=report.html 

BRIT/
├── data/
├── tests/
│   ├── api/
│   │   └── test_patch_request.py
│   ├── ui/
│   │   ├── page_objects/
│   │       ├── cookie_page.py
│   │       ├── home_page.py
│   │       ├── test_ui_page.py
│   │       ├── base_page.py
│   │   └── test_ui_page.py
│   └── conftest.py
├── utils/
├── conftest.py
├── .env
├── .gitignore
├── configuration.properties
├── pytest.ini
├── README.md
└── requirements.txt
```

# Exploratory Testing Documentation for API

## Overview
**Date:** 13/11/2024  
**Component:** https://api.restful-api.dev/  
**Methods Tested:** GET, POST, PATCH, DELETE, PUT

## Test Scope
- All CRUD operations (GET, PUT, POST, DELETE, PATCH)
- Various payload structures
- Response validation
- Status code verification

## Setup
**Tools Used:**
- Postman for API testing
- API Documentation 

## Test Scenarios & Findings

| ID | Scenario | Expected | Actual | Status |
|----|----------|-----------|---------|--------|
| 1 | List all objects (Happy Path) | List all objects displayed | New data missing | ❌ |
| 2 | PATCH with invalid values | 400 Bad Request | 200 OK | ❌ |
| 3 | Unauthorized access | 401 Unauthorized | No auth mechanism | ❌ |
| 4 | Get objects by multiple IDs | All IDs in URI returned | Only first ID shown | ❌ |
| 5 | Response status codes | DELETE: 204 POST: 201 PUT: 201 PATCH: 201 GET: 200 | All return 200 | ❌ |

## Key Issues Found

### Critical Issues
1. Authentication/Authorization:
  - No authentication mechanism
  - No authorization controls
  - Missing 401 responses

2. Status Code Problems:  
  - All operations return 200
  - Missing proper error codes
  - Non-standard response codes

3. Data Retrieval Issues:
  - Multiple ID query limitation
  - New data not showing in list
  - Inconsistent responses

## General Observations
- URI consistency issues
- Missing authentication mechanisms
- Generalized 200 status codes
- Data retrieval inconsistencies

## Future Testing Recommendations
1. Load Testing:
  - Implement rate limiting
  - Performance testing
  - Stress testing

2. Security Testing:  
  - Authentication testing
  - Authorization validation
  - Security headers

3. Edge Cases:
  - Boundary value analysis
  - Special characters

## Summary
The API requires significant improvements in:
1. Security mechanisms
2. Status code implementation
3. Data consistency







Exploratory Testing Documentation 
Test Session Date: 13/11/2024
Tested Component: https://api.restful-api.dev/ for GET, POST, PATCH, DELETE, PUT methods

1. Session Overview
Session Charter:
Goal of the session is to explore the PATCH functionality to identify any issues with different payload structures, and verifying status codes.

Test scope is that it will cover GET, PUT, POST, DELETE, and PATCH methods with different payload structures. 

2. Setup
Tools Used:
Postman for API verification and API documentation provided. 

3. Test Scenarios and Observations
ID	Scenario Description	            Expected Outcome	            Actual Outcome	                  
1   List of all objects (HappyPath)     List of all objects displayed   Newly created data did not come up     
2	With PATCH, invalid values          400                             200
    should give proper status code 
3   With all methods, unauthorised 
    access should give proper code      401                             Authentication/Authorisation 
                                                                        not available  
4   List of objects by ids does bring
    all ids                             List of all ids in the uri      The second and the rest of ids
                                                                        does not show on the list
5   The codes for positive              DELETE 204, POST 201, PUT 201   All of them returning 200 status code  
    responses should be according to    PATCH 201, GET 200
    status conventions 

4. Session Notes
General Observations:
There seems to be a couple of issues with some of the URIs, no authenticatin and authorisation mechanisms are available, all status codes are generalised at 200.

Ideas for Future Testing:
Consider load testing, e.g. rate limiting.

6. Conclusion
Overall Summary of Findings:
S

Recommendations:
Any specific recommendations for developers, testers, or product managers based on this session’s findings.
Example: “Recommend implementing input validation for special characters in the search bar.”


