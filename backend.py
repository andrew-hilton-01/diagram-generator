from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

from openai import OpenAI
from dotenv import load_dotenv
import os
example1input = """
A fitness center is developing a management system to streamline its operations, including member registration, class scheduling, and payment processing. The system should support the following key functions:

Member Registration: New members can sign up, creating profiles that store their personal information, membership details, and fitness goals.
Class Scheduling: Members can view available fitness classes, sign up for classes, and cancel their registrations. Staff can add, modify, or remove classes based on demand.
Payment Processing: The system should handle membership fees and class payments, ensuring secure transactions and providing receipts to members.
Attendance Tracking: The system needs to track member attendance in classes and record usage of gym facilities for better resource management.
Feedback and Support: Members can submit feedback and request support, which staff can review and respond to.
Requirements:
Each member should have a unique profile that includes personal details, membership status, and payment history.
The class schedule should reflect real-time availability and allow members to easily register or cancel.
Payment transactions must be secure and provide confirmation receipts.
The system should generate reports on class attendance and member engagement for management analysis.
Deliverables:
Create a Data Flow Diagram (DFD) for the fitness center management system, illustrating the following:
External entities (members, staff, payment processor).
Processes (member registration, class scheduling, payment processing, attendance tracking, feedback management).
Data stores (member profiles, class schedules, payment records, feedback).
Ensure that the DFD clearly shows the flow of information between processes and data stores, detailing the interactions among different components of the system.
Notes:
Use appropriate DFD symbols (circles for processes, arrows for data flows, open rectangles for data stores, and squares for external entities).
Include a context diagram for a high-level overview of the system.
"""
example1 = """
%%{init: {'theme': 'neutral'}}%%
flowchart TB
    %% Context Diagram
    subgraph "Fitness Center Management System [Context Diagram]"
        direction TB
        Member[Member] <--> System[Fitness Center Management System]
        Staff[Staff] <--> System
        PaymentProcessor[Payment Processor] <--> System
    end

    %% Level 1 Data Flow Diagram
    subgraph "Fitness Center Management System [Level 1 DFD]"
        direction TB

        %% Processes 
        P1[Member Registration]
        P2[Class Scheduling]
        P3[Payment Processing]
        P4[Attendance Tracking]
        P5[Feedback Management]

        %% Data Stores
        DS1[(Member Profiles)]
        DS2[(Class Schedules)]
        DS3[(Payment Records)]
        DS4[(Attendance Logs)]
        DS5[(Feedback Database)]

        %% External Entities
        Member1[Member]
        Staff1[Staff]
        PaymentProcessor1[Payment Processor]

        %% Data Flows
        Member1 -->|Personal Details| P1
        P1 -->|Member Profile| DS1

        Member1 -->|Class Request| P2
        Staff1 -->|Modify Classes| P2
        P2 -->|Updated Schedule| DS2

        Member1 -->|Payment Info| P3
        PaymentProcessor1 -->|Transaction Confirmation| P3
        P3 -->|Payment Details| DS3

        P2 -->|Class Attendance| P4
        P4 -->|Attendance Data| DS4

        Member1 -->|Feedback Submission| P5
        Staff1 -->|Support Response| P5
        P5 -->|Feedback Records| DS5
"""
example2input = """
An online bookstore is developing an e-commerce system to improve its operations, including book catalog management, order processing, and customer service. The system should support the following key functions:

Book Catalog Management: Admins can add, update, and remove books, including details like title, author, price, and stock availability. Customers can browse and search the catalog.

Order Processing: Customers can add books to their cart, place orders, and make payments. The system should handle order confirmation, invoice generation, and shipping details.

Payment Processing: Secure transactions should be supported, with confirmation receipts sent to customers upon successful payments.

Customer Accounts: Customers can create accounts to track order history, save preferences, and manage personal information.

Customer Support: Customers can submit queries or complaints, which support staff can review and respond to.

Requirements:
Each book must have a unique entry with complete details in the catalog.
Orders must be processed in real-time, ensuring stock availability before confirmation.
Payment transactions must be secure and provide receipts to customers.
The system should generate reports on sales, customer activity, and inventory levels.
Deliverables:
Create a Data Flow Diagram (DFD) for the online bookstore system, illustrating the following:

External entities (customers, admins, payment gateway, shipping provider).
Processes (book catalog management, order processing, payment handling, customer support).
Data stores (book database, order records, customer profiles, payment transactions, support requests).
Ensure that the DFD clearly shows the flow of information between processes and data stores, detailing the interactions among different components of the system.

Notes:

Use appropriate DFD symbols (circles for processes, arrows for data flows, open rectangles for data stores, and squares for external entities).
Include a context diagram for a high-level overview of the system.
"""
example2 = """
%%{init: {'theme': 'neutral'}}%%
flowchart TB
    %% Context Diagram
    subgraph "Online Bookstore E-Commerce System [Context Diagram]"
        direction TB
        Customer[Customer] <--> System[Online Bookstore System]
        Admin[Admin] <--> System
        PaymentGateway[Payment Gateway] <--> System
        ShippingProvider[Shipping Provider] <--> System
    end

    %% Level 1 Data Flow Diagram
    subgraph "Online Bookstore System [Level 1 DFD]"
        direction TB

        %% Processes
        P1[Book Catalog Management]
        P2[Order Processing]
        P3[Payment Handling]
        P4[Customer Account Management]
        P5[Customer Support]

        %% Data Stores
        DS1[(Book Database)]
        DS2[(Order Records)]
        DS3[(Customer Profiles)]
        DS4[(Payment Transactions)]
        DS5[(Support Requests)]

        %% External Entities
        Customer1[Customer]
        Admin1[Admin]
        PaymentGateway1[Payment Gateway]
        ShippingProvider1[Shipping Provider]

        %% Data Flows
        Admin1 -->|Book Information| P1
        P1 -->|Catalog Updates| DS1

        Customer1 -->|Search/Browse| P1
        P1 -->|Book Details| Customer1

        Customer1 -->|Order Creation| P2
        P2 -->|Order Details| DS2

        P2 -->|Payment Request| P3
        Customer1 -->|Payment Info| P3
        PaymentGateway1 -->|Transaction Confirmation| P3
        P3 -->|Payment Records| DS4

        Customer1 -->|Account Registration| P4
        P4 -->|Customer Profile| DS3

        Customer1 -->|Support Request| P5
        Admin1 -->|Support Response| P5
        P5 -->|Support Tickets| DS5

        P2 -->|Shipping Details| ShippingProvider1
        ShippingProvider1 -->|Delivery Confirmation| P2
    end
"""
# Load environment variables from .env file
load_dotenv()

app = FastAPI()

# Initialize OpenAI client with OpenRouter API key
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY"),
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

@app.post("/api/generate-mermaid")
async def generate_mermaid(request: Request):
    data = await request.json()
    prompt = data.get("prompt", "")

    if not prompt:
        raise HTTPException(status_code=400, detail="Prompt is required")

    try:
        completion = client.chat.completions.create(
            model="anthropic/claude-3.5-haiku-20241022:beta",
            messages=[
                {
                "role": "system",
                "content": "Create mermaid.js code for a data flow diagram (DFD). Respond with only the raw mermaid code, do not put in code-block. Base the graph content on the following scenario: "
                #This can be updated to include your customGPT instructions
                },
                {
                "role": "user",
                "content": f"Create a DFD for: {example1input}"
                },
                {
                "role": "assistant",
                "content": f"{example1}"
                },
                {
                "role": "user",
                "content": f"Create a DFD for: {example2input}"
                },
                {
                "role": "assistant",
                "content": f"{example2}"
                },
                {
                    "role": "user",
                    "content": f"Create a DFD for: {prompt}"
                }
            ]
        )
        mermaid_code = completion.choices[0].message.content
        return JSONResponse(content={"mermaid_code": mermaid_code})
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# To run the server, use: uvicorn backend:app --reload
