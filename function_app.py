import azure.functions as func
import json
from src.graph import graph

def main(req: func.HttpRequest) -> func.HttpResponse:
    # Get request body for POST method
    if req.method == "POST":
        try:
            req_body = req.get_json()
            url = req_body.get('url')
            
            if not url:
                return func.HttpResponse(
                    json.dumps({"error": "Please provide a URL in the request body"}),
                    mimetype="application/json",
                    status_code=400
                )

            input_state = {
                "url": url,
                "targets": [
                    "Determine if the company is publicly traded or privately held",
                    "Find the company's official CNPJ (Brazilian corporate tax ID number)",
                    "Retrieve the company's annual revenue or financial turnover figures",
                    "Identify the industry sector or market in which the company operates",
                    "Find the total number of employees currently working at the company",
                    "Look up employee satisfaction ratings or internal workplace reviews",
                    "Understand the company's business model, including how it generates and captures value",
                    "List the company's main products and services offered to consumers or businesses",
                    "Identify key suppliers or details about the company's supply chain operations"
                ]
            }

            result = graph.invoke(input_state)
            
            return func.HttpResponse(
                json.dumps({
                    "company_info": {
                        "public_private": result['answers'][0],
                        "cnpj": result['answers'][1],
                        "annual_revenue": result['answers'][2],
                        "industry": result['answers'][3],
                        "employees": result['answers'][4],
                        "satisfaction": result['answers'][5],
                        "business_model": result['answers'][6],
                        "products_services": result['answers'][7],
                        "supply_chain": result['answers'][8]
                    }
                }),
                mimetype="application/json"
            )

        except ValueError:
            return func.HttpResponse(
                json.dumps({"error": "Invalid request body"}),
                mimetype="application/json",
                status_code=400
            )
        except Exception as e:
            return func.HttpResponse(
                json.dumps({"error": str(e)}),
                mimetype="application/json",
                status_code=500
            )
    else:
        return func.HttpResponse(
            json.dumps({"error": "Please use POST method"}),
            mimetype="application/json",
            status_code=405
        )
