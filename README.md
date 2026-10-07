# Challenge Catastrophe

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-3.1.3-green)](https://flask.palletsprojects.com/)
[![SocketIO](https://img.shields.io/badge/Flask--SocketIO-5.6.1-lightblue)](https://flask-socketio.readthedocs.io/)
[![Tests](https://img.shields.io/badge/Tests-Selenium%2BPytest-yellow)](https://www.selenium.dev/)
[![Deployment](https://img.shields.io/badge/Deployment-Render-blueviolet)](https://render.com/)
[![License](https://img.shields.io/badge/License-Educational-orange)](#license)

CITS3200 capstone project — a multiplayer online game built for Yi Fei Wu, University of Western Australia.

> A multiplayer, browser-based strategy game built as a CITS3200 capstone project. Teams join shared sessions, review mission briefings, spend a shared budget on equipment, and complete timed challenges in hostile environments. The game combines cooperative planning, resource management, and fast decision-making into a complete mission-focused gameplay experience.

**Play now:** [https://cits3200-project.onrender.com/join](https://cits3200-project.onrender.com/join)

## Team

UWA ID | Name | GitHub Username  
--- | --- | ---  
23957309 | Abbey Boyle  |    JubileeBee
24223498 | Angela Hewitt	 |   Angela74180
24224304 | Bernadette Arto | BernadetteAx
23356687 | Alon Tucker	 |   ATcoding613
23867057 | Namgay Choden | Nchoden
24167087 | Jo Magnampo	 |   JoLZ18
---

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Architecture](#architecture-overview)
- [Getting Started](#getting-started)
- [Gameplay Guide](#gameplay-guide)
- [Testing](#testing)
- [Deployment](#deployment)
- [Contributing](#contributing)
- [Project Highlights](#project-highlights)
- [License](#license)

---

## Overview

Challenge Catastrophe is a team-based online game where players:
- host or join a game session,
- prepare for a mission with a shared budget,
- vote on equipment purchases in a shop phase,
- complete a sequence of challenge events under time pressure,
- and finish with a scored outcome based on overall performance.

The game is built with Python and Flask, with real-time communication handled through Flask-SocketIO. Core mechanics are data-driven, allowing mission descriptions, item definitions, and environment information to be configured without major code changes.

This project was designed to showcase practical software engineering skills in a full-stack web application: real-time multiplayer interactions, dynamic game state management, data-driven content generation, and responsive frontend experience.

### Project Goals

The project focuses on building a game that is:
- multiplayer and session-based
- visually rich and interactive
- dynamically generated from structured game data
- feature-complete across a full game flow
- suitable as a portfolio-level example of applied software design

The project demonstrates:
- backend architecture for live multiplayer state
- frontend interaction patterns for game screens and UI flow
- modular Python code design
- data modelling for missions and game world content
- testing through browser automation and unit-style validation

---

## Features

### Core Gameplay

- **Multiplayer Sessions** — Real-time player synchronization using WebSockets
- **Shared Team Economy** — Single shared budget creates strategic trade-offs and encourages communication
- **Data-Driven Missions** — Mission templates encoded as structured data for easy extension and variation
- **Dynamic Challenge Generation** — Challenges tied to locations and mission types for replayability
- **Timed Execution** — 60-second countdown for each challenge creates urgency and strategic decision-making
- **Collaborative Voting** — Team votes on equipment purchases during the item shop phase

### Technical Features

- **Real-Time Communication** — SocketIO for instantaneous state synchronization across all players
- **Modular Architecture** — Clear separation between routes, handlers, game logic, and data
- **Extensible Content System** — New missions, items, and challenges can be added without code changes
- **Responsive Web UI** — Pixel-art aesthetic with dark mode and vibrant accents supporting desktop and mobile
- **Browser Testing** — Automated Selenium tests validate full game flow with multiple simultaneous players

---

## Tech Stack

### Backend
- **Python 3.10+** — Core application language
- **Flask 3.1.3** — Web framework and HTTP server
- **Flask-SocketIO 5.6.1** — Real-time bidirectional communication
- **Gunicorn** — Production WSGI server
- **Gevent** — Lightweight concurrency for SocketIO

### Frontend
- **JavaScript (ES6+)** — Client-side game logic
- **HTML5** — Semantic markup
- **CSS3** — Styling with responsive design and animations

### Testing & Deployment
- **Selenium 4.20+** — Browser automation and integration testing
- **Pytest** — Test framework
- **Render** — Cloud deployment platform
- **GitHub** — Version control and collaboration

---

## Architecture overview

The application is organised around a lightweight Flask app with modular route handling and SocketIO-based game events.

### Main structure

```text
CITS3200-Project/
├── app/
│   ├── __init__.py
│   ├── extensions.py
│   ├── routes.py
│   ├── game_data/
│   │   ├── example_mission.py
│   │   ├── items.py
│   │   ├── location_info.py
│   │   ├── mission_structs.py
│   │   └── ...
│   ├── services/
│   ├── sockets/
│   │   ├── __init__.py
│   │   ├── handlers/
│   │   └── ...
│   ├── static/
│   │   ├── css/
│   │   ├── js/
│   │   └── images/
│   └── templates/
│       ├── join.html
│       ├── lobby.html
│       ├── start_game.html
│       ├── mission_description.html
│       ├── auction.html
│       ├── mission.html
│       ├── result_page.html
│       └── ...
├── app.py
├── requirements.txt
├── CONTRIBUTING.md
├── docs/
├── decisions/
├── selenium_tests/
├── tests/
├── README.md
└── .gitignore
```

---

### Backend Architecture

**Flask App Initialization** (`app/__init__.py`)
- Creates Flask application instance
- Initialises SocketIO for real-time communication
- Registers HTTP routes and Socket event handlers

**HTTP Routes** (`app/routes.py`)
- Serves HTML templates for each game phase
- Provides visual catalog data to templates (missions, locations, items)

**SocketIO Handlers** (`app/sockets/handlers/`)
- Manages game session state (players, turns, phase transitions)
- Broadcasts state changes to all players in a session
- Handles voting, purchases, challenge progression, and results

**Game Data** (`app/game_data/`)
- Mission templates with challenge chains
- Item catalog with cost/description metadata
- Location descriptions and environmental context
- Challenge definitions linked to specific scenarios

### Frontend Architecture

**Client Socket Communication** (`app/static/js/`)
- Connects to SocketIO server
- Listens for game state updates
- Sends player actions (votes, item selections, challenge responses)
- Manages page transitions based on phase changes

**Game UI** (`app/static/css/`)
- Responsive design supporting desktop and mobile
- Pixel-art themed aesthetic
- Dark mode with vibrant accent colours
- State-driven animations and transitions

**Templates** (`app/templates/`)
- Jinja2-based HTML with reusable macro components
- Each game phase has its own template
- Base template provides shared header, navigation, and asset loading

---

## Getting Started

### Prerequisites

- Python 3.10 or later
- pip package manager
- Virtual environment tool (recommended)
- Browser with WebSocket support

### Installation

Clone the repository:
```bash
git clone https://github.com/BernadetteAx/CITS3200-Project.git
cd CITS3200-Project
```

Create and activate a virtual environment:
```bash
python3 -m venv .venv
source .venv/bin/activate   # On Windows: .venv\Scripts\activate
```

Install dependencies:
```bash
pip install -r requirements.txt
```

---

## Running it locally

### Start the Flask development server:
```bash
flask --app app run
```
OR:
```bash
python app.py
```

The application will be available at:
```bash
http://localhost:5000/join
```

---

## Testing Locally with Multiple Players
To test multiplayer functionality:

- Open the join page in two browser tabs (or separate browser windows)
- One player clicks "Host a Game" and receives a session code
- The other player enters their name, the session code, and clicks "Join Game"
- Both players proceed through the game phases together

---

## Gameplay Guide

### Game Flow
The game progresses through six distinct phases:

### Code

> JOIN/HOST → LOBBY → MISSION BRIEFING → ITEM SHOP → CHALLENGES → RESULTS

### 1. Join or Host
- Players can create a new session and receive a unique code
- Or join an existing session using a host's code
- Each player enters their name (max 20 characters)

### 2. Lobby
- Team members assemble and see each other
- Host initiates the game when the group is ready
  
### 3. Mission Briefing
- The team learns their objective, location, and expected challenges
- Mission details are provided to inform equipment decisions
- Players review the briefing before proceeding to the shop

### 4. Item Shop (Auction Phase)
- Duration: 8 rounds of voting
- Team Budget: $1,000 (shared pool)
- Each round presents two items for purchase
- Team votes together on which item to buy
- Purchases continue until the budget is spent or all rounds complete

### 5. Mission Challenges
- The team executes the mission with purchased equipment
- Multiple challenges are presented sequentially
- Each challenge has a 60-second countdown timer
- Players select equipment to solve each challenge
- Points are awarded based on solution quality

### 6. Results
- Final score is displayed
- Breakdown of challenge successes and failures
- Summary of team performance

---

## Game Mechanics

### Shared Budget System
- All players share a single $1,000 team budget
- Equipment costs range from $20 to $600
- Strategic decisions about which items are essential
- Unused budget is lost (no refunds or carry-over)

### Collaborative Voting
- Every item purchase requires a team vote
- Votes are anonymous and simultaneous
- Majority vote determines the purchase
- Encourages discussion and strategic alignment

### Challenge Scoring
- Perfect solution (100 points) — Use the ideal equipment for the challenge
- Good solution (80-90 points) — Use acceptable equipment with minor issues
- Risky solution (50-60 points) — Use suboptimal equipment, success with problems
- Failed challenge (0 points) — Wrong equipment or miscalculation

### Mission Progression
- Team must complete challenges in sequence
- Each failure counts toward mission completion
- Mission ends after 3 total failures
- Completing all challenges without failure is the goal

---

## Available Missions
Missions vary by type and location:

Mission Types:

- Heist — Steal an artifact or jewel from a secure location
- Escape — Break free from hostile territory
- Rescue Op — Extract teammates from dangerous situations
- Rescue — Respond to distress signals and provide aid
- Survival — Repair bases or survive environmental challenges

Locations:

- Arctic Tundra
- Desert
- Jungle
- City
- Ocean
- Volcano

---

## Equipment Categories

Transportation - Vehicles for escape and movement
* Helicopter, Armoured Truck, Boat, Dune Buggy, Car, Snowmobile

Climbing & Heights - Tools for vertical navigation
* Paraglider, Ice Axes, Grappling Hook, Rope

Protection & Safety - Defensive and survival gear
* Gas Mask and Knockout Gas, Scuba Gear, Protective Goggles, Heat Resistant Suit, Thermal Clothing

Tools & Repair - Equipment for manipulation and repair
* Wire Cutters, Crowbar, Lock Picks, Toolkit, Welding Kit, Shovel, Axe

Navigation & Survival - Information and sustenance
* Compass, Map, Water Bottle, Water Purifier, Blanket, Flare Gun

Specialized Equipment - Mission-specific tools
* Explosives, Fire Starter Kit, Handheld Radios, Mirror, Animal Deterrent, Taser, Still-suit

---

## Strategy Tips

### Before Shopping
- Read the mission briefing thoroughly
- Identify the location and mission type
- Anticipate likely challenges
- Discuss team needs with your group

### During Shopping
- Prioritize essential equipment over luxury items
- Consider versatile items that work across multiple challenge types
- Allocate budget for flexibility (don't spend all $1,000 immediately)
- Discuss each vote and build consensus

### During Challenges
- Read the challenge description carefully
- Select equipment that directly addresses the problem
- Make deliberate choices under time pressure
- Communicate with your team even during timed rounds

### Common Mistakes to Avoid
- Spending entire budget too early in the shop
- Buying duplicate functions (two climbing tools when only one is needed)
- Ignoring environmental context in equipment selection
- Voting without discussion or justification
- Rushing decisions during timed challenges

---

## Testing

The repository includes automated tests using Selenium for browser-based gameplay validation and pytest for unit testing.

### Install Test Dependencies
```bash
pip install -r selenium_tests/requirements.txt
```

### Run Browser Integration Tests
```bash
pytest selenium_tests/
```

### Run Unit Tests
```bash
pytest tests/
```

### Test Coverage

Browser tests validate:
- Full game flow from join to results
- Session creation and player joining
- Mission briefing display and correctness
- Item shop voting mechanics
- Challenge execution sequences
- Results screen accuracy and scoring
- Multi-player state synchronization
- Session cleanup and player disconnection handling

---

## Deployment

Cloud Deployment
This project is deployed on Render and accessible at:
> https://cits3200-project.onrender.com/join

The application runs as a containerised Flask application using Gunicorn as the WSGI server.

---

## Contributing

This project follows a structured contribution workflow. Before working on new features or fixes, please review CONTRIBUTING.md for:
- Branch naming conventions (feature/, fix/, docs/)
- Commit message standards
- Pull request requirements
- Code review process
- Issue tracking

Quick Start for Contributors
```bash
git checkout main
git pull origin main
git checkout -b feature/your-feature-name
# Make your changes
git add .
git commit -m "feat: describe your changes"
git push origin feature/your-feature-name
# Open a pull request on GitHub
```

### Branch Naming
- feature/short-description — New features
- fix/short-description — Bug fixes
- docs/short-description — Documentation updates

### Commit Message Format
- feat: add new mission type
- fix: resolve player disconnect issue
- docs: add deployment guide
- chore: update dependencies

---

## Project Highlights

This project demonstrates professional software engineering skills across the full development stack:

### Full-Stack Development
- Complete game application from concept through production deployment
- Backend API with real-time communication and game state management
- Responsive, interactive frontend with pixel-art aesthetic
- Live deployment with monitoring and scaling

### Software Architecture
- Modular Flask application following best practices
- Clear separation of concerns (routes, handlers, game logic, data, services)
- Data-driven game mechanics enabling easy content extension
- Circular dependency resolution using the extensions pattern
- WebSocket integration for efficient real-time communication

### Code Quality
- Structured codebase with clear module organization
- Reusable components and templates
- Consistent naming conventions and project structure
- Well-documented code and configuration

### Collaboration and Documentation
- Team contribution guidelines and branching strategy
- Architectural decision records for major choices
- Clear README and onboarding documentation
- Professional project organization

### Testing and Validation
- Comprehensive browser-based integration testing
- Full game flow validation across multiple players
- Production deployment validation
- Test automation ensuring code quality

### Game Design
- Cooperative gameplay mechanics requiring team communication
- Real-time player interaction and state synchronization
- Strategic decision-making under time and resource constraints
- Replayable content through data-driven mission and challenge generation
- Balanced challenge progression and scoring system

### User Experience
- Intuitive game interface with clear visual hierarchy
- Responsive design supporting desktop and mobile
- Smooth animations and state transitions
- In-game guidance and help systems
- Accessibility considerations (keyboard navigation, button focus states)

---

## Known Issues and Limitations

Current Implementation
- Session data is stored in memory (resets on server restart)
- No player authentication system
- Limited to local network testing without production deployment
- Mobile UI optimizations in progress

---

## Client

- **Client:** [Yi Fei Wu / Canva]
- **Contact:** [yi.feiwu@canva.com]

---

## License
This project is provided as-is for educational and portfolio purposes. No explicit license is currently defined.

For use outside of the CITS3200 capstone context, please contact the development team or the project stakeholder (Yi Fei Wu).

