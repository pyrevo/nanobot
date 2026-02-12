import requests
import sys

def get_crypto_predictions(tag="Bitcoin"):
    """
    Cerca mercati su Polymarket relativi a Bitcoin (es. 'Bitcoin above $100k').
    Restituisce la probabilità (prezzo del 'Sì').
    """
    url = "https://gamma-api.polymarket.com/events"
    params = {
        "limit": 10,
        "active": "true",
        "closed": "false",
        "tag_slug": tag.lower()
    }
    
    try:
        response = requests.get(url, params=params)
        data = response.json()
        
        insights = []
        for event in data:
            title = event.get('title', '')
            # Filtriamo per mercati rilevanti al prezzo o eventi crypto
            markets = event.get('markets', [])
            if markets:
                # Prendi il primo mercato (solitamente il principale Binary)
                # Il prezzo del token 'Yes' è solitamente il primo elemento di groupOutcomePrices
                outcome_prices = markets[0].get('groupOutcomePrices', [])
                if outcome_prices:
                    prob = float(outcome_prices[0]) if outcome_prices[0] else 0.5
                    insights.append(f"Event: {title} -> Probability YES: {prob*100:.1f}%")
        
        if not insights:
            return f"Nessun mercato attivo trovato per {tag} su Polymarket."
            
        return "\n".join(insights)
    except Exception as e:
        return f"Errore lettura Polymarket: {str(e)}"

if __name__ == "__main__":
    search_tag = sys.argv[1] if len(sys.argv) > 1 else "Bitcoin"
    print(get_crypto_predictions(search_tag))
