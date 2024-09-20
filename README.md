## Prerequisites
- Python3
- Docker
- Django
- NextJS
- Github Workflows
- Heroku
- Netlify

## Structure
```
.
└── prezi-technical-challenge
     └── monorepo
          ├── .github           contains GitHub Actions workflows for CI/CD - deploying BE and FE.
          ├── backend           contains the backend for the APIs. (presentaions app, parser, BE tests)
          ├── frontend          contains the frontend for the static website. (NextJS app, jest tests, 
```

## Possible improvements

- Improvement in parser considering batch processing for bulk data
- Integrate ElasticSearch and create documents for optimal search
- Add parsing of JSON as periodic action to see for duplicate results
- More unit tests especially for frontend application
- E2E tests using playwright
- Introduce authentication mechanism and add permissions for APIs
- Using cache with API views
- Update CI/CD workflow in a way that it sees the changes in specific directory and deploy applications 
  accordingly if needed - to avoid unwanted deployment cycles